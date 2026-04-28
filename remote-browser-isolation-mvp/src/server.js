import 'dotenv/config';
import express from 'express';
import fs from 'node:fs';
import http from 'node:http';
import https from 'node:https';
import net from 'node:net';
import path from 'node:path';
import tls from 'node:tls';
import { fileURLToPath } from 'node:url';
import { AuthManager } from './auth-manager.js';
import { SessionManager, getCookieName } from './session-manager.js';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const publicDir = path.join(__dirname, '..', 'public');
const appShellTemplate = fs.readFileSync(path.join(publicDir, 'index.html'), 'utf8');

const config = {
  port: Number(process.env.PORT ?? 3000),
  host: process.env.HOST ?? '0.0.0.0',
  publicBaseUrl: process.env.RBI_PUBLIC_BASE_URL?.trim() || '',
  trustProxy: parseTrustProxy(process.env.RBI_TRUST_PROXY),
  enforceHttps: parseBoolean(process.env.RBI_ENFORCE_HTTPS, false),
  tlsKeyFile: process.env.RBI_TLS_KEY_FILE?.trim() || '',
  tlsCertFile: process.env.RBI_TLS_CERT_FILE?.trim() || '',
  tlsCaFile: process.env.RBI_TLS_CA_FILE?.trim() || '',
  authCookieName: process.env.RBI_AUTH_COOKIE_NAME?.trim() || 'rbi_auth',
  publicSitePath: normalizeSitePath(process.env.RBI_PUBLIC_SITE_PATH ?? '/share'),
  privateSitePath: normalizeSitePath(process.env.RBI_PRIVATE_SITE_PATH ?? '/private'),
  privateSiteUsers: parseUsernames(process.env.RBI_PRIVATE_SITE_USERS, ['malek', 'hman']),
  homePcUsers: parseUsernames(process.env.RBI_HOME_PC_USERS, ['malek']),
  homePcUrl: process.env.RBI_HOME_PC_URL?.trim() || '',
  authSessionTtlMs: Number(process.env.RBI_AUTH_SESSION_TTL_MINUTES ?? 720) * 60 * 1000,
  users: parseUsers(process.env.RBI_USERS, parseUsernames(process.env.RBI_ADMIN_USERS, ['malek'])),
  maxSessionsPerUser: Number(process.env.RBI_MAX_SESSIONS_PER_USER ?? 2),
  sessionTtlMs: Number(process.env.RBI_SESSION_TTL_MINUTES ?? 480) * 60 * 1000,
  browserStartupTimeoutMs: Number(process.env.RBI_STARTUP_TIMEOUT_SECONDS ?? 45) * 1000,
  dockerBin: process.env.RBI_DOCKER_BIN ?? 'docker',
  workspaceImage: process.env.RBI_WORKSPACE_IMAGE ?? process.env.RBI_SELENIUM_IMAGE ?? 'kasmweb/chromium:1.17.0',
  listenHost: process.env.RBI_LISTEN_HOST ?? '127.0.0.1',
  workerProvider: process.env.RBI_WORKER_PROVIDER?.trim() || 'docker',
  dockerRuntime: process.env.RBI_DOCKER_RUNTIME?.trim() || '',
  isolationMode: process.env.RBI_ISOLATION_MODE?.trim() || '',
  profilePersistenceEnabled: parseBoolean(process.env.RBI_PERSIST_PROFILES, false),
  profileScope: process.env.RBI_PROFILE_SCOPE?.trim() || 'user',
  profileVolumePrefix: process.env.RBI_PROFILE_VOLUME_PREFIX?.trim() || 'rbi-profile',
  workspaceResolution: process.env.RBI_WORKSPACE_RESOLUTION?.trim() || '2560x1440',
  workspaceMaxVideoResolution: process.env.RBI_WORKSPACE_MAX_VIDEO_RESOLUTION?.trim() || '3840x2160',
  workspaceMinQuality: Number(process.env.RBI_WORKSPACE_MIN_QUALITY ?? 9),
  workspaceMaxQuality: Number(process.env.RBI_WORKSPACE_MAX_QUALITY ?? 9),
  workspaceBrowserZoom: Number(process.env.RBI_WORKSPACE_BROWSER_ZOOM ?? 1.25),
  audioEnabled: parseBoolean(process.env.RBI_AUDIO_ENABLED, true),
  pcmAudioEnabled: parseBoolean(process.env.RBI_AUDIO_PCM, false),
  dnsLabEnabled: parseBoolean(process.env.RBI_DNS_LAB_ENABLED, false),
  workerDnsMode: process.env.RBI_WORKER_DNS_MODE?.trim() || 'system',
  workerDnsServers: process.env.RBI_WORKER_DNS_SERVERS?.trim() || '',
  chromeDohTemplate: process.env.RBI_CHROME_DOH_TEMPLATE?.trim() || '',
  janitorEnabled: parseBoolean(process.env.RBI_ENABLE_JANITOR, true),
  janitorIntervalMs: Number(process.env.RBI_JANITOR_INTERVAL_SECONDS ?? 120) * 1000,
  appLabel: process.env.RBI_APP_LABEL?.trim() || 'remote-browser-isolation-mvp'
};

if (!config.users.length) {
  console.warn('No RBI_USERS configured. Falling back to default admin user (admin/change-me-now). Set RBI_USERS for production.');
  config.users.push({
    username: 'admin',
    password: 'change-me-now',
    isAdmin: true
  });
}

const sites = buildSiteConfigs(config);
const siteByKey = new Map(sites.map((site) => [site.key, site]));
const appShellByKey = new Map(sites.map((site) => [site.key, renderAppShell(site)]));
const landingPageHtml = renderLandingPage(sites);

const tlsOptions = loadTlsOptions(config);
const servingScheme = tlsOptions ? 'https' : 'http';
const hasExplicitPort = process.env.PORT != null;
let runtimePort = config.port;

const authManager = new AuthManager({
  users: config.users,
  sessionTtlMs: config.authSessionTtlMs
});

const sessionManager = new SessionManager({
  dockerBin: config.dockerBin,
  image: config.workspaceImage,
  listenHost: config.listenHost,
  sessionTtlMs: config.sessionTtlMs,
  browserStartupTimeoutMs: config.browserStartupTimeoutMs,
  workerProvider: config.workerProvider,
  dockerRuntime: config.dockerRuntime,
  isolationMode: config.isolationMode || undefined,
  profilePersistenceEnabled: config.profilePersistenceEnabled,
  profileScope: config.profileScope,
  profileVolumePrefix: config.profileVolumePrefix,
  workspaceResolution: config.workspaceResolution,
  workspaceMaxVideoResolution: config.workspaceMaxVideoResolution,
  workspaceMinQuality: config.workspaceMinQuality,
  workspaceMaxQuality: config.workspaceMaxQuality,
  workspaceBrowserZoom: config.workspaceBrowserZoom,
  audioEnabled: config.audioEnabled,
  pcmAudioEnabled: config.pcmAudioEnabled,
  dnsLabEnabled: config.dnsLabEnabled,
  defaultDnsMode: config.workerDnsMode,
  defaultDnsServers: config.workerDnsServers,
  defaultDohTemplate: config.chromeDohTemplate,
  janitorEnabled: config.janitorEnabled,
  janitorIntervalMs: config.janitorIntervalMs,
  appLabel: config.appLabel
});

const app = express();
const server = tlsOptions ? https.createServer(tlsOptions, app) : http.createServer(app);
const useSecureCookies = config.publicBaseUrl.startsWith('https://') || Boolean(tlsOptions) || config.enforceHttps;

app.set('trust proxy', config.trustProxy);
app.disable('x-powered-by');
app.use(express.json({ limit: '32kb' }));

if (config.enforceHttps) {
  app.use((request, response, next) => {
    const forwardedProto = request.get('x-forwarded-proto');
    const isSecure = request.secure || (forwardedProto && forwardedProto.split(',')[0].trim() === 'https');
    if (isSecure) {
      next();
      return;
    }

    const host = request.get('x-forwarded-host') || request.get('host');
    if (!host) {
      response.status(400).json({
        error: 'HTTPS is required.'
      });
      return;
    }

    response.redirect(308, `https://${host}${request.originalUrl}`);
  });
}

app.use(express.static(publicDir, { index: false }));

for (const site of sites) {
  app.use(site.apiBasePath, buildSiteRouter(site));
}

app.get('/', (_request, response) => {
  response.type('html').send(landingPageHtml);
});

for (const site of sites) {
  app.get(site.path, (_request, response) => {
    response.type('html').send(appShellByKey.get(site.key));
  });
  app.get(site.shellMatcher, (_request, response) => {
    response.type('html').send(appShellByKey.get(site.key));
  });
}

server.on('upgrade', (request, socket, head) => {
  socket.on('error', (error) => {
    if (error?.code !== 'ECONNRESET') {
      console.error('Browser upgrade socket error:', error);
    }
  });

  const parsed = getBrowserRequest(request.url, request.headers.host);
  if (!parsed) {
    return;
  }

  const site = siteByKey.get(parsed.siteKey);
  if (!site) {
    socket.write('HTTP/1.1 404 Not Found\r\n\r\n');
    socket.destroy();
    return;
  }

  const authSession = readAuthSession(request, site);
  if (!authSession) {
    socket.write('HTTP/1.1 401 Unauthorized\r\n\r\n');
    socket.destroy();
    return;
  }

  const session = sessionManager.getSessionForOwner(parsed.sessionId, authSession.user.id);
  if (!session) {
    socket.write('HTTP/1.1 404 Not Found\r\n\r\n');
    socket.destroy();
    return;
  }

  const viewerToken = readCookie(request, getCookieName(parsed.sessionId));
  if (!sessionManager.validateViewerToken(parsed.sessionId, viewerToken)) {
    socket.write('HTTP/1.1 401 Unauthorized\r\n\r\n');
    socket.destroy();
    return;
  }

  request.rbiSession = session;
  request.rbiSite = site;
  proxyBrowserWs(request, socket, head);
});

const activeSignals = ['SIGINT', 'SIGTERM'];
for (const signal of activeSignals) {
  process.on(signal, async () => {
    await shutdown(signal);
  });
}

process.on('uncaughtException', async (error) => {
  if (error?.code === 'ECONNRESET') {
    console.warn('Ignoring socket reset from browser stream.');
    return;
  }

  console.error('Uncaught exception:', error);
  await shutdown('uncaughtException', 1);
});

process.on('unhandledRejection', async (error) => {
  console.error('Unhandled rejection:', error);
  await shutdown('unhandledRejection', 1);
});

server.on('error', (error) => {
  if (!hasExplicitPort && error.code === 'EADDRINUSE') {
    (async () => {
      try {
        const fallbackPort = await getFreePort(config.host);
        runtimePort = fallbackPort;
        console.warn(
          `Port ${config.port} is already in use. Falling back to ${servingScheme}://${config.host === '0.0.0.0' ? 'localhost' : config.host}:${fallbackPort}`
        );
        server.listen(fallbackPort, config.host);
      } catch (fallbackError) {
        console.error('Failed to allocate fallback port:', fallbackError);
        await shutdown('serverError', 1);
      }
    })();
    return;
  }

  if (error.code === 'EADDRINUSE') {
    console.error(
      `Port ${config.port} is already in use. Stop the other process or start this app with a different PORT (for example: PORT=3001 npm run dev).`
    );
  } else {
    console.error('Server startup error:', error);
  }
  shutdown('serverError', 1).catch((shutdownError) => {
    console.error('Shutdown after server error failed:', shutdownError);
    process.exit(1);
  });
});

server.listen(config.port, config.host, onListening);

let shuttingDown = false;

async function shutdown(reason, exitCode = 0) {
  if (shuttingDown) {
    return;
  }

  shuttingDown = true;
  console.log(`Shutting down because of ${reason}.`);

  server.close();
  authManager.shutdown();
  await sessionManager.shutdown();
  process.exit(exitCode);
}

function buildSiteRouter(site) {
  const router = express.Router();
  const requireSiteAuth = createRequireAuth(site);

  router.get('/health', async (_request, response) => {
    const health = await sessionManager.getHealth();
    response.status(health.ok ? 200 : 503).json({
      ...health,
      ttlMinutes: Math.round(config.sessionTtlMs / 60_000),
      authSessionTtlMinutes: Math.round(config.authSessionTtlMs / 60_000),
      maxSessionsPerUser: config.maxSessionsPerUser,
      site: serializeSite(site)
    });
  });

  router.post('/auth/login', (request, response) => {
    if (site.authMode === 'guest') {
      response.status(405).json({
        error: 'This portal signs visitors in automatically.'
      });
      return;
    }

    const username = String(request.body?.username ?? '').trim();
    const password = String(request.body?.password ?? '');

    if (!username || !password) {
      response.status(400).json({
        error: 'Username and password are required.'
      });
      return;
    }

    if (!siteAllowsUser(site, username)) {
      response.status(403).json({
        error: 'That account is not allowed on this portal.'
      });
      return;
    }

    const authSession = authManager.authenticate(username, password);
    if (!authSession) {
      response.status(401).json({
        error: 'Invalid username or password.'
      });
      return;
    }

    response.cookie(site.authCookieName, authSession.token, authCookieOptions(site));
    response.json({
      user: authSession.user,
      expiresAt: authSession.expiresAt
    });
  });

  router.post('/auth/logout', (request, response) => {
    const token = readCookie(request, site.authCookieName);
    if (token) {
      authManager.revoke(token);
    }

    response.clearCookie(site.authCookieName, {
      ...authCookieOptions(site),
      maxAge: undefined
    });
    response.status(204).end();
  });

  router.get('/auth/me', (request, response) => {
    const authSession = ensureSiteAuthSession(request, response, site);
    if (!authSession) {
      response.status(401).json({
        error: 'Authentication required.'
      });
      return;
    }

    const activeSessions = sessionManager.countSessionsForOwner(authSession.user.id);
    response.json({
      user: authSession.user,
      expiresAt: authSession.expiresAt,
      activeSessions,
      maxSessionsPerUser: config.maxSessionsPerUser,
      homePc: buildHomePcCapability(authSession.user),
      site: serializeSite(site)
    });
  });

  router.get('/admin/credentials', requireSiteAuth, requireAdmin, (_request, response) => {
    response.json({
      users: config.users.map((user) => ({
        username: user.username,
        password: user.password,
        isAdmin: Boolean(user.isAdmin)
      }))
    });
  });

  router.post('/sessions', requireSiteAuth, async (request, response) => {
    try {
      const initialUrl = normalizeInitialUrl(request.body?.initialUrl);
      if (initialUrl) {
        const homePcCapability = buildHomePcCapability(request.rbiUser);
        if (!homePcCapability.allowed || initialUrl !== homePcCapability.url) {
          response.status(403).json({
            error: 'That startup URL is not allowed for this account.'
          });
          return;
        }
      }

      const activeSessions = sessionManager.countSessionsForOwner(request.rbiUser.id);
      if (config.maxSessionsPerUser > 0 && activeSessions >= config.maxSessionsPerUser) {
        response.status(429).json({
          error: `Session quota reached (${config.maxSessionsPerUser} active session${config.maxSessionsPerUser === 1 ? '' : 's'} max).`
        });
        return;
      }

      const session = await sessionManager.createSession({
        ownerId: request.rbiUser.id,
        initialUrl,
        dnsProfile: request.body?.dnsProfile
      });

      const internalSession = sessionManager.getSession(session.id);
      if (internalSession?.viewerToken) {
        response.cookie(session.cookieName, internalSession.viewerToken, viewerCookieOptions(site, session.id));
      }

      response.status(201).json(serializeSiteSession(site, session, request));
    } catch (error) {
      const status = /Docker is required/.test(error.message) ? 503 : isClientConfigurationError(error) ? 400 : 500;
      response.status(status).json({
        error: error.message
      });
    }
  });

  router.get('/sessions', requireSiteAuth, (request, response) => {
    const sessions = sessionManager
      .listSessionsForOwner(request.rbiUser.id)
      .map((session) => serializeSiteSession(site, sessionManager.serializeSession(session), request));

    response.json({
      sessions
    });
  });

  router.get('/sessions/:id', requireSiteAuth, requireOwnedSession, (request, response) => {
    const viewerToken = request.rbiSession.viewerToken;
    if (viewerToken) {
      response.cookie(getCookieName(request.rbiSession.id), viewerToken, viewerCookieOptions(site, request.rbiSession.id));
    }

    response.json(serializeSiteSession(site, sessionManager.serializeSession(request.rbiSession), request));
  });

  router.delete('/sessions/:id', requireSiteAuth, requireOwnedSession, async (request, response) => {
    response.clearCookie(getCookieName(request.rbiSession.id), viewerCookieOptions(site, request.rbiSession.id));
    await sessionManager.destroySession(request.rbiSession.id);
    response.status(204).end();
  });

  router.use('/sessions/:id/browser', createRequireBrowserAccess(site), proxyBrowserHttp);

  return router;
}

function createRequireAuth(site) {
  return (request, response, next) => {
    const authSession = ensureSiteAuthSession(request, response, site);
    if (!authSession) {
      response.status(401).json({
        error: 'Authentication required.'
      });
      return;
    }

    request.rbiSite = site;
    request.rbiAuthSession = authSession;
    request.rbiUser = authSession.user;
    next();
  };
}

function requireOwnedSession(request, response, next) {
  const session = sessionManager.getSessionForOwner(request.params.id, request.rbiUser.id);
  if (!session) {
    response.status(404).json({
      error: 'Session not found.'
    });
    return;
  }

  request.rbiSession = session;
  next();
}

function requireAdmin(request, response, next) {
  if (!request.rbiUser?.isAdmin) {
    response.status(403).json({
      error: 'Admin access required.'
    });
    return;
  }

  next();
}

function createRequireBrowserAccess(site) {
  return (request, response, next) => {
    const authSession = ensureSiteAuthSession(request, response, site);
    if (!authSession) {
      response.status(401).json({
        error: 'Authentication required.'
      });
      return;
    }

    const session = sessionManager.getSessionForOwner(request.params.id, authSession.user.id);
    if (!session) {
      response.status(404).json({
        error: 'Session not found.'
      });
      return;
    }

    const viewerToken = readCookie(request, getCookieName(session.id));
    if (!sessionManager.validateViewerToken(session.id, viewerToken)) {
      response.status(401).json({
        error: 'Invalid session binding.'
      });
      return;
    }

    request.rbiSite = site;
    request.rbiAuthSession = authSession;
    request.rbiUser = authSession.user;
    request.rbiSession = session;
    next();
  };
}

function ensureSiteAuthSession(request, response, site) {
  const authSession = readAuthSession(request, site);
  if (authSession) {
    return authSession;
  }

  if (site.authMode !== 'guest') {
    return null;
  }

  const guestSession = authManager.createGuestSession({
    username: site.guestDisplayName
  });
  response.cookie(site.authCookieName, guestSession.token, authCookieOptions(site));
  return guestSession;
}

function readAuthSession(request, site) {
  const token = readCookie(request, site.authCookieName);
  return authManager.getSession(token);
}

function siteAllowsUser(site, username) {
  if (!site.allowedUsers) {
    return true;
  }

  return site.allowedUsers.has(String(username ?? '').trim());
}

function buildHomePcCapability(user) {
  const username = String(user?.username ?? '').trim();
  const allowedUsers = new Set(config.homePcUsers.map((entry) => String(entry ?? '').trim()).filter(Boolean));
  const allowed = Boolean(username && allowedUsers.has(username));

  return {
    allowed,
    url: allowed ? config.homePcUrl : ''
  };
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

function cookieOptions(path) {
  return {
    httpOnly: true,
    sameSite: 'strict',
    secure: useSecureCookies,
    path
  };
}

function authCookieOptions(site) {
  return cookieOptions(site.path);
}

function viewerCookieOptions(site, sessionId) {
  return cookieOptions(buildSessionViewerBasePath(site, sessionId));
}

function serializeSiteSession(site, session, request) {
  const connectPath = buildSessionConnectPath(site, session.id);
  return withAbsoluteUrls(
    {
      ...session,
      connectPath
    },
    request
  );
}

function withAbsoluteUrls(session, request) {
  const fallbackBase = `${servingScheme}://localhost:${runtimePort}`;
  const baseUrl = config.publicBaseUrl || getRequestBaseUrl(request) || fallbackBase;
  const connectUrl = new URL(session.connectPath, `${baseUrl.replace(/\/$/, '')}/`);

  return {
    ...session,
    connectUrl: connectUrl.toString()
  };
}

function getBrowserRequest(requestUrl, host) {
  if (!requestUrl) {
    return null;
  }

  const url = new URL(requestUrl, `http://${host ?? 'localhost'}`);
  for (const site of sites) {
    const match = url.pathname.match(site.browserPathMatcher);
    if (match) {
      return {
        siteKey: site.key,
        sessionId: match[1]
      };
    }
  }
  return null;
}

function readCookie(request, cookieName) {
  const cookieHeader = request.headers.cookie;
  if (!cookieHeader) {
    return null;
  }

  for (const pair of cookieHeader.split(';')) {
    const [rawName, ...rawValue] = pair.trim().split('=');
    if (rawName === cookieName) {
      return decodeURIComponent(rawValue.join('='));
    }
  }

  return null;
}

function getRequestBaseUrl(request) {
  if (!request) {
    return null;
  }

  const host = request.get('x-forwarded-host') || request.get('host');
  if (!host) {
    return null;
  }

  const protocol = request.get('x-forwarded-proto') || request.protocol || servingScheme;
  return `${protocol}://${host}`;
}

// Cap the in-memory buffer used to rewrite the upstream noVNC index HTML.
// The real index is ~70 KB; refuse to buffer anything pathological.
const VIEWER_HTML_REWRITE_LIMIT = 1024 * 1024;

function proxyBrowserHttp(request, response) {
  const upstreamPath = rewriteBrowserPath(request.originalUrl ?? request.url, request.baseUrl);
  const upstreamTarget = resolveBrowserUpstream(request.rbiSession, upstreamPath);
  const upstreamUrl = new URL(
    upstreamTarget.path,
    `${upstreamTarget.protocol}://${config.listenHost}:${upstreamTarget.port}`
  );
  const client = upstreamTarget.protocol === 'https' ? https : http;
  const headers = filterUpstreamHeaders(request.headers);

  headers.authorization = request.rbiSession.workspaceAuthorization;

  const upstreamRequest = client.request(
    upstreamUrl,
    {
      method: request.method,
      headers,
      rejectUnauthorized: false
    },
    (upstreamResponse) => {
      const responseHeaders = { ...upstreamResponse.headers };

      if (shouldRewriteViewerHtml(upstreamPath, upstreamResponse)) {
        const chunks = [];
        let bufferedBytes = 0;
        let oversize = false;
        upstreamResponse.on('data', (chunk) => {
          if (oversize) return;
          bufferedBytes += chunk.length;
          if (bufferedBytes > VIEWER_HTML_REWRITE_LIMIT) {
            oversize = true;
            // Stop trying to rewrite and just stream what we have plus the rest.
            response.writeHead(upstreamResponse.statusCode ?? 502, responseHeaders);
            for (const earlier of chunks) response.write(earlier);
            response.write(chunk);
            upstreamResponse.pipe(response);
            return;
          }
          chunks.push(chunk);
        });
        upstreamResponse.on('end', () => {
          if (oversize) return;
          const html = Buffer.concat(chunks).toString('utf8');
          const rewritten = decorateViewerHtml(html, request.rbiSession, request.rbiSite);
          delete responseHeaders['content-length'];
          responseHeaders['content-length'] = Buffer.byteLength(rewritten);
          response.writeHead(upstreamResponse.statusCode ?? 502, responseHeaders);
          response.end(rewritten);
        });
        return;
      }

      response.writeHead(upstreamResponse.statusCode ?? 502, responseHeaders);
      upstreamResponse.pipe(response);
    }
  );

  upstreamRequest.on('error', (error) => {
    if (!response.headersSent) {
      response.status(502).json({
        error: 'The browser stream is unavailable.',
        detail: error.message
      });
      return;
    }

    response.destroy(error);
  });

  request.pipe(upstreamRequest);
}

function proxyBrowserWs(request, socket, head) {
  const session = request.rbiSession;
  const upstreamPath = rewriteBrowserPath(request.originalUrl ?? request.url, buildSessionViewerBasePath(request.rbiSite, session.id));
  const upstreamTarget = resolveBrowserUpstream(session, upstreamPath);
  const useTls = upstreamTarget.protocol === 'https';

  const headers = filterUpstreamHeaders(request.headers);
  headers.authorization = session.workspaceAuthorization;
  headers.host = `${config.listenHost}:${upstreamTarget.port}`;

  // Build the upgrade request as raw bytes with canonical header casing.
  // KasmVNC's HTTP parser rejects lowercase header names with a 404.
  const requestLines = [`GET ${upstreamTarget.path} HTTP/1.1`];
  for (const [name, value] of Object.entries(headers)) {
    requestLines.push(`${canonicalizeHeaderName(name)}: ${value}`);
  }
  const requestBytes = requestLines.join('\r\n') + '\r\n\r\n';

  // VNC interactivity needs every keypress/mouse event delivered without
  // Nagle coalescing; keepalive catches silent NAT/firewall drops.
  socket.setNoDelay(true);
  socket.setKeepAlive(true, 30_000);

  const connect = useTls ? tls.connect : net.connect;
  const upstreamSocket = connect(
    {
      host: config.listenHost,
      port: upstreamTarget.port,
      rejectUnauthorized: false,
      ALPNProtocols: ['http/1.1']
    },
    () => {
      upstreamSocket.setNoDelay(true);
      upstreamSocket.setKeepAlive(true, 30_000);
      upstreamSocket.write(requestBytes);
      if (head?.length) upstreamSocket.write(head);
    }
  );

  // Register error/close handlers before piping so an immediate ECONNREFUSED
  // tears both sides down cleanly.
  upstreamSocket.on('error', (error) => {
    console.error('Upstream WebSocket socket error:', error.code, error.message);
    socket.destroy();
  });
  socket.on('error', () => upstreamSocket.destroy());
  socket.on('close', () => upstreamSocket.destroy());
  upstreamSocket.on('close', () => socket.destroy());

  upstreamSocket.pipe(socket);
  socket.pipe(upstreamSocket);
}

// KasmVNC's HTTP server routes any request carrying browser metadata through
// its API auth pipeline. Strip headers injected by browsers/proxies before
// forwarding so upstream sees a plain client.
const UPSTREAM_HEADER_BLOCKLIST = new Set([
  'host',
  'cookie',
  'referer',
  'authorization',
  'x-forwarded-for',
  'x-forwarded-proto',
  'x-forwarded-host',
  'x-real-ip',
  'cf-ray',
  'cf-connecting-ip',
  'cf-visitor',
  'cf-ipcountry',
  'cdn-loop',
  'sec-fetch-dest',
  'sec-fetch-mode',
  'sec-fetch-site',
  'sec-fetch-user',
  'sec-ch-ua',
  'sec-ch-ua-mobile',
  'sec-ch-ua-platform',
  'upgrade-insecure-requests'
]);

function filterUpstreamHeaders(sourceHeaders) {
  const filtered = {};
  for (const [name, value] of Object.entries(sourceHeaders)) {
    if (!UPSTREAM_HEADER_BLOCKLIST.has(name.toLowerCase())) {
      filtered[name] = value;
    }
  }
  return filtered;
}

// KasmVNC's HTTP parser is case-sensitive on header names: it only recognizes
// canonical RFC casing (e.g. "Sec-WebSocket-Key", not "sec-websocket-key").
const HEADER_CANONICAL_OVERRIDES = {
  'sec-websocket-key': 'Sec-WebSocket-Key',
  'sec-websocket-version': 'Sec-WebSocket-Version',
  'sec-websocket-protocol': 'Sec-WebSocket-Protocol',
  'sec-websocket-extensions': 'Sec-WebSocket-Extensions',
  'sec-websocket-accept': 'Sec-WebSocket-Accept',
  'etag': 'ETag',
  'www-authenticate': 'WWW-Authenticate',
  'dnt': 'DNT'
};

function canonicalizeHeaderName(name) {
  const lower = name.toLowerCase();
  if (HEADER_CANONICAL_OVERRIDES[lower]) {
    return HEADER_CANONICAL_OVERRIDES[lower];
  }
  return lower.split('-').map((part) => part.charAt(0).toUpperCase() + part.slice(1)).join('-');
}

function rewriteBrowserPath(urlValue, browserBasePath) {
  if (!urlValue) {
    return '/';
  }

  const prefix = browserBasePath;
  const [pathname, search = ''] = urlValue.split('?', 2);
  const rewrittenPath = pathname.startsWith(prefix) ? pathname.slice(prefix.length) : pathname;
  const normalizedPath = rewrittenPath || '/';

  if (!search) {
    return normalizedPath;
  }

  // Old viewer links may still carry ?token=; KasmVNC misroutes any request
  // with a `token` query string into its API auth pipeline, so strip it.
  const params = new URLSearchParams(search);
  params.delete('token');
  const cleanedSearch = params.toString();
  return cleanedSearch ? `${normalizedPath}?${cleanedSearch}` : normalizedPath;
}

function resolveBrowserUpstream(session, upstreamPath) {
  if (isAudioBrowserPath(upstreamPath)) {
    if (!session.audioHostPort) {
      throw new Error('Audio stream is not available for this session.');
    }

    return {
      protocol: session.streamProtocol,
      port: session.audioHostPort,
      path: stripAudioBrowserPrefix(upstreamPath)
    };
  }

  return {
    protocol: session.streamProtocol,
    port: session.hostPort,
    path: upstreamPath
  };
}

function isAudioBrowserPath(upstreamPath) {
  return upstreamPath === '/_rbi/audio' || upstreamPath.startsWith('/_rbi/audio/');
}

function stripAudioBrowserPrefix(upstreamPath) {
  const strippedPath = upstreamPath.slice('/_rbi/audio'.length);
  return strippedPath || '/';
}

function shouldRewriteViewerHtml(upstreamPath, upstreamResponse) {
  const contentType = String(upstreamResponse.headers['content-type'] ?? '');
  return (upstreamPath === '/' || upstreamPath.startsWith('/?')) && contentType.includes('text/html');
}

function decorateViewerHtml(html, session, site) {
  const bootstrap = buildViewerBootstrapScript(session, site);
  if (html.includes('</head>')) {
    return html.replace('</head>', `<script>${bootstrap}</script></head>`);
  }

  return `<script>${bootstrap}</script>${html}`;
}

function buildViewerBootstrapScript(session, site) {
  const cookiePath = JSON.stringify(buildSessionViewerBasePath(site, session.id));

  return `(() => {
    const cookiePath = ${cookiePath};
    const currentWsProtocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
    const appendPath = (value) => {
      try {
        const url = new URL(value, window.location.href);
        if (url.hostname !== window.location.hostname) {
          return value;
        }
        const isAlternatePort = url.port !== '' && url.port !== window.location.port;
        const proxyPrefix = isAlternatePort ? cookiePath + '/_rbi/audio' : cookiePath;
        if (!url.pathname.startsWith(proxyPrefix)) {
          const nextPath = url.pathname.startsWith('/') ? url.pathname : '/' + url.pathname;
          url.pathname = proxyPrefix + nextPath;
        }
        if (/^wss?:$/i.test(url.protocol)) {
          url.protocol = currentWsProtocol;
          url.host = window.location.host;
        } else if (/^https?:$/i.test(url.protocol)) {
          url.protocol = window.location.protocol;
          url.host = window.location.host;
        }
        if (/^(https?:|wss?:)/i.test(String(value))) {
          return url.toString();
        }
        return url.pathname + url.search + url.hash;
      } catch {
        return value;
      }
    };

    const NativeWebSocket = window.WebSocket;
    const WrappedWebSocket = function(url, protocols) {
      if (protocols === undefined) {
        return new NativeWebSocket(appendPath(url));
      }
      return new NativeWebSocket(appendPath(url), protocols);
    };
    WrappedWebSocket.prototype = NativeWebSocket.prototype;
    if (typeof Object.setPrototypeOf === 'function') {
      Object.setPrototypeOf(WrappedWebSocket, NativeWebSocket);
    }
    WrappedWebSocket.CONNECTING = NativeWebSocket.CONNECTING;
    WrappedWebSocket.OPEN = NativeWebSocket.OPEN;
    WrappedWebSocket.CLOSING = NativeWebSocket.CLOSING;
    WrappedWebSocket.CLOSED = NativeWebSocket.CLOSED;
    window.WebSocket = WrappedWebSocket;

    const nativeFetch = window.fetch?.bind(window);
    if (nativeFetch) {
      window.fetch = (input, init) => {
        if (typeof input === 'string') {
          return nativeFetch(appendPath(input), init);
        }
        if (input instanceof Request) {
          return nativeFetch(new Request(appendPath(input.url), input), init);
        }
        return nativeFetch(input, init);
      };
    }

    const nativeOpen = XMLHttpRequest.prototype.open;
    XMLHttpRequest.prototype.open = function(method, url, ...rest) {
      return nativeOpen.call(this, method, appendPath(url), ...rest);
    };
  })();`;
}

function buildSiteConfigs(currentConfig) {
  if (currentConfig.publicSitePath === currentConfig.privateSitePath) {
    throw new Error('RBI_PUBLIC_SITE_PATH and RBI_PRIVATE_SITE_PATH must be different.');
  }

  return [
    createSiteConfig({
      key: 'public',
      path: currentConfig.publicSitePath,
      title: 'Shared Browser Portal',
      eyebrow: 'Shared Portal',
      heading: 'Open a browser workspace from a shareable guest link.',
      lede:
        'Anyone with this link gets their own temporary Chromium workspace. No app login is required, and each visitor is isolated behind a guest session cookie.',
      authMode: 'guest',
      guestDisplayName: 'Guest',
      authCookieName: `${currentConfig.authCookieName}_public`
    }),
    createSiteConfig({
      key: 'private',
      path: currentConfig.privateSitePath,
      title: 'Private Browser Portal',
      eyebrow: 'Private Portal',
      heading: 'Launch a persistent workspace for your own accounts.',
      lede:
        'This portal is reserved for approved accounts only. Use it for your own saved sessions, admin tools, and anything you do not want mixed into the public share link.',
      authMode: 'login',
      allowedUsers: new Set(currentConfig.privateSiteUsers),
      authCookieName: `${currentConfig.authCookieName}_private`
    })
  ];
}

function createSiteConfig(options) {
  const pathValue = normalizeSitePath(options.path);
  return {
    key: options.key,
    path: pathValue,
    apiBasePath: `${pathValue}/api`,
    authMode: options.authMode === 'guest' ? 'guest' : 'login',
    authCookieName: String(options.authCookieName ?? '').trim(),
    allowedUsers: options.allowedUsers instanceof Set && options.allowedUsers.size ? options.allowedUsers : null,
    guestDisplayName: String(options.guestDisplayName ?? 'Guest').trim() || 'Guest',
    title: String(options.title ?? 'Browser Portal').trim() || 'Browser Portal',
    eyebrow: String(options.eyebrow ?? 'Browser Portal').trim() || 'Browser Portal',
    heading: String(options.heading ?? 'Launch a browser workspace.').trim() || 'Launch a browser workspace.',
    lede: String(options.lede ?? '').trim(),
    shellMatcher: new RegExp(`^${escapeRegex(pathValue)}(?:/(?!api(?:/|$)).*)?$`),
    browserPathMatcher: new RegExp(`^${escapeRegex(pathValue)}/api/sessions/([^/]+)/browser(?:/|$)`)
  };
}

function serializeSite(site) {
  return {
    key: site.key,
    path: site.path,
    apiBasePath: site.apiBasePath,
    authMode: site.authMode
  };
}

function renderAppShell(site) {
  const bootstrap = {
    site: serializeSite(site),
    title: site.title,
    eyebrow: site.eyebrow,
    heading: site.heading,
    lede: site.lede
  };

  return appShellTemplate
    .replace(/<title>.*?<\/title>/i, `<title>${escapeHtml(site.title)}</title>`)
    .replace('</head>', `<script>window.RBI_APP_BOOTSTRAP = ${JSON.stringify(bootstrap)};</script></head>`);
}

function renderLandingPage(activeSites) {
  const cards = activeSites
    .map(
      (site) => `
        <a class="portal-card" href="${site.path}">
          <p class="portal-mode">${escapeHtml(site.eyebrow)}</p>
          <h2>${escapeHtml(site.title)}</h2>
          <p>${escapeHtml(site.lede)}</p>
          <span>${escapeHtml(site.path)}</span>
        </a>
      `
    )
    .join('');

  return `<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Workspace Portals</title>
    <style>
      :root {
        color-scheme: dark;
        --bg: #07111a;
        --panel: rgba(9, 19, 29, 0.84);
        --edge: rgba(255, 255, 255, 0.08);
        --text: #edf4ff;
        --muted: #9bb0c8;
        --brand: #7ce0ff;
        --accent: #ffb86b;
      }
      * {
        box-sizing: border-box;
      }
      body {
        margin: 0;
        min-height: 100vh;
        display: grid;
        place-items: center;
        padding: 32px;
        background:
          radial-gradient(circle at top left, rgba(124, 224, 255, 0.16), transparent 34%),
          radial-gradient(circle at bottom right, rgba(255, 184, 107, 0.16), transparent 24%),
          linear-gradient(160deg, #07111a 0%, #081018 45%, #132335 100%);
        color: var(--text);
        font: 16px/1.6 "Aptos", "Trebuchet MS", sans-serif;
      }
      main {
        width: min(960px, 100%);
      }
      h1 {
        margin: 0 0 12px;
        font: 700 clamp(2.8rem, 6vw, 4.6rem)/0.95 "Rockwell", "Georgia", serif;
      }
      .lede {
        margin: 0 0 28px;
        max-width: 60ch;
        color: var(--muted);
      }
      .portal-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
        gap: 18px;
      }
      .portal-card {
        display: block;
        padding: 22px;
        border: 1px solid var(--edge);
        border-radius: 24px;
        background: var(--panel);
        color: inherit;
        text-decoration: none;
        box-shadow: 0 24px 70px rgba(0, 0, 0, 0.28);
      }
      .portal-card:hover {
        transform: translateY(-2px);
        border-color: rgba(124, 224, 255, 0.34);
      }
      .portal-mode {
        margin: 0 0 10px;
        color: var(--brand);
        text-transform: uppercase;
        letter-spacing: 0.16em;
        font-size: 0.76rem;
      }
      .portal-card h2 {
        margin: 0 0 12px;
      }
      .portal-card p {
        margin: 0 0 14px;
        color: var(--muted);
      }
      .portal-card span {
        color: var(--accent);
        font-weight: 700;
      }
    </style>
  </head>
  <body>
    <main>
      <p class="portal-mode">Workspace Portals</p>
      <h1>Choose which daily link you want to use.</h1>
      <p class="lede">Use the shared portal when you want to hand out a simple guest link. Use the private portal when only your approved local accounts should be able to sign in.</p>
      <section class="portal-grid">${cards}</section>
    </main>
  </body>
</html>`;
}

function buildSessionConnectPath(site, sessionId) {
  return `${buildSessionViewerBasePath(site, sessionId)}/`;
}

function buildSessionViewerBasePath(site, sessionId) {
  return `${site.apiBasePath}/sessions/${sessionId}/browser`;
}

function normalizeSitePath(value) {
  const trimmed = String(value ?? '').trim();
  if (!trimmed || trimmed === '/') {
    return '/';
  }

  return `/${trimmed.replace(/^\/+|\/+$/g, '')}`;
}

function escapeRegex(value) {
  return String(value ?? '').replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

function escapeHtml(value) {
  return String(value ?? '')
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#39;');
}

function onListening() {
  const address = server.address();
  if (address && typeof address !== 'string') {
    runtimePort = address.port;
  }

  console.log(`KasmVNC workspace app listening on ${servingScheme}://${config.host === '0.0.0.0' ? 'localhost' : config.host}:${runtimePort}`);
}

function getFreePort(host) {
  return new Promise((resolve, reject) => {
    const probe = net.createServer();

    probe.unref();
    probe.on('error', reject);
    probe.listen(0, host, () => {
      const address = probe.address();
      if (!address || typeof address === 'string') {
        probe.close(() => reject(new Error('Could not allocate a fallback app port.')));
        return;
      }

      probe.close((error) => {
        if (error) {
          reject(error);
          return;
        }

        resolve(address.port);
      });
    });
  });
}

function parseUsers(value, adminUsers = []) {
  const raw = String(value ?? '').trim();
  if (!raw) {
    return [];
  }

  const adminSet = new Set(adminUsers.map((username) => String(username ?? '').trim()).filter(Boolean));
  const users = [];
  for (const segment of raw.split(',')) {
    const pair = segment.trim();
    if (!pair) {
      continue;
    }

    const separator = pair.indexOf(':');
    if (separator <= 0 || separator === pair.length - 1) {
      console.warn(`Ignoring RBI_USERS entry "${pair}" because it is not in username:password format.`);
      continue;
    }

    const username = pair.slice(0, separator).trim();
    const password = pair.slice(separator + 1);
    if (!username || !password) {
      continue;
    }

    users.push({
      id: username,
      username,
      password,
      isAdmin: adminSet.has(username)
    });
  }

  return users;
}

function parseUsernames(value, fallback = []) {
  const raw = String(value ?? '').trim();
  if (!raw) {
    return Array.isArray(fallback) ? fallback : [];
  }

  return raw
    .split(',')
    .map((entry) => entry.trim())
    .filter(Boolean);
}

function parseBoolish(value) {
  if (value == null || value === '') return null;
  const normalized = String(value).trim().toLowerCase();
  if (normalized === '1' || normalized === 'true' || normalized === 'yes' || normalized === 'on') return true;
  if (normalized === '0' || normalized === 'false' || normalized === 'no' || normalized === 'off') return false;
  return null;
}

function parseBoolean(value, defaultValue) {
  const parsed = parseBoolish(value);
  return parsed === null ? defaultValue : parsed;
}

function isClientConfigurationError(error) {
  return /\b(DNS lab mode|DNS server|Custom DNS mode|Chromium secure DNS mode|DoH template)\b/i.test(error?.message ?? '');
}

function parseTrustProxy(value) {
  if (value == null || value === '') return true;
  const parsed = parseBoolish(value);
  if (parsed !== null) return parsed;
  const normalized = String(value).trim();
  if (/^\d+$/.test(normalized)) return Number(normalized);
  return value;
}

function loadTlsOptions(currentConfig) {
  const keyPath = currentConfig.tlsKeyFile;
  const certPath = currentConfig.tlsCertFile;
  const caPath = currentConfig.tlsCaFile;

  if (!keyPath && !certPath && !caPath) {
    return null;
  }

  if (!keyPath || !certPath) {
    throw new Error('TLS requires both RBI_TLS_KEY_FILE and RBI_TLS_CERT_FILE.');
  }

  const options = {
    key: fs.readFileSync(path.resolve(keyPath)),
    cert: fs.readFileSync(path.resolve(certPath))
  };

  if (caPath) {
    options.ca = fs.readFileSync(path.resolve(caPath));
  }

  return options;
}
