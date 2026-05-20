import http from "node:http";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { WebSocketServer } from "ws";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const publicDir = path.join(__dirname, "public");
const port = Number(process.env.PORT || 4173);

const mimeTypes = new Map([
  [".html", "text/html; charset=utf-8"],
  [".css", "text/css; charset=utf-8"],
  [".js", "text/javascript; charset=utf-8"],
  [".json", "application/json; charset=utf-8"],
  [".png", "image/png"],
  [".svg", "image/svg+xml; charset=utf-8"],
  [".ico", "image/x-icon"]
]);

const server = http.createServer(async (req, res) => {
  const requestUrl = new URL(req.url || "/", `http://${req.headers.host}`);
  let filePath;

  if (requestUrl.pathname.startsWith("/node_modules/three/")) {
    filePath = path.join(__dirname, requestUrl.pathname.slice(1));
  } else {
    const cleanPath = requestUrl.pathname === "/" ? "/index.html" : requestUrl.pathname;
    filePath = path.join(publicDir, cleanPath);
  }

  const resolved = path.resolve(filePath);
  const allowedPublic = resolved.startsWith(path.resolve(publicDir));
  const allowedThree = resolved.startsWith(path.resolve(__dirname, "node_modules", "three"));
  if (!allowedPublic && !allowedThree) {
    res.writeHead(403);
    res.end("Forbidden");
    return;
  }

  try {
    const body = await readFile(resolved);
    res.writeHead(200, {
      "Content-Type": mimeTypes.get(path.extname(resolved)) || "application/octet-stream",
      "Cache-Control": "no-store"
    });
    res.end(body);
  } catch {
    res.writeHead(404);
    res.end("Not found");
  }
});

const wss = new WebSocketServer({ server });
const players = new Map();

const spawns = {
  guard: [
    { x: -1.2, y: 1.65, z: 10.35, yaw: 0 },
    { x: 1.2, y: 1.65, z: 10.35, yaw: 0 }
  ],
  mascot: [
    { x: -7, y: 1.65, z: -12, yaw: 0 },
    { x: 0, y: 1.65, z: -13, yaw: 0 },
    { x: 7, y: 1.65, z: -12, yaw: 0 }
  ],
  spectator: [{ x: 0, y: 1.65, z: 0, yaw: 0 }]
};

const game = {
  phase: "lobby",
  startedAt: 0,
  lastTickAt: 0,
  endsAt: 0,
  durationMs: 180000,
  power: 100,
  doors: {
    left: false,
    right: false
  },
  winner: ""
};

function now() {
  return Date.now();
}

function clamp(value, min, max) {
  return Math.min(max, Math.max(min, value));
}

function spawnFor(role, index = 0) {
  const list = spawns[role] || spawns.spectator;
  return { ...list[index % list.length] };
}

function resetRound() {
  game.phase = "lobby";
  game.startedAt = 0;
  game.lastTickAt = 0;
  game.endsAt = 0;
  game.power = 100;
  game.doors.left = false;
  game.doors.right = false;
  game.winner = "";

  const roleCounts = new Map();
  for (const player of players.values()) {
    player.caught = false;
    const roleIndex = roleCounts.get(player.role) || 0;
    roleCounts.set(player.role, roleIndex + 1);
    const spawn = spawnFor(player.role, roleIndex);
    player.x = spawn.x;
    player.y = spawn.y;
    player.z = spawn.z;
    player.yaw = spawn.yaw;
  }

  broadcastEvent("Round reset. Pick roles, then wait for at least one guard and one mascot.");
}

function maybeStartRound() {
  if (game.phase !== "lobby") return;
  const guards = [...players.values()].filter((player) => player.role === "guard");
  const mascots = [...players.values()].filter((player) => player.role === "mascot");
  if (guards.length > 0 && mascots.length > 0) {
    game.phase = "live";
    game.startedAt = now();
    game.lastTickAt = game.startedAt;
    game.endsAt = game.startedAt + game.durationMs;
    game.power = 100;
    game.doors.left = false;
    game.doors.right = false;
    game.winner = "";
    for (const player of players.values()) player.caught = false;
    broadcastEvent("The night has started.");
  }
}

function finishRound(winner, message) {
  if (game.phase === "ended") return;
  game.phase = "ended";
  game.winner = winner;
  game.lastTickAt = now();
  game.endsAt = now();
  game.doors.left = false;
  game.doors.right = false;
  broadcastEvent(message);
}

function resetIfMatchCannotContinue() {
  if (game.phase !== "live") return;
  const guardCount = [...players.values()].filter((player) => player.role === "guard").length;
  const mascotCount = [...players.values()].filter((player) => player.role === "mascot").length;
  if (players.size === 0 || guardCount === 0 || mascotCount === 0) {
    resetRound();
  }
}

function broadcastEvent(message) {
  broadcast({ type: "event", message, at: now() });
}

function serializeState() {
  return {
    type: "state",
    now: now(),
    game,
    players: [...players.values()].map((player) => ({
      id: player.id,
      name: player.name,
      role: player.role,
      x: player.x,
      y: player.y,
      z: player.z,
      yaw: player.yaw,
      caught: player.caught
    }))
  };
}

function send(ws, data) {
  if (ws.readyState === ws.OPEN) {
    ws.send(JSON.stringify(data));
  }
}

function broadcast(data) {
  const payload = JSON.stringify(data);
  for (const client of wss.clients) {
    if (client.readyState === client.OPEN) client.send(payload);
  }
}

function distance2D(a, b) {
  return Math.hypot(a.x - b.x, a.z - b.z);
}

function checkCaptures() {
  if (game.phase !== "live") return;
  const guards = [...players.values()].filter((player) => player.role === "guard" && !player.caught);
  const mascots = [...players.values()].filter((player) => player.role === "mascot" && !player.caught);

  for (const guard of guards) {
    for (const mascot of mascots) {
      if (distance2D(guard, mascot) < 1.25) {
        guard.caught = true;
        broadcastEvent(`${mascot.name} caught ${guard.name}.`);
      }
    }
  }

  const remainingGuards = [...players.values()].filter((player) => player.role === "guard" && !player.caught);
  if (remainingGuards.length === 0 && guards.length > 0) {
    finishRound("mascots", "Mascots win. The office went dark.");
  }
}

function tickGame() {
  if (game.phase !== "live") return;

  const currentTime = now();
  const deltaMs = currentTime - (game.lastTickAt || currentTime);
  game.lastTickAt = currentTime;
  const closedDoors = Number(game.doors.left) + Number(game.doors.right);
  const drainPerMs = 0.00018 + closedDoors * 0.00021;
  game.power = clamp(game.power - deltaMs * drainPerMs, 0, 100);

  if (game.power <= 0) {
    game.doors.left = false;
    game.doors.right = false;
    finishRound("mascots", "Mascots win. The power failed.");
    return;
  }

  if (currentTime >= game.endsAt) {
    finishRound("guards", "Guards win. Sunrise hit before the mascots got in.");
    return;
  }

  checkCaptures();
}

wss.on("connection", (ws) => {
  const id = crypto.randomUUID();
  const spawn = spawnFor("spectator", players.size);
  const player = {
    id,
    name: `Player ${players.size + 1}`,
    role: "spectator",
    x: spawn.x,
    y: spawn.y,
    z: spawn.z,
    yaw: spawn.yaw,
    caught: false
  };

  players.set(id, player);
  send(ws, { type: "welcome", id, state: serializeState() });
  broadcastEvent(`${player.name} joined.`);

  ws.on("message", (raw) => {
    let message;
    try {
      message = JSON.parse(raw.toString());
    } catch {
      return;
    }

    if (message.type === "join") {
      player.name = String(message.name || player.name).slice(0, 18);
      if (["guard", "mascot", "spectator"].includes(message.role)) {
        player.role = message.role;
        player.caught = false;
        const roleIndex = [...players.values()].filter((other) => other.id !== player.id && other.role === player.role).length;
        const roleSpawn = spawnFor(player.role, roleIndex);
        player.x = roleSpawn.x;
        player.y = roleSpawn.y;
        player.z = roleSpawn.z;
        player.yaw = roleSpawn.yaw;
      }
      broadcastEvent(`${player.name} is now ${player.role}.`);
      maybeStartRound();
      return;
    }

    if (message.type === "move") {
      if (player.caught) return;
      player.x = clamp(Number(message.x) || player.x, -20.5, 20.5);
      player.y = 1.65;
      player.z = clamp(Number(message.z) || player.z, -14.5, 14.5);
      player.yaw = Number(message.yaw) || 0;
      checkCaptures();
      return;
    }

    if (message.type === "control" && player.role === "guard" && game.phase === "live") {
      if ((message.action === "toggleLeftDoor" || message.action === "toggleOfficeDoor") && game.power > 1) {
        game.doors.left = !game.doors.left;
        broadcastEvent(`Left shutter ${game.doors.left ? "closed" : "opened"}.`);
      }
      if (message.action === "toggleRightDoor" && game.power > 1) {
        game.doors.right = !game.doors.right;
        broadcastEvent(`Right shutter ${game.doors.right ? "closed" : "opened"}.`);
      }
      return;
    }

    if (message.type === "reset") {
      resetRound();
      maybeStartRound();
    }
  });

  ws.on("close", () => {
    players.delete(id);
    broadcastEvent(`${player.name} left.`);
    resetIfMatchCannotContinue();
  });
});

setInterval(() => {
  tickGame();
  broadcast(serializeState());
}, 1000 / 15);

server.listen(port, () => {
  console.log(`Night Shift Arena running at http://localhost:${port}`);
});
