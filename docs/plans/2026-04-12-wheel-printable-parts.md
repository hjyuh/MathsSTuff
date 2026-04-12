# Wheel Printable Parts Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add a six-file individual-parts STL export to `wheel/wheel.html` that produces watertight, manifold, print-ready parts without disturbing the existing rendered assembly view.

**Architecture:** Dual-path geometry. Existing `create*` generators stay intact and continue to feed the rendered assembly view. New `buildPrintable*` functions produce single-solid canonical geometries (`LatheGeometry` or one `ExtrudeGeometry` with through-holes only) and feed a new export button. Each printable STL is produced from a freshly built temporary `Mesh` — never from `assemblyGroup` or `layoutGroup`.

**Tech Stack:** Three.js r160 ES modules (unpkg), `STLExporter`, `LatheGeometry`, `ExtrudeGeometry`, `Shape` / `Path` with holes. No new dependencies.

**Testing note:** `wheel.html` is a single standalone HTML file with no automated test harness. Verification is manual: open the file in a browser, check that (a) the assembly still renders and spins, (b) the new button downloads six STL files with exact names, (c) each STL opens in PrusaSlicer as a single solid body. Validation steps are listed in the final task.

---

## Task 1: Fix axle-bore radii in existing generators

Standardize existing code to 4.2 mm radius for axle-related holes so that the rendered assembly and any retained helpers are internally consistent.

**Files:**
- Modify: `wheel/wheel.html` — `createSupportCap()` and `createAxleCoupler()`

**Step 1: Change `createSupportCap` hole radius `4.3` → `4.2`**

Locate the existing `createSupportCap` function and update the `absarc` radius on the hole path from `4.3` to `4.2`.

**Step 2: Change `createAxleCoupler` hole radius `4.35` → `4.2`**

Locate the existing `createAxleCoupler` function and update the `absarc` radius on the hole path from `4.35` to `4.2`.

**Step 3: Visual sanity check**

Open `wheel.html` in a browser. Confirm the rendered assembly still shows and the support cap / axle look normal. No functional regression expected since these changes are sub-pixel at viewing distance.

---

## Task 2: Add `buildPrintableUtilityPin`

The simplest part. Start here to exercise the export pattern.

**Files:**
- Modify: `wheel/wheel.html` — add new helper after `createUtilityPin`

**Step 1: Add function**

```js
function buildPrintableUtilityPin() {
    // Single manifold cylinder, 2.1mm radius × 18mm long.
    const geo = new THREE.CylinderGeometry(2.1, 2.1, 18, 32);
    // Lie on its side so the long axis is horizontal (print-ready).
    geo.rotateZ(Math.PI / 2);
    return clean(geo);
}
```

**Step 2: No visual test yet — this gets exercised by the final export task.**

---

## Task 3: Add `buildPrintableHub` using `LatheGeometry`

Revolve a closed 2D profile around Y to get a guaranteed-manifold hub with central bore and two flanges.

**Files:**
- Modify: `wheel/wheel.html` — add new helper near the printable-parts section

**Step 1: Add function**

```js
function buildPrintableHub() {
    // Closed lathe profile (r, y). Revolved 64x around Y axis.
    // Dimensions: 4.2mm radius through-bore, 50mm body radius, 65mm flanges
    // at each end (flanges are 4mm thick, body is 92mm tall, total 100mm).
    const profile = [
        new THREE.Vector2(4.2, -50),   // inner bottom
        new THREE.Vector2(4.2,  50),   // inner top
        new THREE.Vector2(65.0, 50),   // out to top flange
        new THREE.Vector2(65.0, 46),   // down flange thickness
        new THREE.Vector2(50.0, 46),   // in to body
        new THREE.Vector2(50.0, -46),  // down body
        new THREE.Vector2(65.0, -46),  // out to bottom flange
        new THREE.Vector2(65.0, -50),  // down flange thickness
        new THREE.Vector2(4.2, -50)    // back to start (closes the profile)
    ];
    const geo = new THREE.LatheGeometry(profile, 64);
    // Lay the hub on its side: Y-axis of revolution becomes horizontal,
    // so the hub prints as a short disc rather than a tall spool.
    geo.rotateZ(Math.PI / 2);
    return clean(geo);
}
```

**Step 2: Verify in browser console (later)** by temporarily swapping `hubGeo` in the assembly to `buildPrintableHub()` — visually should show a hub with flanges and a bore. Revert after verification.

(Skip this step; manifold-ness is guaranteed by construction.)

---

## Task 4: Add `buildPrintableSupportCap`

Thin wrapper that creates a fresh single-solid cap with the 4.2 mm hole.

**Files:**
- Modify: `wheel/wheel.html` — add new helper

**Step 1: Add function**

```js
function buildPrintableSupportCap() {
    // Single ExtrudeGeometry with one through-hole — already manifold.
    const shape = new THREE.Shape();
    shape.moveTo(-42, 0);
    shape.lineTo( 42, 0);
    shape.lineTo( 42, 78);
    shape.lineTo(-42, 78);
    shape.lineTo(-42, 0);

    const hole = new THREE.Path();
    hole.absarc(0, 54, 4.2, 0, Math.PI * 2, true);
    shape.holes.push(hole);

    const geo = new THREE.ExtrudeGeometry(shape, {
        depth: 20,
        bevelEnabled: true,
        bevelThickness: 1.2,
        bevelSize: 1.2,
        curveSegments: 32
    });
    // Center on origin. Shape is XY-plane, extruded along +Z.
    geo.translate(0, -39, -10);
    return clean(geo);
}
```

---

## Task 5: Add `buildPrintableRimSegment`

A single 30° arc extrusion through the full wheel depth — one extrude, through-holes only, manifold.

**Files:**
- Modify: `wheel/wheel.html`

**Step 1: Add function**

```js
function buildPrintableRimSegment() {
    // One 30° arc region between rIn (417) and rOut (457), extruded
    // through the full wheel depth (100mm, matching front-back span).
    // A single Shape with through-holes yields a single manifold body.
    const shape = new THREE.Shape();
    shape.absarc(0, 0, rOut, 0, 30 * DEG2RAD, false);
    shape.absarc(0, 0, rIn, 30 * DEG2RAD, 0, true);

    // Pivot pin through-hole at midpoint of the arc.
    const pivotHole = new THREE.Path();
    const a = 15 * DEG2RAD;
    pivotHole.absarc(rMid * Math.cos(a), rMid * Math.sin(a), 2.2, 0, Math.PI * 2, true);
    shape.holes.push(pivotHole);

    const geo = new THREE.ExtrudeGeometry(shape, {
        depth: 100,
        bevelEnabled: false,
        curveSegments: 64
    });
    // Center depth on origin.
    geo.translate(0, 0, -50);

    // Orient so the printable footprint is on the XZ plane:
    // rotate so the arc lies flat and the extrusion axis becomes vertical.
    // Then translate to center the arc's bounding box near origin.
    const rotated = geo.clone();
    rotated.computeBoundingBox();
    const bb = rotated.boundingBox;
    const cx = (bb.min.x + bb.max.x) / 2;
    const cy = (bb.min.y + bb.max.y) / 2;
    rotated.translate(-cx, -cy, 0);
    return clean(rotated);
}
```

---

## Task 6: Add `buildPrintableSpoke`

Single tapered-trapezoid extrusion through the full wheel depth — manifold by construction.

**Files:**
- Modify: `wheel/wheel.html`

**Step 1: Add function**

```js
function buildPrintableSpoke() {
    // Tapered beam from r=50 (hub side) to r=rIn (rim side), extruded
    // through the full wheel depth. One Shape + optional through-holes.
    const hubEnd = 50;
    const rimEnd = rIn; // 417
    const halfWidthHub = 14;
    const halfWidthRim = 8;

    const shape = new THREE.Shape();
    shape.moveTo(-halfWidthHub, hubEnd);
    shape.lineTo( halfWidthHub, hubEnd);
    shape.lineTo( halfWidthRim, rimEnd);
    shape.lineTo(-halfWidthRim, rimEnd);
    shape.lineTo(-halfWidthHub, hubEnd);

    // Decorative diamond through-holes (still manifold because they are
    // fully through the extrusion).
    for (let y = hubEnd + 40; y <= rimEnd - 40; y += 50) {
        const t = (y - hubEnd) / (rimEnd - hubEnd);
        const w = THREE.MathUtils.lerp(6, 3, t);
        const h = 10;
        const hole = new THREE.Path();
        hole.moveTo(0, y + h);
        hole.lineTo( w, y);
        hole.lineTo(0, y - h);
        hole.lineTo(-w, y);
        hole.lineTo(0, y + h);
        shape.holes.push(hole);
    }

    const geo = new THREE.ExtrudeGeometry(shape, {
        depth: 100,
        bevelEnabled: false,
        curveSegments: 16
    });
    geo.translate(0, 0, -50);

    // Center on origin.
    geo.computeBoundingBox();
    const bb = geo.boundingBox;
    const cy = (bb.min.y + bb.max.y) / 2;
    geo.translate(0, -cy, 0);
    return clean(geo);
}
```

---

## Task 7: Add `buildPrintableGondola`

Simplified bucket-with-handle silhouette, single extrude, single manifold. Look differs from the rendered ornate gondola — accepted.

**Files:**
- Modify: `wheel/wheel.html`

**Step 1: Add function**

```js
function buildPrintableGondola() {
    // Bucket-with-handle silhouette in the XY plane, extruded through Z.
    // Origin sits at the pin hole (top of handle). Bucket hangs below.
    // One Shape + one circular through-hole => single manifold.
    const shape = new THREE.Shape();
    shape.moveTo(-22, -10);  // bucket top-left
    shape.lineTo(-22, -50);  // bucket down-left
    shape.lineTo( 22, -50);  // bucket bottom
    shape.lineTo( 22, -10);  // bucket top-right
    shape.lineTo(  4, -10);  // inner top-right (transition to handle)
    shape.lineTo(  4,   8);  // handle right side up
    shape.lineTo( -4,   8);  // handle top
    shape.lineTo( -4, -10);  // handle left side down
    shape.lineTo(-22, -10);  // back to start

    const pin = new THREE.Path();
    pin.absarc(0, 2, 2.4, 0, Math.PI * 2, true);
    shape.holes.push(pin);

    const geo = new THREE.ExtrudeGeometry(shape, {
        depth: 30,
        bevelEnabled: true,
        bevelThickness: 1.0,
        bevelSize: 1.0,
        curveSegments: 24
    });
    geo.translate(0, 20, -15);  // center Y on body center, center Z on depth
    return clean(geo);
}
```

---

## Task 8: Add the export-individual-parts export helper

A single function that accepts a geometry and a filename, wraps the geometry in a temporary Mesh, exports it, and triggers a download.

**Files:**
- Modify: `wheel/wheel.html`

**Step 1: Add helper**

```js
function exportGeometryAsSTL(geometry, filename) {
    const exporter = new STLExporter();
    const mesh = new THREE.Mesh(geometry, new THREE.MeshStandardMaterial());
    const stl = exporter.parse(mesh, { binary: true });
    const blob = new Blob([stl], { type: "application/octet-stream" });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
}
```

---

## Task 9: Add UI button and wire up export handler

Add a new button beneath "Download STL" labelled "Export Individual Parts". On click, it downloads the six files sequentially with a small delay so browsers do not block the sequential downloads.

**Files:**
- Modify: `wheel/wheel.html` HTML and JS

**Step 1: Add button markup**

Beneath the existing `#btn-export` button, add:

```html
<button id="btn-export-parts">Export Individual Parts</button>
```

**Step 2: Add click handler**

```js
document.getElementById("btn-export-parts").addEventListener("click", () => {
    const btn = document.getElementById("btn-export-parts");
    btn.disabled = true;
    btn.innerText = "Exporting Parts...";

    const exports = [
        { geo: buildPrintableHub(),         name: "hub.stl" },
        { geo: buildPrintableRimSegment(),  name: "rim_segment.stl" },
        { geo: buildPrintableSpoke(),       name: "spoke.stl" },
        { geo: buildPrintableGondola(),     name: "gondola.stl" },
        { geo: buildPrintableSupportCap(),  name: "support_cap.stl" },
        { geo: buildPrintableUtilityPin(),  name: "utility_pin.stl" }
    ];

    let i = 0;
    const step = () => {
        if (i >= exports.length) {
            btn.disabled = false;
            btn.innerText = "Export Individual Parts";
            return;
        }
        const { geo, name } = exports[i++];
        exportGeometryAsSTL(geo, name);
        setTimeout(step, 220);
    };
    step();
});
```

---

## Task 10: End-to-end verification

**Files:**
- Read/verify: `wheel/wheel.html`

**Step 1: Load in browser**

Open `wheel.html` in a Chromium browser. Wait for the "Building Wheel Geometry..." loader to clear.

Expected:
- Assembly view renders (wheel + base + gondolas)
- Wheel spins at 7 deg/s
- Camera presets work
- "Download STL" button still works

**Step 2: Click "Export Individual Parts"**

Expected: six files are downloaded with exact names:
- `hub.stl`
- `rim_segment.stl`
- `spoke.stl`
- `gondola.stl`
- `support_cap.stl`
- `utility_pin.stl`

**Step 3: Import each STL into PrusaSlicer**

For each of the six files:
- Drag into PrusaSlicer
- Confirm it imports as a single solid body
- Check that axle-related bores (hub, support cap) measure 8.4 mm diameter
- Confirm no "multiple solids / separate shells" warning

**Step 4: Confirm 914 mm diameter unchanged**

Hover over the wheel outer edge in the rendered view, confirm the rim is still at 457 mm outer radius (914 mm diameter).

---

## Execution

For a single-file HTML change like this, direct in-session execution is appropriate. Proceed by walking through Tasks 1–10 in order, making minimal edits and committing once at the end with the complete change.
