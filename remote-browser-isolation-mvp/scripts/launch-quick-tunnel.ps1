$ErrorActionPreference = "Stop"

$appDir = Split-Path -Parent $PSScriptRoot
$runtimeDir = Join-Path $appDir ".runtime"

New-Item -ItemType Directory -Path $runtimeDir -Force | Out-Null

$appOut = Join-Path $runtimeDir "app.out.log"
$appErr = Join-Path $runtimeDir "app.err.log"
$tunnelOut = Join-Path $runtimeDir "tunnel.out.log"
$tunnelErr = Join-Path $runtimeDir "tunnel.err.log"
$appPidFile = Join-Path $runtimeDir "app.pid"
$tunnelPidFile = Join-Path $runtimeDir "tunnel.pid"

Remove-Item $appOut, $appErr, $tunnelOut, $tunnelErr -ErrorAction SilentlyContinue

$appProc = Start-Process `
  -FilePath "cmd.exe" `
  -ArgumentList "/c", "set PORT=3100&& node src/server.js" `
  -WorkingDirectory $appDir `
  -WindowStyle Hidden `
  -RedirectStandardOutput $appOut `
  -RedirectStandardError $appErr `
  -PassThru

$appProc.Id | Set-Content $appPidFile

$healthy = $false
for ($i = 0; $i -lt 30; $i++) {
  Start-Sleep -Seconds 1
  try {
    $health = Invoke-RestMethod -Uri "http://localhost:3100/api/health" -Method Get -TimeoutSec 3
    if ($health.ok) {
      $healthy = $true
      break
    }
  } catch {
  }
}

if (-not $healthy) {
  Stop-Process -Id $appProc.Id -Force -ErrorAction SilentlyContinue
  Write-Output "APP_FAILED"
  if (Test-Path $appOut) { Get-Content $appOut -Tail 40 }
  if (Test-Path $appErr) { Get-Content $appErr -Tail 40 }
  exit 1
}

$cloudflared = "C:\Program Files (x86)\cloudflared\cloudflared.exe"

$tunnelProc = Start-Process `
  -FilePath $cloudflared `
  -ArgumentList "tunnel", "--url", "http://localhost:3100" `
  -WorkingDirectory $appDir `
  -WindowStyle Hidden `
  -RedirectStandardOutput $tunnelOut `
  -RedirectStandardError $tunnelErr `
  -PassThru

$tunnelProc.Id | Set-Content $tunnelPidFile

$url = $null
for ($i = 0; $i -lt 45; $i++) {
  Start-Sleep -Seconds 1
  $content = @()
  if (Test-Path $tunnelOut) { $content += Get-Content $tunnelOut -ErrorAction SilentlyContinue }
  if (Test-Path $tunnelErr) { $content += Get-Content $tunnelErr -ErrorAction SilentlyContinue }
  $match = $content | Select-String -Pattern "https://[-a-z0-9]+\.trycloudflare\.com" | Select-Object -Last 1
  if ($match) {
    $url = $match.Matches[0].Value
    break
  }
}

if (-not $url) {
  Stop-Process -Id $tunnelProc.Id -Force -ErrorAction SilentlyContinue
  Write-Output "TUNNEL_FAILED"
  if (Test-Path $tunnelOut) { Get-Content $tunnelOut -Tail 80 }
  if (Test-Path $tunnelErr) { Get-Content $tunnelErr -Tail 80 }
  exit 1
}

[pscustomobject]@{
  AppPid = $appProc.Id
  TunnelPid = $tunnelProc.Id
  LocalUrl = "http://localhost:3100"
  PublicUrl = $url
  AppLog = $appOut
  TunnelLog = $tunnelErr
} | ConvertTo-Json -Compress
