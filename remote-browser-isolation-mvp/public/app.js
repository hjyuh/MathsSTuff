const LAST_SESSION_KEY_PREFIX = 'rbi_last_session_id:';
const bootstrap = normalizeBootstrap(window.RBI_APP_BOOTSTRAP);

const portalEyebrow = document.querySelector('#portal-eyebrow');
const portalTitle = document.querySelector('#portal-title');
const portalLede = document.querySelector('#portal-lede');
const accountLabel = document.querySelector('#account-label');
const loginForm = document.querySelector('#login-form');
const loginButton = document.querySelector('#login-button');
const logoutButton = document.querySelector('#logout-button');
const usernameInput = document.querySelector('#login-username');
const passwordInput = document.querySelector('#login-password');
const authLine = document.querySelector('#auth-line');
const adminTools = document.querySelector('#admin-tools');
const adminToggleButton = document.querySelector('#toggle-admin-credentials');
const adminLine = document.querySelector('#admin-line');
const adminCredentialList = document.querySelector('#admin-credential-list');
const quotaState = document.querySelector('#quota-state');
const sessionPicker = document.querySelector('#session-picker');
const resumeButton = document.querySelector('#resume-session');
const refreshSessionsButton = document.querySelector('#refresh-sessions');
const workspaceChoice = document.querySelector('#workspace-choice');
const chooseKasmButton = document.querySelector('#choose-kasm');
const chooseHomePcButton = document.querySelector('#choose-home-pc');
const homePcPanel = document.querySelector('#home-pc-panel');
const homePcLine = document.querySelector('#home-pc-line');
const openHomePcLink = document.querySelector('#open-home-pc');
const openHomePcKasmButton = document.querySelector('#open-home-pc-kasm');
const dnsLabPanel = document.querySelector('#dns-lab-panel');
const dnsModeSelect = document.querySelector('#dns-mode');
const dnsServersInput = document.querySelector('#dns-servers');
const dohTemplateInput = document.querySelector('#doh-template');
const dnsLabLine = document.querySelector('#dns-lab-line');

const startButton = document.querySelector('#start-session');
const stopButton = document.querySelector('#stop-session');
const openLink = document.querySelector('#open-session');
const statusLine = document.querySelector('#status-line');
const sessionState = document.querySelector('#session-state');
const sessionExpiry = document.querySelector('#session-expiry');
const workerImage = document.querySelector('#worker-image');
const sessionDnsMode = document.querySelector('#session-dns-mode');
const viewerCaption = document.querySelector('#viewer-caption');
const sessionFrame = document.querySelector('#session-frame');
const viewerPlaceholder = document.querySelector('#viewer-placeholder');
const useStepOne = document.querySelector('#use-step-one');
const useStepTwo = document.querySelector('#use-step-two');
const useStepThree = document.querySelector('#use-step-three');
const useStepFour = document.querySelector('#use-step-four');

const state = {
  health: null,
  session: null,
  sessions: [],
  auth: null,
  adminCredentials: [],
  workspaceMode: 'kasm',
  pollTimer: null,
  healthTimer: null
};

init().catch((error) => {
  setStatus(error.message, true);
});

loginForm.addEventListener('submit', async (event) => {
  event.preventDefault();
  await login();
});

logoutButton.addEventListener('click', async () => {
  await logout();
});

adminToggleButton.addEventListener('click', async () => {
  await toggleAdminCredentials();
});

startButton.addEventListener('click', async () => {
  await createSession();
});

stopButton.addEventListener('click', async () => {
  await stopSession();
});

openLink.addEventListener('click', (event) => {
  if (!state.session) {
    event.preventDefault();
    return;
  }

  event.preventDefault();
  openSessionInNewTab(state.session);
});

openHomePcLink.addEventListener('click', (event) => {
  if (!getHomePcUrl()) {
    event.preventDefault();
    setStatus('Home PC access is not configured yet.', true);
    return;
  }

  setStatus('Opened Home PC access in a new tab.', false);
});

openHomePcKasmButton.addEventListener('click', async () => {
  await openHomePcViaKasm();
});

dnsModeSelect.addEventListener('change', () => {
  renderDnsLabControls();
});

dnsServersInput.addEventListener('input', () => {
  renderDnsLabControls();
});

dohTemplateInput.addEventListener('input', () => {
  renderDnsLabControls();
});

resumeButton.addEventListener('click', async () => {
  const id = sessionPicker.value;
  if (!id) {
    return;
  }
  await resumeSessionById(id, {
    announce: true
  });
});

refreshSessionsButton.addEventListener('click', async () => {
  if (!state.auth) {
    return;
  }

  await loadSessionList();
  const resumed = await resumePreferredSession('refresh');
  render();
  if (!resumed) {
    setStatus('Session list refreshed.', false);
  }
});

chooseKasmButton.addEventListener('click', () => {
  state.workspaceMode = 'kasm';
  render();
  setStatus('KasmVNC workspace selected.', false);
});

chooseHomePcButton.addEventListener('click', () => {
  if (!canUseHomePc()) {
    return;
  }

  state.workspaceMode = 'home-pc';
  render();
  setStatus('Home PC access selected.', false);
});

async function init() {
  applyBootstrapCopy();
  await loadHealth();
  await loadAuth();
  if (state.auth) {
    await loadSessionList();
    await resumePreferredSession('startup');
  }
  render();
}

async function loadHealth() {
  const response = await fetch(apiUrl('/health'));
  const health = await readJson(response);
  state.health = health;
  workerImage.textContent = health.image;
  configureDnsLabFromHealth(health);
  const audioMode = health.audioEnabled ? (health.pcmAudioEnabled ? 'PCM high-fidelity audio' : 'compressed audio') : 'audio disabled';
  scheduleHealthRefresh();
  setStatus(
    health.ok
      ? `Workspace image is ready. ${audioMode}. Sessions expire after ${health.ttlMinutes} minutes.`
      : health.warmingImage
        ? 'Preparing the Docker workspace image. First launch after a reset can take a couple of minutes.'
        : (health.imageError || health.error || 'Docker is still starting.'),
    !health.ok && !health.warmingImage
  );
}

async function loadAuth() {
  const response = await fetch(apiUrl('/auth/me'));
  if (response.status === 401) {
    state.auth = null;
    state.workspaceMode = 'kasm';
    resetAdminCredentials();
    setAuthStatus(bootstrap.site.authMode === 'guest' ? 'Preparing guest access.' : 'Signed out. Log in to start browser sessions.', false);
    return;
  }

  const payload = await readJson(response);
  if (!response.ok) {
    state.auth = null;
    state.workspaceMode = 'kasm';
    resetAdminCredentials();
    setAuthStatus(payload.error || 'Could not load authentication state.', true);
    return;
  }

  state.auth = payload;
  if (!canUseHomePc()) {
    state.workspaceMode = 'kasm';
  }
  if (!payload.user?.isAdmin) {
    resetAdminCredentials();
  }
  setAuthStatus(buildSignedInMessage(payload.user), false);
  if (payload.user?.isAdmin && adminCredentialList.hidden) {
    setAdminStatus('Admin tools are ready. Reveal stored account passwords when needed.', false);
  }
}

async function loadSessionList() {
  const response = await fetch(apiUrl('/sessions'));
  if (response.status === 401) {
    await handleAuthExpired();
    return;
  }

  const payload = await readJson(response);
  if (!response.ok) {
    setStatus(payload.error || 'Could not load session list.', true);
    return;
  }

  state.sessions = Array.isArray(payload.sessions) ? payload.sessions : [];
  renderSessionPicker();

  if (state.session && !state.sessions.some((item) => item.id === state.session.id)) {
    clearPollTimer();
    state.session = null;
  }
}

async function toggleAdminCredentials() {
  if (!state.auth?.user?.isAdmin) {
    return;
  }

  if (!adminCredentialList.hidden) {
    adminCredentialList.hidden = true;
    adminToggleButton.textContent = 'Show Passwords';
    setAdminStatus('Admin tools are ready. Reveal stored account passwords when needed.', false);
    return;
  }

  if (state.adminCredentials.length) {
    renderAdminCredentials();
    adminCredentialList.hidden = false;
    adminToggleButton.textContent = 'Hide Passwords';
    setAdminStatus(`Showing ${state.adminCredentials.length} configured account password${state.adminCredentials.length === 1 ? '' : 's'}.`, false);
    return;
  }

  await loadAdminCredentials();
}

async function loadAdminCredentials() {
  if (!state.auth?.user?.isAdmin) {
    return;
  }

  adminToggleButton.disabled = true;
  setAdminStatus('Loading configured account passwords...', false);

  const response = await fetch(apiUrl('/admin/credentials'));
  if (response.status === 401) {
    adminToggleButton.disabled = false;
    await handleAuthExpired();
    return;
  }

  const payload = await readJson(response);
  if (!response.ok) {
    if (response.status === 403) {
      resetAdminCredentials();
    }
    setAdminStatus(payload.error || 'Could not load account passwords.', true);
    adminToggleButton.disabled = false;
    return;
  }

  state.adminCredentials = Array.isArray(payload.users) ? payload.users : [];
  renderAdminCredentials();
  adminCredentialList.hidden = false;
  adminToggleButton.textContent = 'Hide Passwords';
  setAdminStatus(`Showing ${state.adminCredentials.length} configured account password${state.adminCredentials.length === 1 ? '' : 's'}.`, false);
  adminToggleButton.disabled = false;
}

function renderAdminCredentials() {
  adminCredentialList.innerHTML = '';

  if (!state.adminCredentials.length) {
    const emptyState = document.createElement('p');
    emptyState.className = 'credential-empty';
    emptyState.textContent = 'No configured logins are available.';
    adminCredentialList.append(emptyState);
    return;
  }

  const grid = document.createElement('div');
  grid.className = 'credential-grid';

  for (const credential of state.adminCredentials) {
    const card = document.createElement('article');
    card.className = 'credential-card';

    const header = document.createElement('div');
    header.className = 'credential-header';

    const username = document.createElement('p');
    username.className = 'credential-name';
    username.textContent = credential.username;
    header.append(username);

    if (credential.isAdmin) {
      const badge = document.createElement('span');
      badge.className = 'credential-badge';
      badge.textContent = 'Admin';
      header.append(badge);
    }

    const usernameRow = document.createElement('p');
    usernameRow.className = 'credential-row';
    const usernameLabel = document.createElement('span');
    usernameLabel.textContent = 'Username';
    const usernameValue = document.createElement('code');
    usernameValue.textContent = credential.username;
    usernameRow.append(usernameLabel, usernameValue);

    const passwordRow = document.createElement('p');
    passwordRow.className = 'credential-row';
    const passwordLabel = document.createElement('span');
    passwordLabel.textContent = 'Password';
    const passwordValue = document.createElement('code');
    passwordValue.textContent = credential.password;
    passwordRow.append(passwordLabel, passwordValue);

    card.append(header, usernameRow, passwordRow);
    grid.append(card);
  }

  adminCredentialList.append(grid);
}

async function login() {
  loginButton.disabled = true;
  setAuthStatus('Signing in...', false);

  const response = await fetch(apiUrl('/auth/login'), {
    method: 'POST',
    headers: {
      'content-type': 'application/json'
    },
    body: JSON.stringify({
      username: usernameInput.value.trim(),
      password: passwordInput.value
    })
  });

  const payload = await readJson(response);
  if (!response.ok) {
    setAuthStatus(payload.error || 'Login failed.', true);
    loginButton.disabled = false;
    return;
  }

  usernameInput.value = '';
  passwordInput.value = '';

  await loadAuth();
  await loadSessionList();
  const resumed = await resumePreferredSession('login');
  render();
  setStatus(
    resumed
      ? 'Signed in and resumed your most recent session.'
      : 'Authentication successful. You can now launch a workspace.',
    false
  );
  loginButton.disabled = false;
}

async function logout() {
  const currentUserId = state.auth?.user?.id;

  await fetch(apiUrl('/auth/logout'), {
    method: 'POST'
  });

  clearPollTimer();
  state.auth = null;
  state.session = null;
  state.sessions = [];
  state.workspaceMode = 'kasm';
  resetAdminCredentials();
  clearPersistedSessionId(currentUserId);
  renderSessionPicker();
  render();
  setAuthStatus('Signed out. Log in to start browser sessions.', false);
  setStatus('Session ended locally.', false);
}

async function createSession(options = {}) {
  if (!state.auth) {
    setAuthStatus('Log in before creating sessions.', true);
    return null;
  }

  await loadHealth();
  if (!state.health?.ok) {
    setStatus(
      state.health?.warmingImage
        ? 'Still preparing the Docker workspace image. Try again once warmup finishes.'
        : (state.health?.imageError || state.health?.error || 'Docker is not ready yet.'),
      true
    );
    render();
    return null;
  }

  clearPollTimer();
  startButton.disabled = true;
  setStatus(options.statusMessage || 'Starting a new browser worker. This takes a few seconds.', false);
  const slowCreateTimer = window.setTimeout(() => {
    setStatus('Still starting the browser worker. Docker cold starts can take a little longer after a restart.', false);
  }, 12_000);

  const dnsProfileResult = readDnsProfileRequest();
  if (!dnsProfileResult.ok) {
    window.clearTimeout(slowCreateTimer);
    startButton.disabled = false;
    setDnsLabStatus(dnsProfileResult.error, true);
    setStatus(dnsProfileResult.error, true);
    return null;
  }

  const requestBody = {
    initialUrl: options.initialUrl || undefined
  };
  if (dnsProfileResult.value) {
    requestBody.dnsProfile = dnsProfileResult.value;
  }

  const response = await fetch(apiUrl('/sessions'), {
    method: 'POST',
    headers: {
      'content-type': 'application/json'
    },
    body: JSON.stringify(requestBody)
  });

  const payload = await readJson(response);
  if (response.status === 401) {
    window.clearTimeout(slowCreateTimer);
    await handleAuthExpired();
    return null;
  }

  if (!response.ok) {
    window.clearTimeout(slowCreateTimer);
    startButton.disabled = false;
    setStatus(payload.error || 'Failed to start a browser worker.', true);
    return null;
  }

  window.clearTimeout(slowCreateTimer);
  activateSession(payload);
  await refreshAuthSnapshot();
  await loadSessionList();
  render();
  setStatus(options.readyMessage || 'Workspace is ready and attached. Reopening this site will resume it automatically.', false);
  return payload;
}

async function stopSession() {
  if (!state.session) {
    return;
  }

  stopButton.disabled = true;
  const stoppingId = state.session.id;
  const response = await fetch(apiUrl(`/sessions/${stoppingId}`), {
    method: 'DELETE'
  });

  if (response.status === 401) {
    await handleAuthExpired();
    return;
  }

  if (!response.ok && response.status !== 404) {
    const payload = await readJson(response);
    setStatus(payload.error || 'Failed to stop the browser session.', true);
    stopButton.disabled = false;
    return;
  }

  clearPersistedSessionIdIfMatches(stoppingId);
  clearSession('Session stopped.');
  await refreshAuthSnapshot();
  await loadSessionList();
  render();
}

async function resumePreferredSession(reason) {
  if (!state.auth || !state.sessions.length) {
    return false;
  }

  const selectedId = sessionPicker.value;
  const persistedId = getPersistedSessionId();
  const candidates = [persistedId, selectedId, state.sessions[0]?.id].filter(Boolean);
  const targetId = candidates.find((id) => state.sessions.some((item) => item.id === id));
  if (!targetId) {
    return false;
  }

  if (state.session?.id === targetId) {
    return true;
  }

  const announce = reason !== 'startup';
  return resumeSessionById(targetId, {
    announce
  });
}

async function resumeSessionById(id, options = {}) {
  const announce = options.announce ?? false;

  const response = await fetch(apiUrl(`/sessions/${id}`));
  if (response.status === 401) {
    await handleAuthExpired();
    return false;
  }

  if (response.status === 404) {
    clearPersistedSessionIdIfMatches(id);
    await loadSessionList();
    render();
    if (announce) {
      setStatus(`Session ${id} no longer exists.`, true);
    }
    return false;
  }

  const payload = await readJson(response);
  if (!response.ok) {
    if (announce) {
      setStatus(payload.error || 'Failed to resume session.', true);
    }
    return false;
  }

  activateSession(payload);
  await refreshAuthSnapshot();
  await loadSessionList();
  render();
  if (announce) {
    setStatus(`Resumed session ${id}.`, false);
  }
  return true;
}

function activateSession(sessionPayload) {
  state.session = sessionPayload;
  persistSessionId(sessionPayload.id);
  sessionFrame.src = sessionPayload.connectUrl;
  viewerPlaceholder.hidden = true;
  viewerCaption.textContent = `Session ${sessionPayload.id} is live.`;
  startPolling();
}

function openSessionInNewTab(session, options = {}) {
  const connectUrl = session?.connectUrl;
  if (!connectUrl) {
    setStatus('No active session is available to open.', true);
    return;
  }

  const viewerWindow = options.viewerWindow || window.open('about:blank', '_blank');
  if (!viewerWindow) {
    setStatus('Popup blocked. Allow popups for this site, then try again.', true);
    return;
  }

  const title = options.title || `Workspace ${session.id}`;
  const audioUrl = buildSessionAudioUrl(connectUrl);
  const serializedConnectUrl = JSON.stringify(connectUrl);
  const serializedTitle = JSON.stringify(title);
  const serializedAudioUrl = JSON.stringify(audioUrl);
  viewerWindow.document.open();
  viewerWindow.document.write(`<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Workspace</title>
    <style>
      :root {
        color-scheme: dark;
      }
      html, body {
        margin: 0;
        width: 100%;
        height: 100%;
        overflow: hidden;
        background: #030712;
      }
      #session-tab-frame {
        border: 0;
        width: 100vw;
        height: 100vh;
        display: block;
        background: #030712;
      }
      #launch-viewer {
        position: fixed;
        inset: 0;
        display: grid;
        place-items: center;
        background:
          radial-gradient(circle at top, rgba(37, 99, 235, 0.3), transparent 45%),
          #030712;
      }
      #launch-viewer[hidden] {
        display: none;
      }
      #launch-button {
        border: 1px solid rgba(148, 163, 184, 0.35);
        border-radius: 999px;
        padding: 0.9rem 1.4rem;
        background: rgba(15, 23, 42, 0.92);
        color: #e5e7eb;
        font: 600 16px/1.1 system-ui, sans-serif;
        cursor: pointer;
      }
      #launch-button:hover {
        background: rgba(30, 41, 59, 0.98);
      }
      .launch-copy {
        position: fixed;
        left: 50%;
        bottom: 2rem;
        transform: translateX(-50%);
        margin: 0;
        color: rgba(226, 232, 240, 0.88);
        font: 500 0.95rem/1.5 system-ui, sans-serif;
        text-align: center;
      }
    </style>
  </head>
  <body>
    <iframe
      id="session-tab-frame"
      title="Remote browser session"
      loading="eager"
      allow="autoplay; fullscreen; clipboard-read; clipboard-write; speaker-selection"
    ></iframe>
    <div id="launch-viewer">
      <button id="launch-button" type="button">Enter Workspace</button>
      <p class="launch-copy">Click once to enter fullscreen and let browser audio start in this tab.</p>
    </div>
    <script>
      (() => {
        try {
          window.opener = null;
        } catch {}
        document.title = ${serializedTitle};
        const audioUrl = ${serializedAudioUrl};
        const frame = document.getElementById('session-tab-frame');
        const launchPanel = document.getElementById('launch-viewer');
        const launchButton = document.getElementById('launch-button');
        let viewerStarted = false;
        let audioContext = null;
        let audioSocket = null;
        let audioScheduleTime = 0;
        const writeViewerLayoutSettings = () => {
          try {
            localStorage.setItem('resize', 'remote');
            localStorage.setItem('view_clip', 'true');
            localStorage.setItem('quality', '9');
            localStorage.setItem('video_quality', '9');
            localStorage.setItem('dynamic_quality_min', '9');
            localStorage.setItem('dynamic_quality_max', '9');
            localStorage.setItem('jpeg_video_quality', '9');
            localStorage.setItem('webp_video_quality', '9');
            localStorage.setItem('treat_lossless', '9');
            localStorage.setItem('framerate', '60');
            localStorage.setItem('video_scaling', '0');
            localStorage.setItem('max_video_resolution_x', String(Math.max(window.innerWidth, 3840)));
            localStorage.setItem('max_video_resolution_y', String(Math.max(window.innerHeight, 2160)));
          } catch {}
        };
        const startKasmAudio = async () => {
          if (!audioUrl) {
            return;
          }
          if (!audioContext) {
            const AudioContextCtor = window.AudioContext || window.webkitAudioContext;
            if (!AudioContextCtor) {
              return;
            }
            audioContext = new AudioContextCtor({ latencyHint: 'interactive' });
          }
          if (audioContext.state === 'suspended') {
            try {
              await audioContext.resume();
            } catch {}
          }
          if (audioSocket && (audioSocket.readyState === WebSocket.OPEN || audioSocket.readyState === WebSocket.CONNECTING)) {
            return;
          }
          audioSocket = new WebSocket(audioUrl);
          audioSocket.binaryType = 'arraybuffer';
          audioSocket.addEventListener('open', () => {
            audioScheduleTime = audioContext.currentTime + 0.08;
            audioSocket.send(String(Math.round(audioContext.sampleRate)) + ',true');
          });
          audioSocket.addEventListener('message', (event) => {
            if (!(event.data instanceof ArrayBuffer) || event.data.byteLength <= 1 || !audioContext) {
              return;
            }
            const pcm = new Int16Array(event.data);
            const channels = 2;
            const frames = Math.floor(pcm.length / channels);
            if (!frames) {
              return;
            }
            const buffer = audioContext.createBuffer(channels, frames, audioContext.sampleRate);
            const left = buffer.getChannelData(0);
            const right = buffer.getChannelData(1);
            for (let index = 0; index < frames; index += 1) {
              left[index] = pcm[index * channels] / 32768;
              right[index] = pcm[index * channels + 1] / 32768;
            }
            const source = audioContext.createBufferSource();
            source.buffer = buffer;
            source.connect(audioContext.destination);
            const now = audioContext.currentTime;
            if (audioScheduleTime < now + 0.03 || audioScheduleTime > now + 0.75) {
              audioScheduleTime = now + 0.05;
            }
            source.start(audioScheduleTime);
            audioScheduleTime += buffer.duration;
          });
        };
        const applyViewerFit = () => {
          writeViewerLayoutSettings();
          frame?.contentWindow?.postMessage({ action: 'resize', value: 'remote' }, '*');
        };
        const scheduleViewerFit = () => {
          applyViewerFit();
          window.setTimeout(applyViewerFit, 250);
          window.setTimeout(applyViewerFit, 1000);
          window.setTimeout(applyViewerFit, 2500);
        };
        const startViewer = async () => {
          if (viewerStarted) {
            return;
          }
          viewerStarted = true;
          launchPanel.hidden = true;
          writeViewerLayoutSettings();
          startKasmAudio();
          if (document.documentElement.requestFullscreen) {
            try {
              await document.documentElement.requestFullscreen();
            } catch {}
          }
          frame.src = ${serializedConnectUrl};
        };
        writeViewerLayoutSettings();
        if (frame) {
          frame.addEventListener('load', scheduleViewerFit, { once: true });
        }
        launchButton?.addEventListener('click', startViewer, { once: true });
        window.addEventListener('message', (event) => {
          if (event.source !== frame?.contentWindow || !event.data || typeof event.data !== 'object') {
            return;
          }
          if (event.data.action === 'enable_audio') {
            startKasmAudio();
          }
          if (event.data.action === 'noVNC_initialized' || event.data.action === 'connection_state') {
            scheduleViewerFit();
          }
        });
        window.addEventListener('resize', applyViewerFit);
      })();
    </script>
  </body>
</html>`);
  viewerWindow.document.close();
  setStatus(options.statusMessage || `Opened session ${session.id} in a new tab. Click once in that tab to start audio and enter fullscreen.`, false);
}

function buildSessionAudioUrl(connectUrl) {
  if (!connectUrl) {
    return '';
  }

  try {
    const url = new URL(connectUrl);
    url.protocol = url.protocol === 'https:' ? 'wss:' : 'ws:';
    url.pathname = `${url.pathname.replace(/\/+$/g, '')}/_rbi/audio/kasmaudio`;
    url.search = '';
    url.hash = '';
    return url.toString();
  } catch {
    return '';
  }
}

async function openHomePcViaKasm() {
  const homePcUrl = getHomePcUrl();
  if (!homePcUrl) {
    setStatus('Home PC access is not configured yet.', true);
    return;
  }

  if (!state.auth) {
    setAuthStatus('Log in before opening Home PC through Kasm.', true);
    return;
  }

  const viewerWindow = window.open('about:blank', '_blank');
  if (!viewerWindow) {
    setStatus('Popup blocked. Allow popups for this site, then try again.', true);
    return;
  }

  writeLoadingTab(viewerWindow, 'Starting Home PC through Kasm...');

  let session = state.session;
  if (!session && state.sessions.length) {
    const resumed = await resumePreferredSession('home-pc-kasm');
    if (resumed) {
      session = state.session;
    }
  }

  if (!session) {
    session = await createSession({
      initialUrl: homePcUrl,
      statusMessage: 'Starting Kasm with Chrome Remote Desktop. This takes a few seconds.',
      readyMessage: 'Kasm is ready. Chrome Remote Desktop should open inside the workspace.'
    });
  }

  if (!session) {
    try {
      viewerWindow.close();
    } catch {}
    return;
  }

  openSessionInNewTab(session, {
    viewerWindow,
    title: 'Home PC via Kasm',
    statusMessage: 'Opened Home PC through Kasm. Click Enter Workspace in the new tab.'
  });
}

function writeLoadingTab(targetWindow, message) {
  try {
    targetWindow.opener = null;
    targetWindow.document.open();
    targetWindow.document.write(`<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Starting Workspace</title>
    <style>
      :root { color-scheme: dark; }
      body {
        margin: 0;
        min-height: 100vh;
        display: grid;
        place-items: center;
        background: #030712;
        color: #e5e7eb;
        font: 600 16px/1.5 system-ui, sans-serif;
      }
    </style>
  </head>
  <body>${escapeText(message)}</body>
</html>`);
    targetWindow.document.close();
  } catch {}
}

function configureDnsLabFromHealth(health) {
  if (!health?.dnsLabEnabled) {
    return;
  }

  const modes = Array.isArray(health.dnsModes) ? health.dnsModes : [];
  if (modes.length) {
    const selectedBefore = dnsModeSelect.value;
    dnsModeSelect.innerHTML = '';
    for (const mode of modes) {
      const option = document.createElement('option');
      option.value = mode.mode;
      option.textContent = mode.label;
      dnsModeSelect.append(option);
    }

    const defaultMode = health.dnsDefaultProfile?.mode || 'system';
    const selectedStillExists = modes.some((mode) => mode.mode === selectedBefore);
    const defaultExists = modes.some((mode) => mode.mode === defaultMode);
    dnsModeSelect.value = selectedStillExists ? selectedBefore : (defaultExists ? defaultMode : modes[0].mode);
  }

  const defaultProfile = health.dnsDefaultProfile;
  if (defaultProfile?.servers?.length && !dnsServersInput.value) {
    dnsServersInput.value = defaultProfile.servers.join(',');
  }
  if (defaultProfile?.dohTemplate && !dohTemplateInput.value) {
    dohTemplateInput.value = defaultProfile.dohTemplate;
  }
}

function readDnsProfileRequest() {
  if (!state.health?.dnsLabEnabled) {
    return {
      ok: true,
      value: null
    };
  }

  const mode = dnsModeSelect.value || state.health.dnsDefaultProfile?.mode || 'system';
  const dnsServers = dnsServersInput.value.trim();
  const dohTemplate = dohTemplateInput.value.trim();

  if (mode === 'custom-dns' && !dnsServers) {
    return {
      ok: false,
      error: 'Enter at least one custom DNS server IP before starting the session.'
    };
  }

  if (mode === 'browser-doh' && !dohTemplate && !state.health.dnsDefaultProfile?.dohTemplate) {
    return {
      ok: false,
      error: 'Enter a DoH HTTPS template before starting the session.'
    };
  }

  return {
    ok: true,
    value: {
      mode,
      dnsServers: dnsServers || undefined,
      dohTemplate: dohTemplate || undefined
    }
  };
}

function renderDnsLabControls() {
  const enabled = Boolean(state.health?.dnsLabEnabled);
  dnsLabPanel.hidden = !enabled;
  if (!enabled) {
    return;
  }

  const hasSession = Boolean(state.session);
  const mode = dnsModeSelect.value || state.health?.dnsDefaultProfile?.mode || 'system';
  const canEdit = Boolean(state.auth && state.health?.ok && !hasSession);
  const customDnsField = dnsServersInput.closest('.dns-field');
  const dohField = dohTemplateInput.closest('.dns-field');
  const showDnsServers = mode === 'custom-dns' || mode === 'browser-doh';
  const showDohTemplate = mode === 'browser-doh';

  dnsModeSelect.disabled = !canEdit;
  dnsServersInput.disabled = !canEdit || !showDnsServers;
  dohTemplateInput.disabled = !canEdit || !showDohTemplate;
  customDnsField.hidden = !showDnsServers;
  dohField.hidden = !showDohTemplate;

  const validation = readDnsProfileRequest();
  if (!validation.ok) {
    setDnsLabStatus(validation.error, true);
    return;
  }

  const preview = validation.value ? formatDnsProfile(expandDnsProfilePreview(validation.value)) : formatDnsProfile(state.health?.dnsDefaultProfile);
  setDnsLabStatus(`Next session: ${preview}.`, false);
}

function expandDnsProfilePreview(profile) {
  const definition = getDnsModeDefinition(profile.mode);
  const servers = parseList(profile.dnsServers || definition?.servers?.join(',') || '');
  const dohTemplate = profile.dohTemplate || definition?.dohTemplate || '';
  return {
    mode: profile.mode,
    label: definition?.label || profile.mode,
    servers,
    dohTemplate
  };
}

function getDnsModeDefinition(mode) {
  return (state.health?.dnsModes || []).find((item) => item.mode === mode) || null;
}

function formatDnsProfile(profile) {
  if (!profile) {
    return 'Not started';
  }

  const label = profile.label || getDnsModeDefinition(profile.mode)?.label || profile.mode || 'DNS';
  const servers = Array.isArray(profile.servers) ? profile.servers : parseList(profile.servers);
  if (profile.dohTemplate) {
    return `${label} (${formatDohHost(profile.dohTemplate)})`;
  }
  if (servers.length) {
    return `${label} (${servers.join(', ')})`;
  }
  return label;
}

function formatDohHost(value) {
  try {
    return new URL(value).host;
  } catch {
    const match = /^https:\/\/([^/?#{}]+)/i.exec(String(value ?? ''));
    return match?.[1] || 'DoH';
  }
}

function parseList(value) {
  if (Array.isArray(value)) {
    return value.map((entry) => String(entry ?? '').trim()).filter(Boolean);
  }

  return String(value ?? '')
    .split(/[,\s]+/g)
    .map((entry) => entry.trim())
    .filter(Boolean);
}

function render() {
  const hasAuth = Boolean(state.auth);
  const session = state.session;
  const hasSession = Boolean(session);
  const isAdmin = Boolean(state.auth?.user?.isAdmin);
  const isGuest = Boolean(state.auth?.user?.isGuest) || bootstrap.site.authMode === 'guest';
  const maxSessions = Number(state.auth?.maxSessionsPerUser ?? 0);
  const activeSessions = Number(state.auth?.activeSessions ?? 0);
  const hasSavedSessions = state.sessions.length > 0;
  const hasHomePc = canUseHomePc();
  const homePcSelected = hasHomePc && state.workspaceMode === 'home-pc';
  const healthReady = Boolean(state.health?.ok);
  const healthWarming = Boolean(state.health?.warmingImage);

  loginForm.hidden = hasAuth || bootstrap.site.authMode === 'guest';
  logoutButton.hidden = !hasAuth || isGuest;
  adminTools.hidden = !isAdmin;
  adminToggleButton.disabled = !isAdmin;
  workspaceChoice.hidden = !hasHomePc;
  homePcPanel.hidden = !homePcSelected;
  chooseKasmButton.dataset.selected = homePcSelected ? 'false' : 'true';
  chooseHomePcButton.dataset.selected = homePcSelected ? 'true' : 'false';

  startButton.disabled = homePcSelected || hasSession || !healthReady || !hasAuth;
  stopButton.disabled = homePcSelected || !hasSession;
  refreshSessionsButton.disabled = homePcSelected || !hasAuth;
  sessionPicker.disabled = homePcSelected || !hasAuth || !hasSavedSessions;
  resumeButton.disabled = homePcSelected || !hasAuth || !hasSavedSessions || !sessionPicker.value;

  openLink.classList.toggle('disabled', homePcSelected || !hasSession);
  openLink.href = hasSession ? 'about:blank' : '#';
  openHomePcLink.classList.toggle('disabled', !getHomePcUrl());
  openHomePcLink.href = getHomePcUrl() || '#';
  openHomePcKasmButton.disabled = !hasAuth || !getHomePcUrl() || !healthReady;
  homePcLine.textContent = getHomePcUrl()
    ? 'Home PC access is available for this account.'
    : 'Home PC access is enabled for this account, but RBI_HOME_PC_URL is not configured yet.';
  homePcLine.dataset.tone = getHomePcUrl() ? 'ok' : 'error';
  sessionState.textContent = hasSession ? session.state : 'Idle';
  sessionExpiry.textContent = hasSession ? formatDate(session.expiresAt) : 'Not started';
  sessionDnsMode.textContent = hasSession ? formatDnsProfile(session.dnsProfile) : formatDnsProfile(state.health?.dnsDefaultProfile);
  quotaState.textContent = hasAuth
    ? maxSessions > 0
      ? `${activeSessions} / ${maxSessions} active`
      : `${activeSessions} active (no hard cap)`
    : bootstrap.site.authMode === 'guest'
      ? 'Guest access is initializing'
      : 'Sign in to view quota';

  if (!isAdmin) {
    resetAdminCredentials();
  }

  if (!hasSession) {
    viewerCaption.textContent = homePcSelected
      ? 'Home PC selected.'
      : hasAuth
        ? 'No session running.'
        : (bootstrap.site.authMode === 'guest' ? 'Guest access is initializing.' : 'Sign in to launch a session.');
    viewerPlaceholder.hidden = false;
    sessionFrame.removeAttribute('src');
  }

  if (homePcSelected) {
    viewerCaption.textContent = 'Home PC selected.';
    viewerPlaceholder.hidden = false;
    viewerPlaceholder.querySelector('p').textContent = getHomePcUrl()
      ? 'Use the Home PC button to open your remote desktop connection for this Windows machine.'
      : 'Set RBI_HOME_PC_URL to your private remote desktop link, then restart the app.';
    sessionFrame.removeAttribute('src');
  } else {
    viewerPlaceholder.querySelector('p').textContent = healthWarming
      ? 'Docker is still preparing the Chromium workspace image. When warmup finishes, new sessions will start normally.'
      : 'The KasmVNC-backed Chromium workspace will appear here after the container comes online.';
  }

  renderDnsLabControls();
}

function scheduleHealthRefresh() {
  if (state.health?.ok) {
    clearHealthRefreshTimer();
    return;
  }

  if (state.healthTimer) {
    return;
  }

  state.healthTimer = window.setInterval(async () => {
    try {
      await loadHealth();
      render();
    } catch (error) {
      setStatus(error.message, true);
    }
  }, 5_000);
}

function clearHealthRefreshTimer() {
  if (!state.healthTimer) {
    return;
  }

  window.clearInterval(state.healthTimer);
  state.healthTimer = null;
}

function renderSessionPicker() {
  const selectedBefore = sessionPicker.value;
  const fallbackSelected = state.session?.id || getPersistedSessionId() || '';
  const targetSelected = selectedBefore || fallbackSelected;

  sessionPicker.innerHTML = '';

  if (!state.sessions.length) {
    const option = document.createElement('option');
    option.value = '';
    option.textContent = 'No active sessions';
    sessionPicker.append(option);
    sessionPicker.value = '';
    return;
  }

  for (const session of state.sessions) {
    const option = document.createElement('option');
    option.value = session.id;
    option.textContent = `${session.id} | ${session.state} | expires ${formatDate(session.expiresAt)}`;
    sessionPicker.append(option);
  }

  const selectedExists = state.sessions.some((session) => session.id === targetSelected);
  sessionPicker.value = selectedExists ? targetSelected : state.sessions[0].id;
}

function startPolling() {
  clearPollTimer();
  state.pollTimer = setInterval(async () => {
    if (!state.session) {
      clearPollTimer();
      return;
    }

    const response = await fetch(apiUrl(`/sessions/${state.session.id}`));

    if (response.status === 401) {
      await handleAuthExpired();
      return;
    }

    if (response.status === 404) {
      const missingId = state.session.id;
      clearPersistedSessionIdIfMatches(missingId);
      await refreshAuthSnapshot();
      await loadSessionList();
      clearSession('Session expired or was removed.');
      const resumed = await resumePreferredSession('fallback');
      render();
      if (!resumed) {
        setStatus(`Session ${missingId} ended and no resumable sessions remain.`, false);
      }
      return;
    }

    const payload = await readJson(response);
    if (!response.ok) {
      setStatus(payload.error || 'Could not refresh session state.', true);
      return;
    }

    state.session = payload;
    persistSessionId(payload.id);
    await refreshAuthSnapshot();
    await loadSessionList();
    render();
  }, 15_000);
}

function clearPollTimer() {
  if (state.pollTimer) {
    clearInterval(state.pollTimer);
    state.pollTimer = null;
  }
}

function clearSession(message) {
  clearPollTimer();
  state.session = null;
  render();
  setStatus(message, false);
}

async function refreshAuthSnapshot() {
  if (!state.auth) {
    return;
  }

  await loadAuth();
}

async function handleAuthExpired() {
  if (bootstrap.site.authMode === 'guest') {
    clearPollTimer();
    state.session = null;
    state.sessions = [];
    state.auth = null;
    state.workspaceMode = 'kasm';
    resetAdminCredentials();
    renderSessionPicker();
    await loadAuth();
    if (state.auth) {
      await loadSessionList();
      await resumePreferredSession('guest-refresh');
    }
    render();
    setAuthStatus('Guest access refreshed.', false);
    setStatus('Guest session refreshed.', false);
    return;
  }

  const currentUserId = state.auth?.user?.id;

  clearPollTimer();
  state.session = null;
  state.sessions = [];
  state.auth = null;
  state.workspaceMode = 'kasm';
  resetAdminCredentials();
  clearPersistedSessionId(currentUserId);
  renderSessionPicker();
  render();
  setAuthStatus('Your login session expired. Log in again.', true);
  setStatus('Authentication required.', true);
}

function getPersistedSessionId() {
  const userId = state.auth?.user?.id;
  if (!userId) {
    return null;
  }
  return localStorage.getItem(`${LAST_SESSION_KEY_PREFIX}${bootstrap.site.key}:${userId}`);
}

function persistSessionId(sessionId) {
  const userId = state.auth?.user?.id;
  if (!userId || !sessionId) {
    return;
  }
  localStorage.setItem(`${LAST_SESSION_KEY_PREFIX}${bootstrap.site.key}:${userId}`, sessionId);
}

function clearPersistedSessionId(userId = state.auth?.user?.id) {
  if (!userId) {
    return;
  }
  localStorage.removeItem(`${LAST_SESSION_KEY_PREFIX}${bootstrap.site.key}:${userId}`);
}

function clearPersistedSessionIdIfMatches(sessionId) {
  const persisted = getPersistedSessionId();
  if (persisted && persisted === sessionId) {
    clearPersistedSessionId();
  }
}

function setStatus(message, isError) {
  statusLine.textContent = message;
  statusLine.dataset.tone = isError ? 'error' : 'ok';
}

function setAuthStatus(message, isError) {
  authLine.textContent = message;
  authLine.dataset.tone = isError ? 'error' : 'ok';
}

function setAdminStatus(message, isError) {
  adminLine.textContent = message;
  adminLine.dataset.tone = isError ? 'error' : 'ok';
}

function setDnsLabStatus(message, isError) {
  dnsLabLine.textContent = message;
  dnsLabLine.dataset.tone = isError ? 'error' : 'ok';
}

function resetAdminCredentials() {
  state.adminCredentials = [];
  adminCredentialList.innerHTML = '';
  adminCredentialList.hidden = true;
  adminToggleButton.textContent = 'Show Passwords';
  setAdminStatus('Admin tools are ready. Reveal stored account passwords when needed.', false);
}

function formatDate(value) {
  return new Intl.DateTimeFormat(undefined, {
    dateStyle: 'medium',
    timeStyle: 'short'
  }).format(new Date(value));
}

async function readJson(response) {
  const text = await response.text();
  if (!text) {
    return {};
  }

  try {
    return JSON.parse(text);
  } catch {
    return {
      error: text
    };
  }
}

function apiUrl(path) {
  return `${bootstrap.site.apiBasePath}${path}`;
}

function applyBootstrapCopy() {
  document.title = bootstrap.title;
  portalEyebrow.textContent = bootstrap.eyebrow;
  portalTitle.textContent = bootstrap.heading;
  portalLede.textContent = bootstrap.lede;

  if (bootstrap.site.authMode === 'guest') {
    accountLabel.textContent = 'Shared Access';
    useStepOne.textContent = 'Open this link and wait for your guest access to initialize.';
    useStepTwo.textContent = 'Start a session.';
    useStepThree.textContent = 'Wait for the embedded KasmVNC workspace to appear.';
    useStepFour.textContent = 'Use Chromium inside that workspace for browsing, research, or demos. Your guest session stays isolated from other visitors.';
    usernameInput.autocomplete = 'off';
    passwordInput.autocomplete = 'off';
    return;
  }

  accountLabel.textContent = 'Account';
  useStepOne.textContent = 'Sign in with a configured account.';
  useStepTwo.textContent = 'Start a session.';
  useStepThree.textContent = 'Wait for the embedded KasmVNC workspace to appear.';
  useStepFour.textContent = 'Use Chromium inside that workspace to open ChatGPT, Claude, YouTube, or another site and sign in there.';
}

function buildSignedInMessage(user) {
  if (user?.isGuest) {
    return 'Guest access is ready. This shared portal signs visitors in automatically.';
  }

  return `Signed in as ${user.username}${user?.isAdmin ? ' (admin)' : ''}.`;
}

function canUseHomePc() {
  return Boolean(state.auth?.homePc?.allowed);
}

function getHomePcUrl() {
  return state.auth?.homePc?.url || '';
}

function escapeText(value) {
  return String(value ?? '')
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#39;');
}

function normalizeBootstrap(raw) {
  const site = raw?.site ?? {};
  const apiBasePath = typeof site.apiBasePath === 'string' && site.apiBasePath ? site.apiBasePath : '/api';
  return {
    title: raw?.title || 'KasmVNC Browser Workspace MVP',
    eyebrow: raw?.eyebrow || 'KasmVNC Browser Workspace MVP',
    heading: raw?.heading || 'Launch a disposable Chromium workspace from your site.',
    lede:
      raw?.lede ||
      'Each session is a Dockerized Kasm Chromium workspace streamed through your app. The worker stays bound to localhost, and access is bound to your authenticated app session plus a server-issued HTTP-only browser binding cookie.',
    site: {
      key: typeof site.key === 'string' && site.key ? site.key : 'default',
      path: typeof site.path === 'string' && site.path ? site.path : '/',
      apiBasePath,
      authMode: site.authMode === 'guest' ? 'guest' : 'login'
    }
  };
}
