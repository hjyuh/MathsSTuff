import { randomBytes } from 'node:crypto';
import { execFile } from 'node:child_process';
import { accessSync, constants } from 'node:fs';
import http from 'node:http';
import https from 'node:https';
import path from 'node:path';
import net from 'node:net';
import { promisify } from 'node:util';

const execFileAsync = promisify(execFile);
const WORKSPACE_USERNAME = 'kasm_user';
const WORKSPACE_PORT = 6901;
const AUDIO_PORT = 4901;
const PUBLIC_CLOUDFLARE_DOH_TEMPLATE = 'https://cloudflare-dns.com/dns-query';

const DNS_MODE_DEFINITIONS = new Map([
  [
    'system',
    {
      label: 'Docker default DNS',
      servers: [],
      dohTemplate: ''
    }
  ],
  [
    'cloudflare-malware',
    {
      label: 'Cloudflare malware DNS',
      servers: ['1.1.1.2', '1.0.0.2'],
      dohTemplate: ''
    }
  ],
  [
    'cloudflare-family',
    {
      label: 'Cloudflare family DNS',
      servers: ['1.1.1.3', '1.0.0.3'],
      dohTemplate: ''
    }
  ],
  [
    'custom-dns',
    {
      label: 'Custom DNS servers',
      servers: [],
      dohTemplate: ''
    }
  ],
  [
    'browser-doh',
    {
      label: 'Chromium secure DNS',
      servers: [],
      dohTemplate: PUBLIC_CLOUDFLARE_DOH_TEMPLATE
    }
  ]
]);

export class SessionManager {
  constructor(options = {}) {
    this.workerProvider = options.workerProvider ?? 'docker';
    if (this.workerProvider !== 'docker') {
      throw new Error(`Unsupported worker provider "${this.workerProvider}". This build currently supports "docker".`);
    }

    this.dockerBin = options.dockerBin ?? 'docker';
    this.image = options.image ?? 'kasmweb/chromium:1.17.0';
    this.listenHost = options.listenHost ?? '127.0.0.1';
    this.streamPort = options.streamPort ?? WORKSPACE_PORT;
    this.sessionTtlMs = options.sessionTtlMs ?? 8 * 60 * 60 * 1000;
    this.browserStartupTimeoutMs = options.browserStartupTimeoutMs ?? 45 * 1000;
    this.containerPrefix = options.containerPrefix ?? 'rbi-session';
    this.appLabel = options.appLabel ?? 'remote-browser-isolation-mvp';
    this.instanceId = options.instanceId ?? createHexToken(6);
    this.dockerRuntime = options.dockerRuntime?.trim() || '';
    this.isolationMode = options.isolationMode ?? (this.dockerRuntime ? 'microvm-capable' : 'container');
    this.profilePersistenceEnabled = Boolean(options.profilePersistenceEnabled);
    this.profileScope = options.profileScope === 'session' ? 'session' : 'user';
    this.profileVolumePrefix = options.profileVolumePrefix ?? 'rbi-profile';
    this.workspaceResolution = normalizeResolution(options.workspaceResolution, '2560x1440');
    this.workspaceMaxVideoResolution = normalizeResolution(options.workspaceMaxVideoResolution, '3840x2160');
    this.workspaceMinQuality = normalizeQuality(options.workspaceMinQuality, 9);
    this.workspaceMaxQuality = normalizeQuality(options.workspaceMaxQuality, 9);
    this.workspaceBrowserZoom = normalizeZoom(options.workspaceBrowserZoom, 1.25);
    this.audioEnabled = options.audioEnabled ?? true;
    this.pcmAudioEnabled = options.pcmAudioEnabled ?? false;
    this.prepullWorkspaceImage = options.prepullWorkspaceImage ?? true;
    this.imagePullTimeoutMs = options.imagePullTimeoutMs ?? 15 * 60 * 1000;
    this.dnsLabEnabled = Boolean(options.dnsLabEnabled);
    this.defaultDnsProfile = normalizeDnsProfile({
      mode: options.defaultDnsMode,
      dnsServers: options.defaultDnsServers,
      dohTemplate: options.defaultDohTemplate
    });
    this.janitorEnabled = options.janitorEnabled ?? true;
    this.janitorIntervalMs = options.janitorIntervalMs ?? 2 * 60 * 1000;

    this.sessions = new Map();
    this.dockerVersionPromise = null;
    this.resolvedDockerBin = null;
    this.imageReadyPromise = null;
    this.imageWarmup = {
      ready: false,
      warming: false,
      lastError: '',
      lastStartedAt: null,
      lastCompletedAt: null
    };
    this.cleanupTimer = setInterval(() => {
      this.stopExpiredSessions().catch((error) => {
        console.error('Failed to reap expired sessions:', error);
      });
    }, 30 * 1000);
    this.cleanupTimer.unref?.();

    this.janitorTimer = null;
    if (this.janitorEnabled) {
      this.janitorTimer = setInterval(() => {
        this.reapOrphanedContainers('interval').catch((error) => {
          console.error('Janitor failed to reap orphaned containers:', error);
        });
      }, this.janitorIntervalMs);
      this.janitorTimer.unref?.();

      setTimeout(() => {
        this.reapOrphanedContainers('startup').catch((error) => {
          console.error('Janitor startup sweep failed:', error);
        });
      }, 0).unref?.();
    }

    if (this.prepullWorkspaceImage) {
      setTimeout(() => {
        this.queueWorkspaceImageWarmup('startup')?.catch((error) => {
          console.warn('Workspace image startup warmup failed:', error.message);
        });
      }, 0).unref?.();
    }
  }

  async getHealth() {
    try {
      const dockerVersion = await this.ensureDocker();
      this.queueWorkspaceImageWarmup('health')?.catch(() => {});
      const imageReady = this.prepullWorkspaceImage ? this.imageWarmup.ready : true;
      const warmingImage = this.prepullWorkspaceImage ? this.imageWarmup.warming : false;
      return {
        ok: imageReady,
        dockerAvailable: true,
        dockerVersion,
        image: this.image,
        imageReady,
        warmingImage,
        imageError: this.imageWarmup.lastError || null,
        imageLastStartedAt: this.imageWarmup.lastStartedAt?.toISOString() ?? null,
        imageLastCompletedAt: this.imageWarmup.lastCompletedAt?.toISOString() ?? null,
        activeSessions: this.sessions.size,
        workspacePort: this.streamPort,
        workerProvider: this.workerProvider,
        dockerRuntime: this.dockerRuntime || null,
        isolationMode: this.isolationMode,
        profilePersistenceEnabled: this.profilePersistenceEnabled,
        profileScope: this.profilePersistenceEnabled ? this.profileScope : null,
        workspaceResolution: this.workspaceResolution,
        workspaceMaxVideoResolution: this.workspaceMaxVideoResolution,
        workspaceQualityRange: `${this.workspaceMinQuality}-${this.workspaceMaxQuality}`,
        workspaceBrowserZoom: this.workspaceBrowserZoom,
        audioEnabled: this.audioEnabled,
        pcmAudioEnabled: this.audioEnabled ? this.pcmAudioEnabled : false,
        dnsLabEnabled: this.dnsLabEnabled,
        dnsDefaultProfile: serializeDnsProfile(this.defaultDnsProfile),
        dnsModes: getDnsModeOptions(),
        janitorEnabled: this.janitorEnabled
      };
    } catch (error) {
      return {
        ok: false,
        dockerAvailable: false,
        error: error.message,
        image: this.image,
        imageReady: false,
        warmingImage: this.prepullWorkspaceImage ? this.imageWarmup.warming : false,
        imageError: this.imageWarmup.lastError || null,
        imageLastStartedAt: this.imageWarmup.lastStartedAt?.toISOString() ?? null,
        imageLastCompletedAt: this.imageWarmup.lastCompletedAt?.toISOString() ?? null,
        activeSessions: this.sessions.size,
        workspacePort: this.streamPort,
        workerProvider: this.workerProvider,
        dockerRuntime: this.dockerRuntime || null,
        isolationMode: this.isolationMode,
        profilePersistenceEnabled: this.profilePersistenceEnabled,
        profileScope: this.profilePersistenceEnabled ? this.profileScope : null,
        workspaceResolution: this.workspaceResolution,
        workspaceMaxVideoResolution: this.workspaceMaxVideoResolution,
        workspaceQualityRange: `${this.workspaceMinQuality}-${this.workspaceMaxQuality}`,
        workspaceBrowserZoom: this.workspaceBrowserZoom,
        audioEnabled: this.audioEnabled,
        pcmAudioEnabled: this.audioEnabled ? this.pcmAudioEnabled : false,
        dnsLabEnabled: this.dnsLabEnabled,
        dnsDefaultProfile: serializeDnsProfile(this.defaultDnsProfile),
        dnsModes: getDnsModeOptions(),
        janitorEnabled: this.janitorEnabled
      };
    }
  }

  queueWorkspaceImageWarmup(reason = 'background') {
    if (!this.prepullWorkspaceImage || this.imageWarmup.ready || this.imageReadyPromise) {
      return this.imageReadyPromise;
    }

    this.imageWarmup.warming = true;
    this.imageWarmup.lastError = '';
    this.imageWarmup.lastStartedAt = new Date();

    this.imageReadyPromise = this.pullWorkspaceImage(reason)
      .then(() => {
        this.imageWarmup.ready = true;
        this.imageWarmup.warming = false;
        this.imageWarmup.lastCompletedAt = new Date();
      })
      .catch((error) => {
        this.imageWarmup.ready = false;
        this.imageWarmup.warming = false;
        this.imageWarmup.lastError = error.message;
        throw error;
      })
      .finally(() => {
        this.imageReadyPromise = null;
      });

    return this.imageReadyPromise;
  }

  async ensureWorkspaceImage() {
    if (this.imageWarmup.ready) {
      return;
    }

    const pendingWarmup = this.queueWorkspaceImageWarmup('session-create');
    if (pendingWarmup) {
      await pendingWarmup;
      return;
    }

    await this.pullWorkspaceImage('session-create');
    this.imageWarmup.ready = true;
    this.imageWarmup.warming = false;
    this.imageWarmup.lastCompletedAt = new Date();
  }

  async createSession(options = {}) {
    const ownerId = String(options.ownerId ?? '').trim();
    if (!ownerId) {
      throw new Error('Sessions require an authenticated owner.');
    }

    const dockerVersion = await this.ensureDocker();
    await this.ensureWorkspaceImage();
    const initialUrl = normalizeInitialUrl(options.initialUrl);
    const dnsProfile = this.resolveSessionDnsProfile(options.dnsProfile);
    const id = createHexToken(8);
    const viewerToken = createHexToken(24);
    const workspacePassword = createReadablePassword(14);
    const hostPort = await getFreePort(this.listenHost);
    const audioHostPort = this.audioEnabled ? await getFreePort(this.listenHost) : null;
    const createdAt = new Date();
    const expiresAt = new Date(createdAt.getTime() + this.sessionTtlMs);
    const containerName = `${this.containerPrefix}-${id}`;
    const profileVolumeName = this.resolveProfileVolumeName(ownerId, id);

    const workspaceAuthorization = `Basic ${Buffer.from(`${WORKSPACE_USERNAME}:${workspacePassword}`, 'utf8').toString('base64')}`;
    const session = {
      id,
      ownerId,
      viewerToken,
      containerName,
      profileVolumeName,
      hostPort,
      audioHostPort,
      state: 'starting',
      createdAt,
      expiresAt,
      dockerVersion,
      streamProtocol: 'https',
      initialUrl,
      dnsProfile,
      workspaceUsername: WORKSPACE_USERNAME,
      workspacePassword,
      workspaceAuthorization
    };

    this.sessions.set(id, session);

    try {
      await this.startContainer(session);
      await waitForEndpoint(`${session.streamProtocol}://${this.listenHost}:${hostPort}/`, this.browserStartupTimeoutMs, {
        rejectUnauthorized: false
      });
      session.state = 'ready';
      session.lastVerifiedAt = new Date();
      return this.serializeSession(session);
    } catch (error) {
      session.state = 'failed';
      session.lastError = error.message;
      await this.destroySession(id);
      throw error;
    }
  }

  getSession(id) {
    return this.sessions.get(id) ?? null;
  }

  getSessionForOwner(id, ownerId) {
    const session = this.getSession(id);
    if (!session || session.ownerId !== ownerId) {
      return null;
    }
    return session;
  }

  listSessionsForOwner(ownerId) {
    return [...this.sessions.values()]
      .filter((session) => session.ownerId === ownerId)
      .sort((left, right) => right.createdAt.getTime() - left.createdAt.getTime());
  }

  countSessionsForOwner(ownerId) {
    let count = 0;
    for (const session of this.sessions.values()) {
      if (session.ownerId === ownerId) {
        count += 1;
      }
    }
    return count;
  }

  validateViewerToken(id, viewerToken) {
    const session = this.getSession(id);
    return Boolean(session && viewerToken && session.viewerToken === viewerToken);
  }

  serializeSession(session) {
    return {
      id: session.id,
      ownerId: session.ownerId,
      cookieName: getCookieName(session.id),
      state: session.state,
      createdAt: session.createdAt.toISOString(),
      expiresAt: session.expiresAt.toISOString(),
      lastVerifiedAt: session.lastVerifiedAt?.toISOString() ?? null,
      hostPort: session.hostPort,
      audioHostPort: session.audioHostPort ?? null,
      streamProtocol: session.streamProtocol,
      connectPath: `/api/sessions/${session.id}/browser/`,
      dockerVersion: session.dockerVersion,
      profilePersistenceEnabled: Boolean(session.profileVolumeName),
      profileScope: session.profileVolumeName ? this.profileScope : null,
      dnsProfile: serializeDnsProfile(session.dnsProfile ?? this.defaultDnsProfile)
    };
  }

  async destroySession(id) {
    const session = this.getSession(id);
    if (!session) {
      return false;
    }

    this.sessions.delete(id);
    await runDocker(this.resolvedDockerBin ?? this.dockerBin, ['rm', '-f', session.containerName], {
      allowFailure: true
    });

    return true;
  }

  async shutdown() {
    clearInterval(this.cleanupTimer);
    if (this.janitorTimer) {
      clearInterval(this.janitorTimer);
    }
    const sessionIds = [...this.sessions.keys()];
    await Promise.allSettled(sessionIds.map((id) => this.destroySession(id)));
  }

  async ensureDocker() {
    if (!this.dockerVersionPromise) {
      this.dockerVersionPromise = this.resolveDockerBin()
        .then((dockerBin) =>
          execFileAsync(dockerBin, ['version', '--format', '{{.Server.Version}}'], {
            timeout: 5_000,
            env: buildDockerEnv(dockerBin)
          }).then(({ stdout }) => {
            this.resolvedDockerBin = dockerBin;
            return stdout.trim() || 'unknown';
          })
        )
        .catch((error) => {
          this.dockerVersionPromise = null;
          throw new Error(buildDockerErrorMessage(this.dockerBin, error));
        });
    }

    return this.dockerVersionPromise;
  }

  async pullWorkspaceImage(reason) {
    const dockerBin = await this.resolveDockerBin();
    await execFileAsync(dockerBin, ['pull', this.image], {
      timeout: this.imagePullTimeoutMs,
      env: buildDockerEnv(dockerBin)
    }).catch((error) => {
      const stderr = error.stderr?.trim();
      const stdout = error.stdout?.trim();
      const detail = stderr || stdout || error.message;
      throw new Error(`Workspace image warmup failed during ${reason}: ${detail}`);
    });
  }

  async startContainer(session) {
    const args = [
      'run',
      '-d',
      '--rm',
      '--name',
      session.containerName,
      '--label',
      'codex.rbi=true',
      '--label',
      `codex.rbi.app=${this.appLabel}`,
      '--label',
      `codex.rbi.instance=${this.instanceId}`,
      '--label',
      `codex.rbi.session=${session.id}`,
      '--label',
      `codex.rbi.owner=${sanitizeDockerName(session.ownerId)}`,
      '--label',
      `codex.rbi.dnsMode=${sanitizeDockerName(session.dnsProfile.mode)}`,
      '-p',
      `${this.listenHost}:${session.hostPort}:${this.streamPort}`,
      '--shm-size=1g',
      '-e',
      `VNC_PW=${session.workspacePassword}`,
      '-e',
      `VNCOPTIONS=${this.buildVncOptions()}`,
      '-e',
      `VNC_RESOLUTION=${this.workspaceResolution}`,
      '-e',
      `CHROME_CLI=${this.buildChromeCli(session.initialUrl, session.dnsProfile)}`,
      '-e',
      `KASM_SVC_AUDIO=${this.audioEnabled ? '1' : '0'}`
    ];

    for (const dnsServer of session.dnsProfile.servers) {
      args.push('--dns', dnsServer);
    }

    if (session.audioHostPort) {
      args.push('-p', `${this.listenHost}:${session.audioHostPort}:${AUDIO_PORT}`);
    }

    if (this.pcmAudioEnabled) {
      args.push('-e', 'PCM_AUDIO=1');
    }

    if (this.dockerRuntime) {
      args.push('--runtime', this.dockerRuntime);
    }

    if (session.profileVolumeName) {
      args.push('--label', `codex.rbi.profile=${session.profileVolumeName}`);
      args.push('--volume', `${session.profileVolumeName}:/home/kasm-user`);
    }

    args.push(this.image);

    await runDocker(this.resolvedDockerBin ?? this.dockerBin, args, {
      timeoutMs: 10 * 60 * 1000
    });
  }

  async stopExpiredSessions() {
    const now = Date.now();
    const expiredIds = [...this.sessions.values()]
      .filter((session) => session.expiresAt.getTime() <= now)
      .map((session) => session.id);

    if (!expiredIds.length) {
      return;
    }

    await Promise.allSettled(expiredIds.map((id) => this.destroySession(id)));
  }

  async reapOrphanedContainers(reason = 'interval') {
    const names = await this.listManagedContainerNames();
    if (!names.length) {
      return 0;
    }

    const liveNames = new Set([...this.sessions.values()].map((session) => session.containerName));
    const orphaned = names.filter((name) => !liveNames.has(name));

    if (!orphaned.length) {
      return 0;
    }

    await Promise.allSettled(
      orphaned.map((name) =>
        runDocker(this.resolvedDockerBin ?? this.dockerBin, ['rm', '-f', name], {
          allowFailure: true
        })
      )
    );

    console.log(`[janitor] Reaped ${orphaned.length} orphaned worker container(s) during ${reason} sweep.`);
    return orphaned.length;
  }

  async listManagedContainerNames() {
    const output = await runDocker(
      this.resolvedDockerBin ?? this.dockerBin,
      ['ps', '-a', '--filter', 'label=codex.rbi=true', '--filter', `label=codex.rbi.app=${this.appLabel}`, '--format', '{{.Names}}'],
      { allowFailure: true }
    );

    if (!output) {
      return [];
    }

    return output
      .split(/\r?\n/g)
      .map((line) => line.trim())
      .filter(Boolean);
  }

  resolveProfileVolumeName(ownerId, sessionId) {
    if (!this.profilePersistenceEnabled) {
      return null;
    }

    const scopeKey = this.profileScope === 'session' ? sessionId : ownerId;
    const suffix = sanitizeDockerName(scopeKey);
    return `${sanitizeDockerName(this.profileVolumePrefix)}-${suffix}`.slice(0, 128);
  }

  buildVncOptions() {
    return [
      '-DisableBasicAuth',
      '-geometry',
      this.workspaceResolution,
      '-DynamicQualityMin',
      String(this.workspaceMinQuality),
      '-DynamicQualityMax',
      String(this.workspaceMaxQuality),
      '-JpegVideoQuality',
      String(this.workspaceMaxQuality),
      '-WebpVideoQuality',
      String(this.workspaceMaxQuality),
      '-MaxVideoResolution',
      this.workspaceMaxVideoResolution
    ].join(' ');
  }

  resolveSessionDnsProfile(input) {
    if (!this.dnsLabEnabled) {
      return this.defaultDnsProfile;
    }

    return normalizeDnsProfile(input, this.defaultDnsProfile);
  }

  buildChromeCli(initialUrl, dnsProfile) {
    const args = [
      `--force-device-scale-factor=${this.workspaceBrowserZoom}`,
      '--high-dpi-support=1'
    ];

    if (dnsProfile?.dohTemplate) {
      args.push('--dns-over-https-mode=secure');
      args.push(`--dns-over-https-templates=${dnsProfile.dohTemplate}`);
    } else {
      args.push('--dns-over-https-mode=off');
    }

    if (initialUrl) {
      args.push(initialUrl);
    }

    return args.join(' ');
  }
}

async function runDocker(dockerBin, args, options = {}) {
  try {
    const { stdout } = await execFileAsync(dockerBin, args, {
      timeout: options.timeoutMs ?? 30_000,
      env: buildDockerEnv(dockerBin)
    });
    return stdout.trim();
  } catch (error) {
    if (options.allowFailure) {
      return '';
    }

    const stderr = error.stderr?.trim();
    const stdout = error.stdout?.trim();
    const detail = stderr || stdout || error.message;
    throw new Error(`Docker command failed: ${dockerBin} ${args.join(' ')}. ${detail}`);
  }
}

SessionManager.prototype.resolveDockerBin = async function resolveDockerBin() {
  if (this.resolvedDockerBin) {
    return this.resolvedDockerBin;
  }

  const candidates = getDockerCandidates(this.dockerBin);

  for (const candidate of candidates) {
    try {
      if (isAbsolutePath(candidate)) {
        accessSync(candidate, constants.F_OK);
      }

      this.resolvedDockerBin = candidate;
      return candidate;
    } catch {
      continue;
    }
  }

  return this.dockerBin;
};

function createHexToken(bytes) {
  return randomBytes(bytes).toString('hex');
}

function createReadablePassword(length) {
  const alphabet = 'ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz23456789';
  let password = '';

  while (password.length < length) {
    const buffer = randomBytes(length);
    for (const value of buffer) {
      password += alphabet[value % alphabet.length];
      if (password.length === length) {
        break;
      }
    }
  }

  return password;
}

export function getCookieName(sessionId) {
  return `rbi_session_${sessionId}`;
}

function getFreePort(host) {
  return new Promise((resolve, reject) => {
    const server = net.createServer();

    server.unref();
    server.on('error', reject);
    server.listen(0, host, () => {
      const address = server.address();
      if (!address || typeof address === 'string') {
        server.close(() => {
          reject(new Error('Could not allocate a TCP port for the browser worker.'));
        });
        return;
      }

      const { port } = address;
      server.close((error) => {
        if (error) {
          reject(error);
          return;
        }

        resolve(port);
      });
    });
  });
}

function waitForEndpoint(url, timeoutMs, options = {}) {
  const client = url.startsWith('https:') ? https : http;
  const startedAt = Date.now();

  return new Promise((resolve, reject) => {
    const attempt = () => {
      const request = client.get(url, options, (response) => {
        response.resume();

        if (response.statusCode && response.statusCode < 500) {
          resolve();
          return;
        }

        maybeRetry(new Error(`Browser worker returned HTTP ${response.statusCode ?? 'unknown'}.`));
      });

      request.setTimeout(3_000, () => {
        request.destroy(new Error('Browser worker did not respond in time.'));
      });

      request.on('error', maybeRetry);
    };

    const maybeRetry = (error) => {
      if (Date.now() - startedAt >= timeoutMs) {
        reject(new Error(`Browser worker failed to become ready within ${Math.ceil(timeoutMs / 1000)} seconds. ${error.message}`));
        return;
      }

      setTimeout(attempt, 1_000).unref?.();
    };

    attempt();
  });
}

function getDockerCandidates(configuredDockerBin) {
  const candidates = [];

  if (process.platform === 'win32') {
    candidates.push('C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe');
  }

  candidates.push(configuredDockerBin);

  if (process.platform !== 'win32') {
    candidates.push('/usr/local/bin/docker', '/usr/bin/docker');
  }

  return [...new Set(candidates.filter(Boolean))];
}

function isAbsolutePath(value) {
  return value.includes('\\') || value.startsWith('/');
}

function sanitizeDockerName(value) {
  const cleaned = String(value ?? '')
    .toLowerCase()
    .replace(/[^a-z0-9_.-]+/g, '-')
    .replace(/^-+|-+$/g, '');

  if (!cleaned) {
    return 'anon';
  }

  return cleaned.slice(0, 80);
}

function normalizeResolution(value, fallback) {
  const normalized = String(value ?? '').trim().toLowerCase();
  return /^\d{3,5}x\d{3,5}$/.test(normalized) ? normalized : fallback;
}

function normalizeQuality(value, fallback) {
  const parsed = Number(value);
  if (!Number.isFinite(parsed)) {
    return fallback;
  }
  return Math.max(0, Math.min(9, Math.round(parsed)));
}

function normalizeZoom(value, fallback) {
  const parsed = Number(value);
  if (!Number.isFinite(parsed)) {
    return fallback;
  }
  return Math.max(1, Math.min(2, Number(parsed.toFixed(2))));
}

function normalizeInitialUrl(value) {
  const raw = String(value ?? '').trim();
  if (!raw) {
    return '';
  }

  try {
    const url = new URL(raw);
    if (url.protocol !== 'https:' && url.protocol !== 'http:') {
      return '';
    }
    return url.toString();
  } catch {
    return '';
  }
}

function getDnsModeOptions() {
  return [...DNS_MODE_DEFINITIONS.entries()].map(([mode, definition]) => ({
    mode,
    label: definition.label,
    servers: definition.servers,
    dohTemplate: definition.dohTemplate
  }));
}

function normalizeDnsProfile(input = {}, fallbackProfile = null) {
  const requestedMode = String(input?.mode ?? fallbackProfile?.mode ?? 'system').trim().toLowerCase();
  const definition = DNS_MODE_DEFINITIONS.get(requestedMode);
  if (!definition) {
    throw new Error(`Invalid DNS lab mode "${requestedMode}".`);
  }

  const profile = {
    mode: requestedMode,
    label: definition.label,
    servers: [...definition.servers],
    dohTemplate: definition.dohTemplate
  };

  if (requestedMode === 'custom-dns') {
    const servers = parseDnsServers(input?.dnsServers ?? input?.servers ?? fallbackProfile?.servers ?? []);
    if (!servers.length) {
      throw new Error('Custom DNS mode requires at least one DNS server IP address.');
    }
    profile.servers = servers;
  }

  if (requestedMode === 'browser-doh') {
    const dohTemplate = normalizeDohTemplate(input?.dohTemplate ?? fallbackProfile?.dohTemplate ?? definition.dohTemplate);
    if (!dohTemplate) {
      throw new Error('Chromium secure DNS mode requires a DoH HTTPS template.');
    }
    profile.dohTemplate = dohTemplate;
    profile.servers = parseDnsServers(input?.dnsServers ?? input?.servers ?? fallbackProfile?.servers ?? []);
  }

  return profile;
}

function serializeDnsProfile(profile) {
  const normalized = normalizeDnsProfile(profile);
  return {
    mode: normalized.mode,
    label: normalized.label,
    servers: normalized.servers,
    dohTemplate: normalized.dohTemplate
  };
}

function parseDnsServers(value) {
  const rawValues = Array.isArray(value) ? value : String(value ?? '').split(/[,\s]+/g);
  const servers = [];
  for (const rawValue of rawValues) {
    const server = String(rawValue ?? '').trim();
    if (!server) {
      continue;
    }

    if (!net.isIP(server)) {
      throw new Error(`Invalid DNS server "${server}". Use IPv4 or IPv6 addresses only.`);
    }

    if (!servers.includes(server)) {
      servers.push(server);
    }
  }

  if (servers.length > 6) {
    throw new Error('DNS lab mode supports up to 6 DNS server addresses per session.');
  }

  return servers;
}

function normalizeDohTemplate(value) {
  const raw = String(value ?? '').trim();
  if (!raw) {
    return '';
  }

  if (raw.length > 2048 || /\s/.test(raw)) {
    throw new Error('DoH template must be a single HTTPS URL under 2048 characters.');
  }

  if (!/^https:\/\/[^/?#{}]+(?:[/?#]|$)/i.test(raw)) {
    throw new Error('DoH template must start with an HTTPS URL, such as https://cloudflare-dns.com/dns-query.');
  }

  return raw;
}

function buildDockerErrorMessage(configuredDockerBin, error) {
  const detail = error?.message ?? String(error);

  if (/\bENOENT\b/i.test(detail) || /not recognized as the name of a cmdlet/i.test(detail)) {
    return `Docker is required to launch browser workers. Docker Desktop appears to be installed, but this shell cannot find "${configuredDockerBin}" yet. Restart the terminal or Codex app after installing Docker, or set RBI_DOCKER_BIN to the full path. Original error: ${detail}`;
  }

  if (
    /docker_engine/i.test(detail) ||
    /daemon is running/i.test(detail) ||
    /cannot find the file specified/i.test(detail) ||
    /internal server error/i.test(detail) ||
    /dockerdesktoplinuxengine/i.test(detail)
  ) {
    return `Docker Desktop is installed, but the engine is not ready yet. Open Docker Desktop and wait until it shows Engine running, then retry. First launch can take around a minute while WSL is provisioned. Original error: ${detail}`;
  }

  return `Docker is required to launch browser workers. Install Docker Desktop and make sure "${configuredDockerBin}" is usable from this shell. Original error: ${detail}`;
}

function buildDockerEnv(dockerBin) {
  if (!isAbsolutePath(dockerBin)) {
    return process.env;
  }

  const dockerDir = path.dirname(dockerBin);
  const currentPath = process.env.PATH ?? process.env.Path ?? '';

  return {
    ...process.env,
    PATH: [dockerDir, currentPath].filter(Boolean).join(path.delimiter),
    Path: [dockerDir, currentPath].filter(Boolean).join(path.delimiter)
  };
}
