import { createHash, randomBytes, timingSafeEqual } from 'node:crypto';

const DEFAULT_AUTH_TTL_MS = 12 * 60 * 60 * 1000;

export class AuthManager {
  constructor(options = {}) {
    const users = normalizeUsers(options.users);
    if (!users.length) {
      throw new Error('Authentication requires at least one configured user.');
    }

    this.users = new Map(users.map((user) => [user.username, user]));
    this.sessionTtlMs = options.sessionTtlMs ?? DEFAULT_AUTH_TTL_MS;
    this.sessions = new Map();
    this.cleanupTimer = setInterval(() => {
      this.reapExpiredSessions();
    }, 60_000);
    this.cleanupTimer.unref?.();
  }

  authenticate(username, password) {
    const user = this.users.get(String(username ?? ''));
    if (!user) {
      return null;
    }

    if (!secureCompare(user.password, String(password ?? ''))) {
      return null;
    }

    return this.createSession(user);
  }

  createGuestSession(options = {}) {
    const guestId = `guest-${createHexToken(10)}`;
    const guestUsername = String(options.username ?? 'Guest').trim() || 'Guest';
    return this.createSession({
      id: guestId,
      username: guestUsername,
      isAdmin: false,
      isGuest: true
    });
  }

  createSession(user) {
    const token = createHexToken(32);
    const createdAt = new Date();
    const expiresAt = new Date(createdAt.getTime() + this.sessionTtlMs);

    const session = {
      token,
      userId: user.id,
      username: user.username,
      isAdmin: user.isAdmin,
      isGuest: user.isGuest,
      createdAt,
      expiresAt
    };

    this.sessions.set(token, session);
    return serializeAuthSession(session);
  }

  getSession(token) {
    if (!token) {
      return null;
    }

    const session = this.sessions.get(token);
    if (!session) {
      return null;
    }

    if (session.expiresAt.getTime() <= Date.now()) {
      this.sessions.delete(token);
      return null;
    }

    return serializeAuthSession(session);
  }

  revoke(token) {
    if (!token) {
      return false;
    }

    return this.sessions.delete(token);
  }

  shutdown() {
    clearInterval(this.cleanupTimer);
    this.sessions.clear();
  }

  reapExpiredSessions() {
    const now = Date.now();
    for (const [token, session] of this.sessions.entries()) {
      if (session.expiresAt.getTime() <= now) {
        this.sessions.delete(token);
      }
    }
  }
}

function normalizeUsers(users) {
  if (!Array.isArray(users)) {
    return [];
  }

  return users
    .map((user) => ({
      id: String(user?.id ?? user?.username ?? '').trim(),
      username: String(user?.username ?? '').trim(),
      password: String(user?.password ?? ''),
      isAdmin: Boolean(user?.isAdmin),
      isGuest: Boolean(user?.isGuest)
    }))
    .filter((user) => user.id && user.username && user.password);
}

function secureCompare(expected, actual) {
  const expectedHash = createHash('sha256').update(expected, 'utf8').digest();
  const actualHash = createHash('sha256').update(actual, 'utf8').digest();
  return timingSafeEqual(expectedHash, actualHash);
}

function createHexToken(bytes) {
  return randomBytes(bytes).toString('hex');
}

function serializeAuthSession(session) {
  return {
    token: session.token,
    user: {
      id: session.userId,
      username: session.username,
      isAdmin: Boolean(session.isAdmin),
      isGuest: Boolean(session.isGuest)
    },
    createdAt: session.createdAt.toISOString(),
    expiresAt: session.expiresAt.toISOString()
  };
}
