# KasmVNC Browser Workspace

This project launches isolated browser workspaces on demand and streams them back through your app domain.

## What it does

- Starts one `kasmweb/chromium` worker per session.
- Proxies KasmVNC HTTP + WebSocket traffic through the app.
- Supports both a guest-share portal and a private login portal on separate paths.
- Enforces per-user active session quotas.
- Uses server-only HTTP-only cookies for viewer binding (no session token in URL query params).
- Lists active sessions for the signed-in user and allows manual resume.
- Automatically resumes the most recent active session on startup/login when available.
- Supports optional profile persistence for saved browser state.
- Supports configurable audio mode (compressed compatibility mode or higher-fidelity PCM mode).
- Supports configurable Docker runtime selection (including microVM-capable runtimes when available).
- Supports optional built-in TLS and HTTPS enforcement.
- Includes a janitor loop that reaps orphaned worker containers after crashes/restarts.

## Architecture

```text
user browser
  -> Express app
     -> auth session cookie
     -> session manager
        -> docker run kasmweb/chromium
           -> Chromium workspace + KasmVNC
```

The browser worker is a real remote browser workspace, so sites like ChatGPT, Claude, and YouTube run directly in Chromium inside the worker.

## Prerequisites

- Node.js 22+
- Docker Desktop running locally

On Windows, if Docker is installed while terminals are already open, restart the terminal/Codex app shell so `docker` is available.

## Run

1. Install dependencies:

   ```powershell
   npm install
   ```

2. Copy `.env.example` to `.env` and adjust values.
   At minimum, set `RBI_USERS` to real credentials.

3. Start the app:

   ```powershell
   npm run dev
   ```

4. Open [http://localhost:3000](http://localhost:3000), then choose a portal:
   - `/share`: guest portal that anyone can use without a local app login
   - `/private`: restricted portal that only allows `RBI_PRIVATE_SITE_USERS`
5. If you already have active workers, use the session picker + `Resume` button, or just refresh/reopen the page to auto-reattach to the latest one.
6. For audio playback (YouTube/Spotify), click inside the remote session at least once so the browser can start audio output.

## Environment

### Core app

- `PORT`: app port
- `HOST`: bind host for the Express server
- `RBI_PUBLIC_BASE_URL`: public base URL used to build viewer URLs
- `RBI_TRUST_PROXY`: Express trust proxy setting (`true`, `false`, number, or value accepted by Express)
- `RBI_ENFORCE_HTTPS`: redirect HTTP requests to HTTPS

### Authentication + quotas

- `RBI_USERS`: comma-separated `username:password` list
- `RBI_ADMIN_USERS`: comma-separated usernames treated as local app admins
- `RBI_AUTH_COOKIE_NAME`: auth cookie name
- `RBI_PUBLIC_SITE_PATH`: path for the guest-share portal
- `RBI_PRIVATE_SITE_PATH`: path for the private login portal
- `RBI_PRIVATE_SITE_USERS`: comma-separated usernames allowed to log into the private portal
- `RBI_HOME_PC_USERS`: comma-separated usernames allowed to see the Home PC workspace option
- `RBI_HOME_PC_URL`: private remote desktop URL opened by the Home PC option, such as Chrome Remote Desktop
- `RBI_AUTH_SESSION_TTL_MINUTES`: auth session lifetime
- `RBI_MAX_SESSIONS_PER_USER`: per-user active session cap (`<=0` means no cap)

### Worker runtime

- `RBI_DOCKER_BIN`: Docker executable name or path
- `RBI_WORKER_PROVIDER`: worker provider (`docker`)
- `RBI_WORKSPACE_IMAGE`: workspace image (`kasmweb/chromium:1.17.0` by default)
- `RBI_DOCKER_RUNTIME`: optional Docker runtime (use this for microVM-capable runtimes when available, e.g. Kata in environments that support it)
- `RBI_ISOLATION_MODE`: optional label/metadata for health reporting
- `RBI_SESSION_TTL_MINUTES`: session lifetime
- `RBI_STARTUP_TIMEOUT_SECONDS`: startup wait timeout
- `RBI_LISTEN_HOST`: host interface for worker port mappings

### Profile persistence

- `RBI_PERSIST_PROFILES`: enable persisted browser profiles (`true/false`)
- `RBI_PROFILE_SCOPE`: `user` or `session`
- `RBI_PROFILE_VOLUME_PREFIX`: Docker volume prefix used when persistence is enabled
- `RBI_WORKSPACE_RESOLUTION`: initial KasmVNC desktop resolution
- `RBI_WORKSPACE_MAX_VIDEO_RESOLUTION`: maximum streamed video-mode resolution
- `RBI_WORKSPACE_MIN_QUALITY`: minimum dynamic stream quality (`0-9`)
- `RBI_WORKSPACE_MAX_QUALITY`: maximum dynamic stream quality (`0-9`)
- `RBI_WORKSPACE_BROWSER_ZOOM`: Chromium device scale factor for larger text, usually `1`, `1.25`, or `1.5`

### Audio

- `RBI_AUDIO_ENABLED`: enable or disable workspace audio streaming
- `RBI_AUDIO_PCM`: enable higher-fidelity PCM audio streaming (uses more bandwidth than the default compressed mode)

### Janitor

- `RBI_ENABLE_JANITOR`: enable orphan reaper
- `RBI_JANITOR_INTERVAL_SECONDS`: janitor sweep interval
- `RBI_APP_LABEL`: Docker label namespace for managed worker containers

### TLS

- `RBI_TLS_KEY_FILE`: TLS private key path
- `RBI_TLS_CERT_FILE`: TLS certificate path
- `RBI_TLS_CA_FILE`: optional CA bundle path

If `RBI_TLS_KEY_FILE` and `RBI_TLS_CERT_FILE` are set, the app serves HTTPS directly.

## Reverse proxy deployment notes

For production, place this app behind a reverse proxy that:

- Terminates HTTPS.
- Preserves `Upgrade` + `Connection` headers for WebSocket upgrades.
- Forwards `X-Forwarded-Proto` and `Host`.

The app already handles WebSocket upgrades and can enforce HTTPS (`RBI_ENFORCE_HTTPS=true`) when proxy headers are present.
