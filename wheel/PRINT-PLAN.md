# Victorian Ferris Wheel — Print & Assembly Plan
**Due: April 21, 2026 | Diameter: 914mm (3 feet) | Scale: 1:1 (no scaling needed)**

---

## STL STATUS
- `wheel.html` — Procedural CAD viewer with print layout export. Open in browser.
- `wheel_colorcode.html` — Color-coded version with minimal build toggle (in outputs).
- Combined assembly STL already at correct 914mm diameter.
- **TODO:** Merge 3 spoke sections into single-piece spokes in Blender (10 min job).

---

## MINIMAL BUILD — 46 PIECES

| Part | Qty | Material | Color | Notes |
|------|-----|----------|-------|-------|
| Rim segments | 12 | PLA | White | 30° arc each, ~236mm chord |
| Full spokes (single piece) | 12 | PLA | White | 367mm long, print DIAGONALLY on bed |
| Hub | 1 | PLA | Black | 130mm diameter, 108mm tall, 8.4mm axle bore |
| Gondolas | 4 | PLA | Red | At 0°, 90°, 180°, 270° positions |
| Axle segments | 2 | PLA | Black | 4mm radius cylinders |
| Axle coupler | 1 | PLA | Black | Joins two axle halves |
| Support caps | 2 | PLA | Black | Where axle meets stand |
| Utility pins | 12 | PLA | Any | 4mm × 18mm connection pins |
| **Simple A-frame base** | 2-4 | PLA or foamboard | Black | Replaces 33-piece Victorian base |
| **TOTAL** | **~46** | | | |

### What was CUT from full build (saves ~20 hours of printing):
- ❌ 33-piece modular Victorian base → replaced with simple A-frame
- ❌ 8 gondolas (kept 4 at cardinal positions)
- ❌ 12 utility pins (kept 12, cut 12)
- ❌ Mid spoke sections eliminated by merging into single-piece spokes

---

## MOTOR SETUP (friction drive — no design changes needed)

### How it works:
The motor doesn't connect to the axle. Instead, it sits on the base and presses
a small rubber tip against the outside of the rim. Motor spins → rubber grips rim →
wheel turns. Like a finger spinning a record. Zero code changes to the wheel design.

### Shopping list:

| Item | Cost | Where |
|------|------|-------|
| GA12-N20 geared motor (30 RPM, 6V) | ~$6 | Amazon |
| 2× AA battery holder with ON/OFF switch | ~$3 | Amazon or electronics store |
| 2× AA batteries | ~$2 | Anywhere |
| **Total** | **~$11** | |

### Wiring (dead simple, no code, no Arduino):
```
[2× AA batteries in holder] → [switch] → [motor]
```
Two wires. Positive through the switch to one motor lead, negative to the other.
Switch ON = wheel spins. Switch OFF = wheel stops.
If it spins backwards, swap the two wires.

Running the 6V motor on 3V (2× AA) gives roughly 15 RPM — a gentle Ferris wheel pace.

### Mounting:
1. Position the motor inside the A-frame base, near where the rim passes closest to the base
2. Hot glue or zip-tie the motor body to the base structure
3. Stick a small piece of eraser or rubber onto the motor shaft tip (for grip)
4. The rubber tip should press lightly against the rim's outer edge
5. If grip is weak, wrap a rubber band around the rim at the contact point
6. Battery holder sits on the base platform, switch accessible from outside
7. Motor is hidden inside the base — audience just sees the wheel spin

### Troubleshooting:
- Wheel doesn't spin: press motor tighter against rim, add more rubber to shaft tip
- Wheel spins too fast: use 1× AA (1.5V) instead of 2
- Wheel spins wrong direction: swap the two wires on the motor
- Motor slips on rim: wrap rubber band around rim at contact point

---

## PRINTERS AVAILABLE

| Printer | Location | Bed Size | Constraints |
|---------|----------|----------|-------------|
| Prusa XL #1 | Library | 360×360×360mm | 4hr regular + 8hr overnight/week/card |
| Prusa XL #2 | Library | 360×360×360mm | Same — need 2nd person's card |
| School Printer A | School | TBD (~305mm+) | No hourly limits? Check with teacher |
| School Printer B | School | TBD (~305mm+) | Same |

### Library file transfer: Google Drive link → their computers. No USB needed.
### Free PLA colors: Black, White, Red, Blue

---

## PRINT ORIENTATION GUIDE

**Rim segments:** Flat, curved side down. 3 per print. ~1.5hr each batch.

**Full spokes:** DIAGONAL across bed at ~45°. 367mm length > 360mm bed width, but diagonal = 509mm so it fits. 2 per print. ~40min each batch.

**Hub:** Flat, circular face down. Solo print. ~1.5hr.

**Gondolas:** Upright, floor on bed. All 4 fit in one print. ~2hr.

**Axle + coupler + caps:** All in one batch. ~1.5hr.

**Pins:** All 12 standing upright. One batch. ~30min.

---

## SCHEDULE — 2 LIBRARY PRINTERS SIMULTANEOUS

**Requires: You + 1 other person (partner #2, mom, dad, or brother)**

| Session | Printer A (you) | Printer B (helper) | Wall Time |
|---------|-----------------|-------------------|-----------|
| 1 | 3 rim segments | 3 rim segments | 1.5hr |
| 2 | 3 rim segments | 3 rim segments | 1.5hr |
| 3 | 2 spokes (diagonal) | 2 spokes (diagonal) | 40min |
| 4 | 2 spokes | 2 spokes | 40min |
| 5 | 2 spokes | 2 spokes | 40min |
| 6 | Hub | 4 gondolas + 12 pins | 1.5hr |
| 7 | Axle + coupler + caps | Reprints / base | 1.5hr |
| **TOTAL** | | | **~8 hours** |

### Fits into library rules:
- **Day 1:** You take 4hr regular, helper takes 4hr regular. Sessions 1-5 done.
- **Day 2:** You take 8hr overnight, helper takes 8hr overnight. Sessions 6-7 + buffer.
- **DONE IN 2 DAYS.**

### Backup: School printers handle small parts (spokes, gondolas, pins) in parallel.

---

## ASSEMBLY ORDER

1. **Test fit** — dry-assemble 2-3 rim segments with spokes before gluing anything
2. **Hub + spokes** — glue all 12 spokes to hub, let cure
3. **Spokes + rim** — attach rim segments to spoke ends, work around the circle
4. **Pin joints** — insert utility pins at rim segment connections
5. **Gondolas** — attach at pivot points on rim (4 positions)
6. **Base** — build simple A-frame stand (2 triangular supports + crossbar)
7. **Axle** — insert through hub, mount on support caps on base
8. **Motor** — mount motor inside base, rubber tip touching rim, wire to battery pack
9. **Touch up** — sand any rough joints, optional paint

### Glue: Super glue (CA) or plastic model cement for PLA
### Axle: 8.4mm metal rod or wooden dowel
### Assembly time: 5-7 days working between classes / at home

---

## PREP BEFORE FIRST LIBRARY VISIT

- [ ] Open `wheel.html` in browser, verify model looks correct
- [ ] In Blender: import spoke STLs, boolean union inner+mid+outer into single piece, export 1 spoke STL
- [ ] Install PrusaSlicer, load Prusa XL profile
- [ ] Slice all pieces: 0.2mm layer height, 15% infill, PLA settings
- [ ] Upload .gcode files to Google Drive in labeled folders
- [ ] Book library reservation (Day 1: 4hr regular slot)
- [ ] Confirm helper (partner #2 / family) for 2nd printer reservation
- [ ] Buy: super glue, 8.4mm dowel rod, GA12-N20 motor, 2×AA battery holder w/ switch, AA batteries

---

## COMPETITION CONTEXT
- Average past project: ~1 foot diameter
- Our project: 3 feet diameter (3× bigger, 9× visual area)
- Victorian structural detail (diamond cutouts, interlocking segments, gondolas with roofs)
- Color scheme: White structure + Black hub/base + Red gondolas = clean Victorian aesthetic
- MOTORIZED — wheel actually spins during exhibition
- Engineering explanation ready: segmentation for print constraints, diagonal orientation, overlap joints, friction drive motor

---

## CONTINGENCY
- If a print fails: 8 days of buffer before deadline
- If school printers are unavailable: library alone can handle everything in 2-3 days
- If no helper for 2nd library printer: single printer finishes in ~4 days (still fine)
- If spoke merge in Blender fails: print 3-section spokes instead (adds ~4hr, still fits timeline)
- Base alternative: foamboard + hot glue A-frame instead of printing (saves ~2hr)
- If motor doesn't grip rim: wrap rubber band around rim at contact point
- If motor is too fast: reduce to 1× AA battery (1.5V instead of 3V)
