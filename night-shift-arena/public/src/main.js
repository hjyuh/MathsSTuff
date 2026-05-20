import * as THREE from "/node_modules/three/build/three.module.js";

const canvas = document.querySelector("#game");
const rolePanel = document.querySelector("#role-panel");
const nameInput = document.querySelector("#name-input");
const guardButton = document.querySelector("#guard-button");
const mascotButton = document.querySelector("#mascot-button");
const rosterList = document.querySelector("#roster-list");
const eventFeed = document.querySelector("#event-feed");
const powerBar = document.querySelector("#power-bar");
const powerText = document.querySelector("#power-text");
const roleText = document.querySelector("#role-text");
const timerText = document.querySelector("#timer-text");
const hintText = document.querySelector("#hint-text");
const leftDoorButton = document.querySelector("#left-door-button");
const rightDoorButton = document.querySelector("#right-door-button");
const cameraButton = document.querySelector("#camera-button");
const resetButton = document.querySelector("#reset-button");
const roundBanner = document.querySelector("#round-banner");
const roundTitle = document.querySelector("#round-title");
const reticle = document.querySelector("#reticle");
const cameraOverlay = document.querySelector("#camera-overlay");
const cameraName = document.querySelector("#camera-name");
const cameraFeed = document.querySelector("#camera-feed");
const cameraTabs = document.querySelectorAll("[data-camera]");

const socket = new WebSocket(`${location.protocol === "https:" ? "wss" : "ws"}://${location.host}`);
const scene = new THREE.Scene();
scene.background = new THREE.Color(0x05070a);
scene.fog = new THREE.FogExp2(0x05070a, 0.045);

const camera = new THREE.PerspectiveCamera(72, window.innerWidth / window.innerHeight, 0.1, 85);
const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, powerPreference: "high-performance" });
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;
renderer.outputColorSpace = THREE.SRGBColorSpace;
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.12;

const playerMeshes = new Map();
const keys = new Set();
const events = [];
const players = new Map();
const reusableVector = new THREE.Vector3();
const remoteTarget = new THREE.Vector3();
const cameraForward = new THREE.Vector3();
const viewModel = new THREE.Group();
const viewModelRefs = {};
const officeDoorMeshes = {};

let myId = "";
let myRole = "spectator";
let gameState = null;
let lastFrame = performance.now();
let yaw = 0;
let pitch = 0;
let position = new THREE.Vector3(0, 1.65, 0);
let velocity = new THREE.Vector3();
let joined = false;
let localMoveAmount = 0;
let cameraMonitorOpen = false;
let activeCamera = "stage";

const staticWalls = [];
const dynamicWalls = [];

buildWorld();
buildViewModel();
wireInput();
animate();

socket.addEventListener("message", (event) => {
  const message = JSON.parse(event.data);
  if (message.type === "welcome") {
    myId = message.id;
    applyState(message.state);
    return;
  }
  if (message.type === "state") {
    applyState(message);
    return;
  }
  if (message.type === "event") {
    pushEvent(message.message);
  }
});

guardButton.addEventListener("click", () => joinAs("guard"));
mascotButton.addEventListener("click", () => joinAs("mascot"));
leftDoorButton.addEventListener("click", () => {
  if (myRole === "guard") {
    send({ type: "control", action: "toggleLeftDoor" });
  }
});
rightDoorButton.addEventListener("click", () => {
  if (myRole === "guard") {
    send({ type: "control", action: "toggleRightDoor" });
  }
});
cameraButton.addEventListener("click", () => toggleCameraMonitor());
cameraTabs.forEach((button) => {
  button.addEventListener("click", () => setActiveCamera(button.dataset.camera));
});
resetButton.addEventListener("click", () => send({ type: "reset" }));

function send(payload) {
  if (socket.readyState === WebSocket.OPEN) {
    socket.send(JSON.stringify(payload));
  }
}

function joinAs(role) {
  joined = true;
  myRole = role;
  rolePanel.classList.add("hidden");
  canvas.requestPointerLock?.();
  send({
    type: "join",
    role,
    name: nameInput.value.trim() || "Player"
  });
}

function toggleCameraMonitor(forceState = !cameraMonitorOpen) {
  if (myRole !== "guard" && forceState) return;
  cameraMonitorOpen = forceState;
  cameraOverlay.classList.toggle("hidden", !cameraMonitorOpen);
  cameraButton.classList.toggle("active", cameraMonitorOpen);
  if (cameraMonitorOpen) {
    setActiveCamera(activeCamera);
  }
}

function setActiveCamera(cameraId) {
  activeCamera = cameraId;
  const labels = {
    stage: ["CAM 01", "STAGE FLOOR"],
    left: ["CAM 02", "LEFT HALL"],
    right: ["CAM 03", "RIGHT HALL"],
    office: ["CAM 04", "SECURITY OFFICE"]
  };
  const [shortName, longName] = labels[cameraId] || labels.stage;
  cameraName.textContent = shortName;
  cameraFeed.dataset.label = longName;
  cameraFeed.style.setProperty("--feed-x", `${30 + Math.random() * 45}%`);
  cameraFeed.style.setProperty("--feed-y", `${34 + Math.random() * 34}%`);
  cameraTabs.forEach((button) => {
    button.classList.toggle("active", button.dataset.camera === cameraId);
  });
}

function buildViewModel() {
  const light = new THREE.PointLight(0xffffff, 0.55, 2.8, 1.7);
  light.position.set(0, -0.3, -0.7);
  camera.add(light);

  const guard = new THREE.Group();
  const guardSleeve = viewMaterial(0x214c70, 0x07131a);
  const guardSkin = viewMaterial(0xc78f67, 0x2b130a);
  const guardMetal = viewMaterial(0x171d20, 0x030506);
  const guardGlow = viewMaterial(0x9fe7ff, 0x2d95bc, 0.9);

  const leftSleeve = viewBox(0.16, 0.42, 0.16, guardSleeve, -0.36, -0.5, -0.75);
  leftSleeve.rotation.set(-0.42, 0.08, -0.24);
  const leftHand = viewBox(0.17, 0.14, 0.18, guardSkin, -0.28, -0.68, -0.95);
  leftHand.rotation.set(-0.32, 0.08, -0.18);
  const rightSleeve = viewBox(0.16, 0.44, 0.16, guardSleeve, 0.38, -0.5, -0.72);
  rightSleeve.rotation.set(-0.55, -0.1, 0.28);
  const rightHand = viewBox(0.17, 0.14, 0.18, guardSkin, 0.28, -0.68, -0.94);
  rightHand.rotation.set(-0.4, -0.08, 0.2);
  const flashlight = new THREE.Mesh(
    new THREE.CylinderGeometry(0.07, 0.09, 0.44, 18),
    guardMetal
  );
  flashlight.position.set(0.31, -0.63, -1.08);
  flashlight.rotation.set(Math.PI / 2 - 0.12, 0.02, 0.08);
  const flashlightLens = new THREE.Mesh(new THREE.CylinderGeometry(0.095, 0.095, 0.04, 18), guardGlow);
  flashlightLens.position.set(0.31, -0.64, -1.31);
  flashlightLens.rotation.x = Math.PI / 2;
  const tablet = viewBox(0.52, 0.34, 0.045, guardMetal, -0.02, -0.75, -0.82);
  tablet.rotation.set(-0.58, 0, 0);
  const tabletScreen = new THREE.Mesh(
    new THREE.PlaneGeometry(0.42, 0.24),
    new THREE.MeshBasicMaterial({ map: createScreenTexture("MAP", "#9fe7ff"), side: THREE.DoubleSide, toneMapped: false })
  );
  tabletScreen.position.set(-0.02, -0.695, -0.94);
  tabletScreen.rotation.x = -0.58;
  guard.add(leftSleeve, leftHand, rightSleeve, rightHand, flashlight, flashlightLens, tablet, tabletScreen);

  const mascot = new THREE.Group();
  const mascotShell = viewMaterial(0x8d402a, 0x2c0b06);
  const mascotMetal = viewMaterial(0x22292c, 0x050607);
  const clawGlow = viewMaterial(0xffa04d, 0x833313, 0.82);
  const clawLeft = buildViewClawHand(-0.34, mascotShell, mascotMetal, clawGlow);
  const clawRight = buildViewClawHand(0.34, mascotShell, mascotMetal, clawGlow);
  mascot.add(clawLeft, clawRight);

  guard.visible = false;
  mascot.visible = false;
  viewModelRefs.guard = { root: guard, leftSleeve, rightSleeve, leftHand, rightHand, tablet, tabletScreen, flashlight };
  viewModelRefs.mascot = { root: mascot, clawLeft, clawRight };
  viewModel.scale.setScalar(0.72);
  viewModel.add(guard, mascot);
  viewModel.visible = false;
  camera.add(viewModel);
}

function buildViewClawHand(x, shell, metal, glow) {
  const group = new THREE.Group();
  group.position.set(x, -0.56, -0.82);
  group.rotation.z = x > 0 ? 0.22 : -0.22;
  const forearm = viewBox(0.18, 0.48, 0.18, shell, 0, 0.02, 0);
  forearm.rotation.x = -0.64;
  const wrist = new THREE.Mesh(new THREE.SphereGeometry(0.11, 14, 10), metal);
  wrist.position.set(0, -0.2, -0.18);
  const palm = viewBox(0.24, 0.18, 0.2, shell, 0, -0.3, -0.28);
  palm.rotation.x = -0.12;
  group.add(forearm, wrist, palm);
  for (let i = 0; i < 3; i += 1) {
    const claw = new THREE.Mesh(new THREE.ConeGeometry(0.035, 0.24, 10), glow);
    claw.position.set((i - 1) * 0.085, -0.35, -0.43);
    claw.rotation.x = Math.PI / 2;
    group.add(claw);
  }
  return group;
}

function viewBox(width, height, depth, meshMaterial, x, y, z) {
  const object = new THREE.Mesh(new THREE.BoxGeometry(width, height, depth), meshMaterial);
  object.position.set(x, y, z);
  object.castShadow = false;
  object.receiveShadow = false;
  object.renderOrder = 20;
  if (object.material) {
    object.material.depthTest = false;
    object.material.depthWrite = false;
  }
  return object;
}

function viewMaterial(color, emissive = 0x000000, emissiveIntensity = 0.18) {
  const vm = new THREE.MeshStandardMaterial({
    color,
    roughness: 0.5,
    metalness: 0.18,
    emissive,
    emissiveIntensity
  });
  vm.depthTest = false;
  vm.depthWrite = false;
  return vm;
}

function buildWorld() {
  const ambient = new THREE.AmbientLight(0x71838a, 0.32);
  scene.add(ambient);

  const moon = new THREE.DirectionalLight(0x8ab8ff, 0.46);
  moon.position.set(-8, 10, 8);
  moon.castShadow = true;
  moon.shadow.mapSize.set(2048, 2048);
  moon.shadow.camera.near = 1;
  moon.shadow.camera.far = 42;
  scene.add(moon);

  const floor = new THREE.Mesh(
    new THREE.PlaneGeometry(44, 32, 22, 16),
    new THREE.MeshStandardMaterial({
      color: 0x151b1e,
      map: createFloorTexture(),
      roughness: 0.78,
      metalness: 0.1
    })
  );
  floor.rotation.x = -Math.PI / 2;
  floor.receiveShadow = true;
  scene.add(floor);

  const grid = new THREE.GridHelper(44, 22, 0x334149, 0x182128);
  grid.position.y = 0.012;
  scene.add(grid);

  addWall(0, -16, 44, 0.7, 0x232b30);
  addWall(0, 16, 44, 0.7, 0x232b30);
  addWall(-22, 0, 0.7, 32, 0x232b30);
  addWall(22, 0, 0.7, 32, 0x232b30);

  addWall(-14, -4, 0.55, 17, 0x1e272c);
  addWall(14, -4, 0.55, 17, 0x1e272c);
  addWall(-7, -7.8, 14, 0.55, 0x1f292f);
  addWall(7, -7.8, 14, 0.55, 0x1f292f);
  addWall(-13, 5.5, 12, 0.55, 0x1b2429);
  addWall(13, 5.5, 12, 0.55, 0x1b2429);
  addWall(-12, 10, 10, 0.55, 0x202a2f);
  addWall(12, 10, 10, 0.55, 0x202a2f);
  addWall(0, 8.8, 7.4, 0.55, 0x273139);

  addProp(-8, -12.6, 8, 1.1, 1.2, 0x5b2d32);
  addProp(0, -12.9, 7, 1.1, 1.2, 0x5b2d32);
  addProp(8, -12.6, 8, 1.1, 1.2, 0x5b2d32);
  addProp(0, 12.8, 5.2, 1.2, 1.2, 0x343023);
  addProp(-17, 4, 2.2, 1.1, 5.2, 0x27383c);
  addProp(17, 4, 2.2, 1.1, 5.2, 0x27383c);

  addSign("STAGE", 0, -15.45, 0xd87c42);
  addSign("OFFICE", 0, 15.45, 0x5fa8d3);
  addAreaLight(-9, 8, 0x5fa8d3, 1.8);
  addAreaLight(9, 8, 0xd87c42, 1.8);
  addAreaLight(0, -10, 0xc64034, 2.4);
  addAreaLight(0, 4, 0x65ba8f, 1.2);
  addOfficeBuildout();

  const flashlight = new THREE.SpotLight(0xf6ead0, 2.2, 18, Math.PI / 7, 0.55, 1.25);
  flashlight.position.set(0, 0, 0);
  flashlight.target.position.set(0, 0, -1);
  camera.add(flashlight);
  camera.add(flashlight.target);
  scene.add(camera);
}

function createFloorTexture() {
  const canvasTexture = document.createElement("canvas");
  canvasTexture.width = 512;
  canvasTexture.height = 512;
  const ctx = canvasTexture.getContext("2d");
  ctx.fillStyle = "#11171a";
  ctx.fillRect(0, 0, canvasTexture.width, canvasTexture.height);

  for (let y = 0; y < 512; y += 64) {
    for (let x = 0; x < 512; x += 64) {
      ctx.fillStyle = (x / 64 + y / 64) % 2 === 0 ? "#151d20" : "#0f1518";
      ctx.fillRect(x, y, 64, 64);
      ctx.fillStyle = "rgba(255,255,255,0.035)";
      ctx.fillRect(x, y, 64, 1);
      ctx.fillRect(x, y, 1, 64);
    }
  }

  for (let i = 0; i < 46; i += 1) {
    ctx.fillStyle = `rgba(0,0,0,${0.08 + Math.random() * 0.1})`;
    ctx.beginPath();
    ctx.ellipse(Math.random() * 512, Math.random() * 512, 12 + Math.random() * 48, 5 + Math.random() * 20, Math.random() * Math.PI, 0, Math.PI * 2);
    ctx.fill();
  }

  const texture = new THREE.CanvasTexture(canvasTexture);
  texture.colorSpace = THREE.SRGBColorSpace;
  texture.wrapS = THREE.RepeatWrapping;
  texture.wrapT = THREE.RepeatWrapping;
  texture.repeat.set(7, 5);
  return texture;
}

function createScreenTexture(label, tint = "#7fd3e7") {
  const screen = document.createElement("canvas");
  screen.width = 512;
  screen.height = 320;
  const ctx = screen.getContext("2d");
  ctx.fillStyle = "#020506";
  ctx.fillRect(0, 0, 512, 320);
  ctx.strokeStyle = "rgba(127, 211, 231, 0.18)";
  for (let x = 0; x < 512; x += 24) {
    ctx.beginPath();
    ctx.moveTo(x, 0);
    ctx.lineTo(x, 320);
    ctx.stroke();
  }
  for (let y = 0; y < 320; y += 18) {
    ctx.beginPath();
    ctx.moveTo(0, y);
    ctx.lineTo(512, y);
    ctx.stroke();
  }
  ctx.fillStyle = "rgba(127, 211, 231, 0.1)";
  ctx.fillRect(34, 42, 190, 86);
  ctx.fillRect(276, 58, 156, 122);
  ctx.fillRect(84, 186, 320, 24);
  ctx.fillStyle = tint;
  ctx.font = "bold 44px system-ui, sans-serif";
  ctx.fillText(label, 32, 286);
  ctx.fillStyle = "rgba(255,255,255,0.5)";
  ctx.font = "bold 18px system-ui, sans-serif";
  ctx.fillText("LIVE", 420, 36);

  const texture = new THREE.CanvasTexture(screen);
  texture.colorSpace = THREE.SRGBColorSpace;
  return texture;
}

function addOfficeBuildout() {
  const wallPanel = material(0x1b2428, 0.7, 0.18);
  const darkMetal = material(0x0b0e10, 0.56, 0.58);
  const trim = material(0x475159, 0.42, 0.55);
  const rubber = material(0x07090a, 0.82, 0.24);
  const deskTop = material(0x493829, 0.58, 0.1);
  const blueGlow = material(0x79d8ef, 0.38, 0.12, 0x1d6f8d, 0.8);
  const amberGlow = material(0xf1a24b, 0.42, 0.16, 0x9a3a0c, 0.65);
  const redGlow = material(0xe35445, 0.44, 0.18, 0x8d1512, 0.7);

  const backPanel = mesh(new THREE.BoxGeometry(8.2, 2.75, 0.12), wallPanel, 0, 1.65, 15.45);
  backPanel.receiveShadow = true;
  scene.add(backPanel);
  for (let x = -3.8; x <= 3.8; x += 1.9) {
    scene.add(mesh(new THREE.BoxGeometry(0.05, 2.7, 0.16), trim, x, 1.64, 15.34));
  }
  scene.add(mesh(new THREE.BoxGeometry(8.4, 0.14, 0.18), trim, 0, 3.02, 15.32));
  scene.add(mesh(new THREE.BoxGeometry(8.4, 0.12, 0.18), trim, 0, 0.3, 15.32));
  addWallDisplay(-2.25, 1.82, 15.22, "CAM 02");
  addWallDisplay(0, 1.82, 15.2, "OFFICE");
  addWallDisplay(2.25, 1.82, 15.22, "CAM 03");
  addFrontOfficeStation();

  addDoorBay("left", -5.7, 12.15, -Math.PI / 2);
  addDoorBay("right", 5.7, 12.15, Math.PI / 2);

  const desk = mesh(new THREE.BoxGeometry(5.9, 0.32, 1.32), deskTop, 0, 0.86, 13.25);
  const deskFront = mesh(new THREE.BoxGeometry(5.95, 0.82, 0.22), material(0x2d241c, 0.66, 0.08), 0, 0.44, 12.57);
  const drawerA = mesh(new THREE.BoxGeometry(1.05, 0.5, 0.12), trim, -2.1, 0.5, 12.43);
  const drawerB = mesh(new THREE.BoxGeometry(1.05, 0.5, 0.12), trim, 2.1, 0.5, 12.43);
  scene.add(desk, deskFront, drawerA, drawerB);
  staticWalls.push({ x: 0, z: 13.05, width: 6.05, depth: 1.55 });

  addMonitor(-1.65, 1.3, 12.47, -0.14, "CAM 01", blueGlow);
  addMonitor(0, 1.36, 12.42, 0, "OFFICE", amberGlow);
  addMonitor(1.65, 1.3, 12.47, 0.14, "CAM 03", blueGlow);

  const keyboard = mesh(new THREE.BoxGeometry(1.6, 0.08, 0.34), rubber, 0, 1.06, 12.62);
  const mouse = mesh(new THREE.BoxGeometry(0.28, 0.07, 0.38), rubber, 1.08, 1.06, 12.62);
  const phone = mesh(new THREE.BoxGeometry(0.48, 0.16, 0.28), darkMetal, -2.65, 1.08, 12.78);
  phone.rotation.y = -0.4;
  scene.add(keyboard, mouse, phone);

  addDeskFan(2.52, 1.42, 12.9);
  addControlBox(-4.75, 1.28, 13.64, "LEFT", redGlow, -Math.PI / 2);
  addControlBox(4.75, 1.28, 13.64, "RIGHT", redGlow, Math.PI / 2);
  addCable(-2.5, 12.8, -1.2, 13.12);
  addCable(1.2, 12.82, 2.4, 13.06);

  addSecurityCamera(-4.2, 14.95, 2.55, -0.58, "OFFICE");
  addSecurityCamera(-9.7, 8.1, 2.65, 0.2, "LEFT");
  addSecurityCamera(9.7, 8.1, 2.65, -0.2, "RIGHT");
  addSecurityCamera(0, -10.2, 2.75, Math.PI, "STAGE");

  const ceilingStrip = new THREE.PointLight(0x9bc8d4, 1.2, 8.5, 1.65);
  ceilingStrip.position.set(0, 2.85, 13.4);
  scene.add(ceilingStrip);
  scene.add(mesh(new THREE.BoxGeometry(4.8, 0.05, 0.12), blueGlow, 0, 2.78, 13.4));

  const warningA = createWarningStrip(-5.2, 11.0, -Math.PI / 2);
  const warningB = createWarningStrip(5.2, 11.0, Math.PI / 2);
  scene.add(warningA, warningB);
}

function addDoorBay(side, x, z, rotationY) {
  const frameMaterial = material(0x323b40, 0.48, 0.62);
  const shutterMaterial = material(0x1c2428, 0.36, 0.68);
  const glowMaterial = material(side === "left" ? 0xd94d42 : 0x5fa8d3, 0.4, 0.12, side === "left" ? 0x7c1815 : 0x18546f, 0.6);

  const frame = new THREE.Group();
  frame.position.set(x, 0, z);
  frame.rotation.y = rotationY;
  frame.add(mesh(new THREE.BoxGeometry(0.18, 2.75, 0.18), frameMaterial, -0.75, 1.45, 0));
  frame.add(mesh(new THREE.BoxGeometry(0.18, 2.75, 0.18), frameMaterial, 0.75, 1.45, 0));
  frame.add(mesh(new THREE.BoxGeometry(1.7, 0.18, 0.2), frameMaterial, 0, 2.76, 0));
  frame.add(mesh(new THREE.BoxGeometry(1.4, 0.04, 0.12), glowMaterial, 0, 2.52, -0.06));
  scene.add(frame);

  const shutter = new THREE.Group();
  shutter.position.set(x, 3.15, z);
  shutter.rotation.y = rotationY;
  const panel = mesh(new THREE.BoxGeometry(1.42, 2.5, 0.16), shutterMaterial, 0, 0, 0);
  shutter.add(panel);
  for (let y = -1.0; y <= 1.0; y += 0.4) {
    shutter.add(mesh(new THREE.BoxGeometry(1.44, 0.045, 0.18), frameMaterial, 0, y, -0.01));
  }
  shutter.userData.openY = 3.15;
  shutter.userData.closedY = 1.48;
  officeDoorMeshes[side] = shutter;
  scene.add(shutter);
}

function addMonitor(x, y, z, rotationY, label) {
  const body = material(0x050708, 0.48, 0.4);
  const stand = material(0x20272b, 0.38, 0.58);
  const group = new THREE.Group();
  group.position.set(x, y, z);
  group.rotation.y = rotationY;
  const monitor = mesh(new THREE.BoxGeometry(1.34, 0.74, 0.12), body, 0, 0.34, 0);
  const screen = new THREE.Mesh(
    new THREE.PlaneGeometry(1.16, 0.56),
    new THREE.MeshBasicMaterial({ map: createScreenTexture(label), side: THREE.DoubleSide, toneMapped: false })
  );
  screen.position.set(0, 0.34, -0.071);
  screen.rotation.y = Math.PI;
  const neck = mesh(new THREE.BoxGeometry(0.12, 0.32, 0.12), stand, 0, -0.19, 0);
  const base = mesh(new THREE.BoxGeometry(0.62, 0.08, 0.42), stand, 0, -0.39, 0.06);
  group.add(monitor, screen, neck, base);
  scene.add(group);
}

function addWallDisplay(x, y, z, label) {
  const frameMaterial = material(0x06090b, 0.46, 0.44);
  const group = new THREE.Group();
  group.position.set(x, y, z);
  const frame = mesh(new THREE.BoxGeometry(1.68, 0.94, 0.1), frameMaterial, 0, 0, 0);
  const screen = new THREE.Mesh(
    new THREE.PlaneGeometry(1.48, 0.74),
    new THREE.MeshBasicMaterial({ map: createScreenTexture(label), side: THREE.DoubleSide, toneMapped: false })
  );
  screen.position.set(0, 0, -0.061);
  screen.rotation.y = Math.PI;
  const statusLight = mesh(
    new THREE.BoxGeometry(0.12, 0.05, 0.035),
    material(0x65ba8f, 0.42, 0.12, 0x145f38, 0.8),
    0.7,
    0.39,
    -0.065
  );
  group.add(frame, screen, statusLight);
  scene.add(group);
}

function addFrontOfficeStation() {
  const frameMaterial = material(0x05080a, 0.48, 0.42);
  const ledgeMaterial = material(0x32271f, 0.58, 0.12);
  const panelMaterial = material(0x182126, 0.62, 0.24);
  const panel = mesh(new THREE.BoxGeometry(6.2, 1.85, 0.08), panelMaterial, 0, 1.62, 9.12);
  scene.add(panel);
  for (let x = -2.1; x <= 2.1; x += 2.1) {
    const group = new THREE.Group();
    group.position.set(x, 1.68, 9.18);
    const frame = mesh(new THREE.BoxGeometry(1.55, 0.86, 0.09), frameMaterial, 0, 0, 0);
    const screen = new THREE.Mesh(
      new THREE.PlaneGeometry(1.35, 0.66),
      new THREE.MeshBasicMaterial({
        map: createScreenTexture(x === 0 ? "DESK" : x < 0 ? "L-HALL" : "R-HALL"),
        side: THREE.DoubleSide,
        toneMapped: false
      })
    );
    screen.position.set(0, 0, 0.052);
    group.add(frame, screen);
    scene.add(group);
  }

  const ledge = mesh(new THREE.BoxGeometry(5.8, 0.22, 0.72), ledgeMaterial, 0, 0.88, 9.65);
  const papers = mesh(new THREE.BoxGeometry(0.72, 0.025, 0.44), material(0xc7c1aa, 0.8, 0.02), -1.8, 1.01, 9.42);
  papers.rotation.y = 0.22;
  const mug = new THREE.Mesh(new THREE.CylinderGeometry(0.09, 0.075, 0.16, 16), material(0x5fa8d3, 0.5, 0.04));
  mug.position.set(2.22, 1.05, 9.43);
  mug.castShadow = true;
  const buttonRail = mesh(new THREE.BoxGeometry(2.2, 0.12, 0.2), frameMaterial, 0, 1.04, 9.36);
  scene.add(ledge, papers, mug, buttonRail);

  for (let i = 0; i < 6; i += 1) {
    const lightColor = i % 2 ? 0xd94d42 : 0x65ba8f;
    scene.add(
      mesh(
        new THREE.BoxGeometry(0.12, 0.06, 0.035),
        material(lightColor, 0.4, 0.12, lightColor, 0.55),
        -0.75 + i * 0.3,
        1.15,
        9.24
      )
    );
  }
}

function addDeskFan(x, y, z) {
  const metal = material(0x2b3338, 0.34, 0.62);
  const ring = new THREE.Mesh(new THREE.TorusGeometry(0.32, 0.025, 8, 28), metal);
  ring.position.set(x, y, z);
  ring.rotation.y = Math.PI;
  ring.castShadow = true;
  scene.add(ring);
  for (let i = 0; i < 3; i += 1) {
    const blade = mesh(new THREE.BoxGeometry(0.1, 0.04, 0.42), metal, x, y, z);
    blade.rotation.z = (i / 3) * Math.PI * 2 + 0.4;
    blade.rotation.y = Math.PI / 2;
    scene.add(blade);
  }
  scene.add(mesh(new THREE.BoxGeometry(0.1, 0.45, 0.1), metal, x, y - 0.34, z + 0.05));
}

function addControlBox(x, y, z, label, lightMaterial, rotationY) {
  const group = new THREE.Group();
  group.position.set(x, y, z);
  group.rotation.y = rotationY;
  const box = mesh(new THREE.BoxGeometry(0.54, 0.7, 0.18), material(0x161d20, 0.52, 0.46), 0, 0, 0);
  const lightA = mesh(new THREE.BoxGeometry(0.16, 0.16, 0.035), lightMaterial, -0.13, 0.1, -0.105);
  const lightB = mesh(new THREE.BoxGeometry(0.16, 0.16, 0.035), material(0x65ba8f, 0.42, 0.12, 0x145f38, 0.45), 0.13, 0.1, -0.105);
  const labelPlane = new THREE.Mesh(
    new THREE.PlaneGeometry(0.42, 0.16),
    new THREE.MeshBasicMaterial({ map: createSmallLabel(label), transparent: true, toneMapped: false })
  );
  labelPlane.position.set(0, -0.19, -0.102);
  group.add(box, lightA, lightB, labelPlane);
  scene.add(group);
}

function createSmallLabel(text) {
  const label = document.createElement("canvas");
  label.width = 256;
  label.height = 96;
  const ctx = label.getContext("2d");
  ctx.clearRect(0, 0, 256, 96);
  ctx.fillStyle = "rgba(8,12,14,0.9)";
  ctx.fillRect(0, 0, 256, 96);
  ctx.fillStyle = "#dbe7e4";
  ctx.font = "bold 44px system-ui, sans-serif";
  ctx.textAlign = "center";
  ctx.textBaseline = "middle";
  ctx.fillText(text, 128, 52);
  const texture = new THREE.CanvasTexture(label);
  texture.colorSpace = THREE.SRGBColorSpace;
  return texture;
}

function addSecurityCamera(x, z, y, yawAngle, label) {
  const group = new THREE.Group();
  group.position.set(x, y, z);
  group.rotation.y = yawAngle;
  const casing = material(0x11171a, 0.46, 0.48);
  const lens = material(0x74c9d8, 0.28, 0.22, 0x174e65, 0.5);
  const body = mesh(new THREE.BoxGeometry(0.46, 0.24, 0.32), casing, 0, 0, 0);
  const barrel = mesh(new THREE.CylinderGeometry(0.1, 0.12, 0.26, 16), lens, 0, 0, -0.26);
  barrel.rotation.x = Math.PI / 2;
  const arm = mesh(new THREE.BoxGeometry(0.08, 0.08, 0.34), casing, 0, 0.05, 0.3);
  const tag = new THREE.Mesh(
    new THREE.PlaneGeometry(0.56, 0.18),
    new THREE.MeshBasicMaterial({ map: createSmallLabel(label), transparent: true, toneMapped: false })
  );
  tag.position.set(0, -0.28, -0.1);
  group.add(body, barrel, arm, tag);
  scene.add(group);
}

function addCable(x1, z1, x2, z2) {
  const curve = new THREE.CatmullRomCurve3([
    new THREE.Vector3(x1, 1.08, z1),
    new THREE.Vector3((x1 + x2) / 2, 0.98, (z1 + z2) / 2 + 0.2),
    new THREE.Vector3(x2, 1.08, z2)
  ]);
  const cable = new THREE.Mesh(
    new THREE.TubeGeometry(curve, 18, 0.018, 8, false),
    material(0x050607, 0.78, 0.28)
  );
  cable.castShadow = true;
  scene.add(cable);
}

function createWarningStrip(x, z, rotationY) {
  const canvasTexture = document.createElement("canvas");
  canvasTexture.width = 512;
  canvasTexture.height = 128;
  const ctx = canvasTexture.getContext("2d");
  ctx.fillStyle = "#0a0a0a";
  ctx.fillRect(0, 0, 512, 128);
  ctx.fillStyle = "#d89038";
  for (let xPos = -128; xPos < 640; xPos += 96) {
    ctx.save();
    ctx.translate(xPos, 64);
    ctx.rotate(-Math.PI / 5);
    ctx.fillRect(-20, -90, 42, 180);
    ctx.restore();
  }
  const texture = new THREE.CanvasTexture(canvasTexture);
  texture.colorSpace = THREE.SRGBColorSpace;
  const strip = new THREE.Mesh(
    new THREE.PlaneGeometry(1.5, 0.38),
    new THREE.MeshBasicMaterial({ map: texture, toneMapped: false })
  );
  strip.position.set(x, 0.28, z);
  strip.rotation.x = -Math.PI / 2;
  strip.rotation.z = rotationY;
  return strip;
}

function addWall(x, z, width, depth, color) {
  const wall = new THREE.Mesh(
    new THREE.BoxGeometry(width, 3.2, depth),
    new THREE.MeshStandardMaterial({ color, roughness: 0.74, metalness: 0.05 })
  );
  wall.position.set(x, 1.6, z);
  wall.castShadow = true;
  wall.receiveShadow = true;
  scene.add(wall);
  staticWalls.push({ x, z, width, depth });
  return wall;
}

function addProp(x, z, width, height, depth, color) {
  const prop = new THREE.Mesh(
    new THREE.BoxGeometry(width, height, depth),
    new THREE.MeshStandardMaterial({ color, roughness: 0.66, metalness: 0.18 })
  );
  prop.position.set(x, height / 2, z);
  prop.castShadow = true;
  prop.receiveShadow = true;
  scene.add(prop);
  staticWalls.push({ x, z, width, depth });
}

function addAreaLight(x, z, color, intensity) {
  const light = new THREE.PointLight(color, intensity, 10, 1.9);
  light.position.set(x, 2.6, z);
  scene.add(light);

  const bulb = new THREE.Mesh(
    new THREE.SphereGeometry(0.18, 14, 14),
    new THREE.MeshBasicMaterial({ color })
  );
  bulb.position.copy(light.position);
  scene.add(bulb);
}

function addSign(text, x, z, color) {
  const group = new THREE.Group();
  const back = new THREE.Mesh(
    new THREE.BoxGeometry(5.5, 1.2, 0.12),
    new THREE.MeshStandardMaterial({ color: 0x101316, roughness: 0.5 })
  );
  group.add(back);

  const loaderCanvas = document.createElement("canvas");
  loaderCanvas.width = 512;
  loaderCanvas.height = 128;
  const ctx = loaderCanvas.getContext("2d");
  ctx.fillStyle = "#101316";
  ctx.fillRect(0, 0, 512, 128);
  ctx.fillStyle = `#${color.toString(16).padStart(6, "0")}`;
  ctx.font = "bold 54px system-ui, sans-serif";
  ctx.textAlign = "center";
  ctx.textBaseline = "middle";
  ctx.fillText(text, 256, 68);
  const texture = new THREE.CanvasTexture(loaderCanvas);
  const sign = new THREE.Mesh(
    new THREE.PlaneGeometry(5.2, 1),
    new THREE.MeshBasicMaterial({ map: texture })
  );
  sign.position.z = 0.071;
  group.add(sign);
  group.position.set(x, 2.2, z);
  if (z > 0) group.rotation.y = Math.PI;
  scene.add(group);
}

function wireInput() {
  window.addEventListener("resize", () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
  });

  window.addEventListener("keydown", (event) => {
    keys.add(event.code);
    if (event.code === "KeyQ" && myRole === "guard") {
      send({ type: "control", action: "toggleLeftDoor" });
    }
    if (event.code === "KeyE" && myRole === "guard") {
      send({ type: "control", action: "toggleRightDoor" });
    }
    if (event.code === "KeyC" && myRole === "guard") {
      toggleCameraMonitor();
    }
    if (event.code === "Digit1") {
      setActiveCamera("stage");
    }
    if (event.code === "Digit2") {
      setActiveCamera("left");
    }
    if (event.code === "Digit3") {
      setActiveCamera("right");
    }
    if (event.code === "Digit4") {
      setActiveCamera("office");
    }
    if (event.code === "Escape") {
      if (cameraMonitorOpen) {
        toggleCameraMonitor(false);
        return;
      }
      document.exitPointerLock?.();
    }
  });

  window.addEventListener("keyup", (event) => keys.delete(event.code));

  canvas.addEventListener("click", () => {
    if (joined) canvas.requestPointerLock?.();
  });

  window.addEventListener("mousemove", (event) => {
    if (document.pointerLockElement !== canvas) return;
    yaw -= event.movementX * 0.0023;
    pitch -= event.movementY * 0.0023;
    pitch = Math.max(-1.15, Math.min(1.15, pitch));
  });
}

function applyState(state) {
  gameState = state.game;
  players.clear();
  for (const player of state.players) {
    players.set(player.id, player);
    if (player.id === myId) {
      myRole = player.role;
      if (!joined && player.role !== "spectator") {
        rolePanel.classList.add("hidden");
      }
      if (Math.abs(position.x - player.x) > 5 || Math.abs(position.z - player.z) > 5) {
        position.set(player.x, player.y, player.z);
        yaw = player.yaw;
      }
    }
  }
  syncMeshes();
  updateUi(state.now);
}

function syncMeshes() {
  const seen = new Set();
  for (const player of players.values()) {
    if (player.role === "spectator" || player.id === myId) continue;
    seen.add(player.id);
    let mesh = playerMeshes.get(player.id);
    let isNewMesh = false;
    if (!mesh || mesh.userData.modelRole !== player.role) {
      if (mesh) scene.remove(mesh);
      mesh = createPlayerRig(player.role);
      playerMeshes.set(player.id, mesh);
      scene.add(mesh);
      isNewMesh = true;
    }

    const targetX = player.id === myId ? position.x : player.x;
    const targetZ = player.id === myId ? position.z : player.z;
    if (isNewMesh) {
      mesh.position.set(targetX, 0, targetZ);
      mesh.rotation.y = player.id === myId ? yaw : player.yaw;
      mesh.userData.lastNetX = targetX;
      mesh.userData.lastNetZ = targetZ;
    }
    const lastNetAt = mesh.userData.lastNetAt || performance.now();
    const netDt = Math.max(0.05, (performance.now() - lastNetAt) / 1000);
    const netDistance = Math.hypot(targetX - mesh.userData.lastNetX, targetZ - mesh.userData.lastNetZ);

    mesh.userData.target.set(targetX, 0, targetZ);
    mesh.userData.targetYaw = player.id === myId ? yaw : player.yaw;
    mesh.userData.moveAmount =
      player.id === myId ? localMoveAmount : THREE.MathUtils.clamp(netDistance / netDt / 4.6, 0, 1.3);
    mesh.userData.lastNetX = targetX;
    mesh.userData.lastNetZ = targetZ;
    mesh.userData.lastNetAt = performance.now();
    mesh.visible = !player.caught;
  }

  for (const [id, mesh] of playerMeshes) {
    if (!seen.has(id)) {
      scene.remove(mesh);
      playerMeshes.delete(id);
    }
  }
}

function createPlayerRig(role) {
  const isGuard = role === "guard";
  const group = new THREE.Group();
  group.userData.modelRole = role;
  group.userData.target = new THREE.Vector3();
  group.userData.targetYaw = 0;
  group.userData.lastNetX = 0;
  group.userData.lastNetZ = 0;
  group.userData.lastNetAt = performance.now();
  group.userData.moveAmount = 0;
  group.userData.animTime = Math.random() * 10;
  group.userData.rig = isGuard ? buildGuardRig(group) : buildMascotRig(group);
  return group;
}

function buildGuardRig(root) {
  const cloth = material(0x2d5f87, 0.72, 0.08);
  const vest = material(0x17272f, 0.88, 0.12);
  const skin = material(0xc78f67, 0.58, 0.02);
  const dark = material(0x0c1114, 0.78, 0.1);
  const glow = material(0x92d4ff, 0.38, 0.12, 0x1e6b96, 0.28);
  const boot = material(0x111315, 0.7, 0.22);

  const torso = mesh(new THREE.BoxGeometry(0.64, 0.78, 0.34), vest, 0, 1.24, 0);
  const chestStripe = mesh(new THREE.BoxGeometry(0.68, 0.08, 0.035), glow, 0, 1.35, -0.19);
  root.add(torso, chestStripe);

  const headPivot = new THREE.Group();
  headPivot.position.set(0, 1.78, 0);
  root.add(headPivot);
  const neck = mesh(new THREE.CylinderGeometry(0.13, 0.16, 0.16, 12), skin, 0, -0.18, 0);
  const head = mesh(new THREE.BoxGeometry(0.44, 0.42, 0.42), skin, 0, 0.05, -0.01);
  const cap = mesh(new THREE.BoxGeometry(0.5, 0.14, 0.48), dark, 0, 0.34, 0);
  const brim = mesh(new THREE.BoxGeometry(0.42, 0.045, 0.24), dark, 0, 0.28, -0.31);
  headPivot.add(neck, head, cap, brim);

  const visor = mesh(new THREE.BoxGeometry(0.26, 0.045, 0.04), glow, 0, 0.11, -0.235);
  headPivot.add(visor);

  const leftArm = buildLimb({
    material: cloth,
    jointMaterial: dark,
    endMaterial: skin,
    upper: [0.16, 0.44, 0.16],
    lower: [0.14, 0.42, 0.14],
    end: [0.18, 0.16, 0.16],
    pivot: [-0.48, 1.52, 0],
    side: -1
  });
  const rightArm = buildLimb({
    material: cloth,
    jointMaterial: dark,
    endMaterial: skin,
    upper: [0.16, 0.44, 0.16],
    lower: [0.14, 0.42, 0.14],
    end: [0.18, 0.16, 0.16],
    pivot: [0.48, 1.52, 0],
    side: 1
  });
  root.add(leftArm.root, rightArm.root);

  const flashlight = new THREE.Group();
  flashlight.position.set(0.02, -0.43, -0.03);
  flashlight.rotation.x = Math.PI / 2;
  flashlight.add(mesh(new THREE.CylinderGeometry(0.07, 0.09, 0.36, 14), dark, 0, 0, 0));
  flashlight.add(mesh(new THREE.CylinderGeometry(0.095, 0.095, 0.045, 14), glow, 0, 0.2, 0));
  rightArm.lower.add(flashlight);

  const leftLeg = buildLimb({
    material: cloth,
    jointMaterial: dark,
    endMaterial: boot,
    upper: [0.18, 0.48, 0.18],
    lower: [0.16, 0.46, 0.16],
    end: [0.22, 0.14, 0.32],
    pivot: [-0.2, 0.85, 0],
    side: -1,
    footForward: true
  });
  const rightLeg = buildLimb({
    material: cloth,
    jointMaterial: dark,
    endMaterial: boot,
    upper: [0.18, 0.48, 0.18],
    lower: [0.16, 0.46, 0.16],
    end: [0.22, 0.14, 0.32],
    pivot: [0.2, 0.85, 0],
    side: 1,
    footForward: true
  });
  root.add(leftLeg.root, rightLeg.root);

  const shadow = new THREE.Mesh(
    new THREE.CircleGeometry(0.62, 24),
    new THREE.MeshBasicMaterial({ color: 0x000000, transparent: true, opacity: 0.34, depthWrite: false })
  );
  shadow.rotation.x = -Math.PI / 2;
  shadow.position.y = 0.018;
  root.add(shadow);

  return {
    type: "guard",
    torso,
    headPivot,
    leftArm,
    rightArm,
    leftLeg,
    rightLeg,
    baseY: 0
  };
}

function buildMascotRig(root) {
  const shell = material(0x8d402a, 0.5, 0.5);
  const panels = material(0xd17842, 0.46, 0.42);
  const metal = material(0x3a4143, 0.34, 0.72);
  const dark = material(0x0b0d0e, 0.64, 0.45);
  const glow = material(0xffb25f, 0.3, 0.22, 0xff6f1f, 0.82);

  const torso = mesh(new THREE.BoxGeometry(0.9, 1.08, 0.48), shell, 0, 1.22, 0);
  const belly = mesh(new THREE.BoxGeometry(0.58, 0.42, 0.05), panels, 0, 1.13, -0.27);
  const spine = mesh(new THREE.BoxGeometry(0.18, 1.15, 0.18), metal, 0, 1.18, 0.31);
  root.add(torso, belly, spine);

  const headPivot = new THREE.Group();
  headPivot.position.set(0, 1.95, 0);
  root.add(headPivot);
  const head = mesh(new THREE.BoxGeometry(0.82, 0.58, 0.58), shell, 0, 0.02, 0);
  const snout = mesh(new THREE.BoxGeometry(0.42, 0.2, 0.28), panels, 0, -0.06, -0.42);
  const jaw = mesh(new THREE.BoxGeometry(0.48, 0.1, 0.3), dark, 0, -0.23, -0.4);
  const eyeA = mesh(new THREE.BoxGeometry(0.12, 0.08, 0.045), glow, -0.18, 0.08, -0.315);
  const eyeB = mesh(new THREE.BoxGeometry(0.12, 0.08, 0.045), glow, 0.18, 0.08, -0.315);
  const earA = mesh(new THREE.BoxGeometry(0.22, 0.32, 0.18), shell, -0.28, 0.43, 0.02);
  const earB = mesh(new THREE.BoxGeometry(0.22, 0.32, 0.18), shell, 0.28, 0.43, 0.02);
  headPivot.add(head, snout, jaw, eyeA, eyeB, earA, earB);

  const leftArm = buildLimb({
    material: shell,
    jointMaterial: metal,
    endMaterial: dark,
    upper: [0.22, 0.5, 0.22],
    lower: [0.19, 0.48, 0.19],
    end: [0.26, 0.22, 0.2],
    pivot: [-0.64, 1.55, 0],
    side: -1
  });
  const rightArm = buildLimb({
    material: shell,
    jointMaterial: metal,
    endMaterial: dark,
    upper: [0.22, 0.5, 0.22],
    lower: [0.19, 0.48, 0.19],
    end: [0.26, 0.22, 0.2],
    pivot: [0.64, 1.55, 0],
    side: 1
  });
  root.add(leftArm.root, rightArm.root);

  addClaws(leftArm.lower, -1, glow);
  addClaws(rightArm.lower, 1, glow);

  const leftLeg = buildLimb({
    material: shell,
    jointMaterial: metal,
    endMaterial: dark,
    upper: [0.24, 0.5, 0.24],
    lower: [0.21, 0.46, 0.21],
    end: [0.34, 0.16, 0.42],
    pivot: [-0.28, 0.82, 0],
    side: -1,
    footForward: true
  });
  const rightLeg = buildLimb({
    material: shell,
    jointMaterial: metal,
    endMaterial: dark,
    upper: [0.24, 0.5, 0.24],
    lower: [0.21, 0.46, 0.21],
    end: [0.34, 0.16, 0.42],
    pivot: [0.28, 0.82, 0],
    side: 1,
    footForward: true
  });
  root.add(leftLeg.root, rightLeg.root);

  const antenna = new THREE.Group();
  antenna.position.set(0, 0.42, 0.16);
  antenna.add(mesh(new THREE.CylinderGeometry(0.025, 0.025, 0.42, 8), metal, 0, 0.2, 0));
  antenna.add(mesh(new THREE.SphereGeometry(0.08, 12, 12), glow, 0, 0.44, 0));
  headPivot.add(antenna);

  const shadow = new THREE.Mesh(
    new THREE.CircleGeometry(0.78, 24),
    new THREE.MeshBasicMaterial({ color: 0x000000, transparent: true, opacity: 0.42, depthWrite: false })
  );
  shadow.rotation.x = -Math.PI / 2;
  shadow.position.y = 0.018;
  root.add(shadow);

  return {
    type: "mascot",
    torso,
    headPivot,
    jaw,
    leftArm,
    rightArm,
    leftLeg,
    rightLeg,
    baseY: 0
  };
}

function buildLimb({ material, jointMaterial, endMaterial, upper, lower, end, pivot, side, footForward = false }) {
  const root = new THREE.Group();
  root.position.set(...pivot);

  const upperMesh = mesh(new THREE.BoxGeometry(...upper), material, 0, -upper[1] / 2, 0);
  const elbow = mesh(new THREE.SphereGeometry(Math.max(upper[0], upper[2]) * 0.58, 12, 8), jointMaterial, 0, -upper[1], 0);
  const lowerPivot = new THREE.Group();
  lowerPivot.position.set(0, -upper[1], 0);
  const lowerMesh = mesh(new THREE.BoxGeometry(...lower), material, 0, -lower[1] / 2, 0);
  const endMesh = mesh(
    new THREE.BoxGeometry(...end),
    endMaterial,
    0,
    -lower[1] - end[1] / 2,
    footForward ? -0.08 : 0
  );
  if (!footForward) {
    endMesh.rotation.z = side * 0.12;
  }

  lowerPivot.add(lowerMesh, endMesh);
  root.add(upperMesh, elbow, lowerPivot);
  return { root, lower: lowerPivot, upperMesh, lowerMesh, endMesh };
}

function addClaws(handPivot, side, clawMaterial) {
  for (let i = 0; i < 3; i += 1) {
    const claw = mesh(new THREE.ConeGeometry(0.035, 0.22, 8), clawMaterial, (i - 1) * 0.075, -0.62, -0.1);
    claw.rotation.x = Math.PI / 2;
    claw.rotation.z = side * 0.16;
    handPivot.add(claw);
  }
}

function mesh(geometry, meshMaterial, x, y, z) {
  const object = new THREE.Mesh(geometry, meshMaterial);
  object.position.set(x, y, z);
  object.castShadow = true;
  object.receiveShadow = true;
  return object;
}

function material(color, roughness, metalness, emissive = 0x000000, emissiveIntensity = 0) {
  return new THREE.MeshStandardMaterial({
    color,
    roughness,
    metalness,
    emissive,
    emissiveIntensity
  });
}

function updateUi(timeNow) {
  const me = players.get(myId);
  if (myRole !== "guard" && cameraMonitorOpen) {
    toggleCameraMonitor(false);
  }
  roleText.textContent = me ? `${me.role}${me.caught ? " caught" : ""}` : "Connecting";
  const guardCanControl = myRole === "guard" && gameState?.phase === "live";
  leftDoorButton.disabled = !guardCanControl;
  rightDoorButton.disabled = !guardCanControl;
  cameraButton.disabled = myRole !== "guard";
  leftDoorButton.classList.toggle("active", Boolean(gameState?.doors?.left));
  rightDoorButton.classList.toggle("active", Boolean(gameState?.doors?.right));
  cameraButton.classList.toggle("active", cameraMonitorOpen);
  powerText.textContent = `${Math.round(gameState?.power ?? 100)}%`;
  powerBar.style.width = `${Math.max(0, gameState?.power ?? 100)}%`;

  if (gameState?.phase === "live") {
    const remaining = Math.max(0, Math.ceil((gameState.endsAt - timeNow) / 1000));
    const minutes = Math.floor(remaining / 60);
    const seconds = String(remaining % 60).padStart(2, "0");
    timerText.textContent = `${minutes}:${seconds}`;
    roundBanner.classList.add("hidden");
  } else if (gameState?.phase === "ended") {
    timerText.textContent = "Ended";
    roundTitle.textContent = gameState.winner === "guards" ? "Guards survived." : "Mascots won.";
    roundBanner.classList.remove("hidden");
  } else {
    timerText.textContent = "Lobby";
    roundBanner.classList.add("hidden");
  }

  if (myRole === "guard") {
    hintText.textContent = "WASD move, mouse look, Q left shutter, E right shutter, C cameras.";
  } else if (myRole === "mascot") {
    hintText.textContent = "WASD move, Shift sprint, mouse look. Touch a guard to catch them.";
  } else {
    hintText.textContent = "Choose a role. Click the game to lock your mouse.";
  }

  rosterList.innerHTML = "";
  for (const player of players.values()) {
    const item = document.createElement("li");
    const name = document.createElement("span");
    name.textContent = player.name + (player.id === myId ? " (you)" : "");
    const role = document.createElement("span");
    role.className = `tag ${player.role}`;
    role.textContent = player.caught ? "caught" : player.role;
    item.append(name, role);
    rosterList.append(item);
  }
}

function pushEvent(message) {
  events.unshift(message);
  events.length = Math.min(events.length, 5);
  eventFeed.innerHTML = "";
  for (const entry of events) {
    const item = document.createElement("li");
    item.textContent = entry;
    eventFeed.append(item);
  }
}

function animate() {
  requestAnimationFrame(animate);
  const frame = performance.now();
  const dt = Math.min(0.05, (frame - lastFrame) / 1000);
  lastFrame = frame;
  updateMovement(dt);
  animatePlayerRigs(dt);
  updateOfficeDoors(dt);
  updateCamera();
  updateViewModel(frame / 1000);
  renderer.render(scene, camera);
}

function animatePlayerRigs(dt) {
  for (const [id, model] of playerMeshes) {
    if (!model.visible) continue;

    if (id === myId) {
      model.position.set(position.x, 0, position.z);
      model.rotation.y = yaw;
      model.userData.moveAmount = localMoveAmount;
    } else {
      remoteTarget.copy(model.userData.target);
      model.position.lerp(remoteTarget, 0.34);
      model.rotation.y = lerpAngle(model.rotation.y, model.userData.targetYaw, 0.3);
    }

    animateRigPose(model, dt);
  }
}

function animateRigPose(model, dt) {
  const rig = model.userData.rig;
  const speed = THREE.MathUtils.clamp(model.userData.moveAmount || 0, 0, 1.35);
  const moving = speed > 0.04;
  model.userData.animTime += dt * (moving ? 6.4 + speed * 3.4 : 1.25);
  const t = model.userData.animTime;
  const stride = Math.sin(t);
  const counterStride = Math.sin(t + Math.PI);
  const bob = Math.abs(Math.sin(t * 2)) * 0.055 * speed;
  const idle = Math.sin(t * 0.9) * 0.018;

  model.children.forEach((child) => {
    if (child.type === "Group" || child.isMesh) child.position.y += 0;
  });
  model.position.y = rig.baseY + bob + idle;

  if (rig.type === "guard") {
    rig.headPivot.rotation.x = Math.sin(t * 0.65) * 0.04;
    rig.headPivot.rotation.y = Math.sin(t * 0.45) * 0.08 * (moving ? 1 : 0.35);
    rig.torso.rotation.x = -0.05 * speed;

    rig.leftArm.root.rotation.x = -stride * 0.62 * speed - 0.08;
    rig.rightArm.root.rotation.x = -counterStride * 0.52 * speed - 0.18;
    rig.leftArm.root.rotation.z = -0.08;
    rig.rightArm.root.rotation.z = 0.08;
    rig.leftArm.lower.rotation.x = 0.12 + Math.max(0, -stride) * 0.18 * speed;
    rig.rightArm.lower.rotation.x = 0.24;

    rig.leftLeg.root.rotation.x = stride * 0.72 * speed;
    rig.rightLeg.root.rotation.x = counterStride * 0.72 * speed;
    rig.leftLeg.lower.rotation.x = Math.max(0, -stride) * 0.48 * speed;
    rig.rightLeg.lower.rotation.x = Math.max(0, stride) * 0.48 * speed;
  } else {
    rig.headPivot.rotation.x = Math.sin(t * 0.72) * 0.055 - 0.04 * speed;
    rig.headPivot.rotation.y = Math.sin(t * 0.52) * 0.16;
    rig.torso.rotation.z = Math.sin(t * 0.6) * 0.035;
    rig.jaw.rotation.x = 0.1 + Math.max(0, Math.sin(t * 1.8)) * 0.26;

    rig.leftArm.root.rotation.x = -stride * 0.82 * speed - 0.16;
    rig.rightArm.root.rotation.x = -counterStride * 0.82 * speed - 0.16;
    rig.leftArm.root.rotation.z = -0.18 + Math.sin(t * 1.4) * 0.06;
    rig.rightArm.root.rotation.z = 0.18 - Math.sin(t * 1.4) * 0.06;
    rig.leftArm.lower.rotation.x = 0.32 + Math.max(0, stride) * 0.28 * speed;
    rig.rightArm.lower.rotation.x = 0.32 + Math.max(0, counterStride) * 0.28 * speed;

    rig.leftLeg.root.rotation.x = stride * 0.64 * speed;
    rig.rightLeg.root.rotation.x = counterStride * 0.64 * speed;
    rig.leftLeg.lower.rotation.x = Math.max(0, -stride) * 0.38 * speed;
    rig.rightLeg.lower.rotation.x = Math.max(0, stride) * 0.38 * speed;
  }
}

function lerpAngle(from, to, alpha) {
  const delta = Math.atan2(Math.sin(to - from), Math.cos(to - from));
  return from + delta * alpha;
}

function updateMovement(dt) {
  const me = players.get(myId);
  if (!me || me.caught || myRole === "spectator") {
    velocity.set(0, 0, 0);
    localMoveAmount = 0;
    return;
  }

  const forward = Number(keys.has("KeyS")) - Number(keys.has("KeyW"));
  const strafe = Number(keys.has("KeyD")) - Number(keys.has("KeyA"));
  const sprint = keys.has("ShiftLeft") || keys.has("ShiftRight");
  const baseSpeed = myRole === "mascot" ? 4.7 : 4.0;
  const speed = baseSpeed * (sprint ? 1.35 : 1);
  localMoveAmount = forward || strafe ? (sprint ? 1.15 : 0.82) : 0;

  reusableVector.set(strafe, 0, forward);
  if (reusableVector.lengthSq() > 0) reusableVector.normalize();
  reusableVector.applyAxisAngle(new THREE.Vector3(0, 1, 0), yaw);
  reusableVector.multiplyScalar(speed * dt);

  tryMove(reusableVector.x, reusableVector.z);

  camera.rotation.set(pitch, yaw, 0, "YXZ");
  send({
    type: "move",
    x: position.x,
    y: position.y,
    z: position.z,
    yaw
  });
}

function tryMove(dx, dz) {
  const nextX = position.x + dx;
  if (!collides(nextX, position.z)) position.x = nextX;
  const nextZ = position.z + dz;
  if (!collides(position.x, nextZ)) position.z = nextZ;
}

function collides(x, z) {
  dynamicWalls.length = 0;
  if (gameState?.doors?.left) {
    dynamicWalls.push({ x: -5.7, z: 12.15, width: 0.75, depth: 2.25 });
  }
  if (gameState?.doors?.right) {
    dynamicWalls.push({ x: 5.7, z: 12.15, width: 0.75, depth: 2.25 });
  }
  const walls = staticWalls.concat(dynamicWalls);
  const radius = 0.42;
  for (const wall of walls) {
    const halfW = wall.width / 2 + radius;
    const halfD = wall.depth / 2 + radius;
    if (Math.abs(x - wall.x) < halfW && Math.abs(z - wall.z) < halfD) return true;
  }
  return x < -21 || x > 21 || z < -15 || z > 15;
}

function updateCamera() {
  camera.position.copy(position);
  camera.rotation.set(pitch, yaw, 0, "YXZ");
}

function updateViewModel(timeSeconds) {
  const me = players.get(myId);
  const active = Boolean(me && myRole !== "spectator" && !me.caught);
  viewModel.visible = active;
  reticle.classList.toggle("hidden", !active);
  if (!active) {
    viewModelRefs.guard.root.visible = false;
    viewModelRefs.mascot.root.visible = false;
    return;
  }

  const walkBob = Math.sin(timeSeconds * 11) * 0.018 * localMoveAmount;
  const idleBob = Math.sin(timeSeconds * 1.7) * 0.012;
  viewModel.position.set(0, -0.22 + walkBob + idleBob, -0.03);
  viewModel.rotation.z = Math.sin(timeSeconds * 8.5) * 0.015 * localMoveAmount;

  const guardActive = myRole === "guard";
  viewModelRefs.guard.root.visible = guardActive;
  viewModelRefs.mascot.root.visible = !guardActive;

  if (guardActive) {
    const sway = Math.sin(timeSeconds * 8) * localMoveAmount;
    viewModelRefs.guard.leftSleeve.rotation.z = -0.24 - sway * 0.05;
    viewModelRefs.guard.rightSleeve.rotation.z = 0.28 + sway * 0.05;
    viewModelRefs.guard.flashlight.rotation.z = 0.08 + sway * 0.08;
    viewModelRefs.guard.tablet.position.y = -0.75 + Math.sin(timeSeconds * 1.5) * 0.01;
    viewModelRefs.guard.tabletScreen.position.y = -0.695 + Math.sin(timeSeconds * 1.5) * 0.01;
  } else {
    const clawPulse = Math.sin(timeSeconds * 6.5) * 0.04 + localMoveAmount * 0.03;
    viewModelRefs.mascot.clawLeft.rotation.x = -clawPulse;
    viewModelRefs.mascot.clawRight.rotation.x = clawPulse;
  }
}

function updateOfficeDoors(dt) {
  const speed = Math.min(1, dt * 7.5);
  for (const side of ["left", "right"]) {
    const door = officeDoorMeshes[side];
    if (!door) continue;
    const closed = Boolean(gameState?.doors?.[side]);
    const targetY = closed ? door.userData.closedY : door.userData.openY;
    door.position.y = THREE.MathUtils.lerp(door.position.y, targetY, speed);
  }
}
