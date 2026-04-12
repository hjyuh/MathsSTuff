---
title: Victorian Wheel — Printable Individual Parts Export
date: 2026-04-12
status: approved
---

# Design: Wheel printable-parts export

## Goal

Add a second STL export path to `wheel/wheel.html` that produces six individual, watertight, print-ready STL files — one per part type — without disturbing the existing 914 mm rendered assembly view or motion controls.

## Outputs

Six files, one part each, at full scale:

- `hub.stl`
- `rim_segment.stl`
- `spoke.stl`
- `gondola.stl`
- `support_cap.stl`
- `utility_pin.stl`

Minimal print-set counts (planning only, not reflected in file names): 1 hub, 12 rims, 12 spokes, 4 gondolas, 2 support caps, 12 utility pins. Base pieces, extra gondolas, extra pins, axle segments, and axle couplers are **not** included in the export set — the user builds the base from foamboard and uses a real 8.4 mm dowel for the axle.

## Manifold strategy

Rewrite each printable generator so the final part is ONE continuous solid by construction — no `mergeGeometries` on overlapping shells. No CSG dependency.

| Part | Technique | Single-solid guarantee |
|---|---|---|
| Hub | `LatheGeometry` with a closed 2D profile revolved 64× around Y | A closed lathe profile yields a topologically sealed surface of revolution. |
| Rim segment | Single `ExtrudeGeometry` of a 30° arc region (rIn..rOut) with through-holes | One extrude with through-holes only stays manifold. |
| Spoke | Single `ExtrudeGeometry` of a tapered trapezoid (r=50..rIn) with through-holes | Same rationale. |
| Gondola | Single `ExtrudeGeometry` of a bucket+handle silhouette with one pin-hole | Same rationale. Simpler look than rendered gondola — accepted tradeoff. |
| Support cap | Existing single `ExtrudeGeometry`, hole radius fixed 4.3 → 4.2 | Already single-solid. |
| Utility pin | `CylinderGeometry` | Already single-solid. |

## Dual-path geometry

- Existing `createHub / createRimSegment / createSpokeSection / createGondola / createSupportCap / createUtilityPin` stay as the **rendered** geometries. The assembly view is visually unchanged.
- New `buildPrintable*` functions produce **canonical single-solid** geometries used ONLY by the new export button.

The printable gondola will look simpler than the rendered gondola. This is explicitly approved — the rendered assembly view keeps the fancy version.

## Axle bore standardization

All axle-related bores use 4.2 mm radius (8.4 mm diameter) consistently:

- Hub bore — already 4.2 ✓
- Support cap hole — 4.3 → 4.2 (fix in both old and new functions)
- Axle coupler hole (if function retained) — 4.35 → 4.2

## UI

Add a second button "Export Individual Parts" below the existing "Download STL" button. It triggers a sequential download of the six STL files. Each download is produced by:

1. Building a fresh canonical geometry via `buildPrintable*`.
2. Wrapping it in a temporary `Mesh` centered near the origin and oriented in a print-ready pose.
3. Calling `STLExporter.parse(mesh, { binary: true })` once per part.
4. Triggering an anchor-click download with the exact file name.

The existing "Download STL" button is preserved and continues to export the current scene.

## Out of scope (do not touch)

- 914 mm overall diameter
- Rendered assembly view geometry (rim double-layer, spoke braces, complex gondola)
- Base stand, 12-gondola wheel, axle visualization cylinder
- Motion controls, spin rate slider, camera presets
- Print-layout kit and its populated scene

## Acceptance criteria

- "Export Individual Parts" button downloads exactly six files with the exact names above.
- Each STL, when imported into PrusaSlicer, reports as a single solid body (not multiple shells, not self-intersecting).
- All axle-related bores measure 8.4 mm diameter in-slicer.
- Wheel overall diameter unchanged at 914 mm.
- The rendered assembly view still renders, still spins, still responds to camera and motion controls.
- Existing "Download STL" button still works.
