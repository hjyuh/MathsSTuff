# Problem Web Redesign — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a polished, interactive force-directed graph visualization of math problems for the research community — searchable, zoomable, filterable, extensible.

**Architecture:** Vite + React 18 app with D3-force simulation rendered to Canvas for performance, HTML overlays for crisp text. Framer Motion for transitions, Tailwind for UI styling. Data in a single module for easy extension.

**Tech Stack:** Vite, React 18, D3 (d3-force, d3-zoom, d3-drag, d3-shape), Framer Motion, Tailwind CSS 3

---

### Task 1: Scaffold the Vite + React project

**Files:**
- Create: `visualize/package.json`
- Create: `visualize/vite.config.js`
- Create: `visualize/tailwind.config.js`
- Create: `visualize/postcss.config.js`
- Create: `visualize/index.html`
- Create: `visualize/src/main.jsx`
- Create: `visualize/src/styles/index.css`
- Create: `visualize/src/App.jsx`

**Step 1: Create package.json**

```json
{
  "name": "problem-web",
  "private": true,
  "version": "0.1.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  }
}
```

**Step 2: Install dependencies**

Run: `cd visualize && npm install react react-dom d3-force d3-zoom d3-drag d3-shape d3-selection framer-motion fuse.js`
Run: `npm install -D vite @vitejs/plugin-react tailwindcss postcss autoprefixer`

**Step 3: Create config files**

`vite.config.js`:
```js
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
export default defineConfig({ plugins: [react()] });
```

`tailwind.config.js`:
```js
export default {
  content: ["./index.html", "./src/**/*.{js,jsx}"],
  theme: {
    extend: {
      colors: {
        bg: { DEFAULT: "#09090b", card: "#0f0f14", border: "#1a1a2a" },
      },
      fontFamily: {
        sans: ["Inter", "system-ui", "sans-serif"],
        mono: ["JetBrains Mono", "monospace"],
      },
    },
  },
  plugins: [],
};
```

`postcss.config.js`:
```js
export default { plugins: { tailwindcss: {}, autoprefixer: {} } };
```

**Step 4: Create index.html**

```html
<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Problem Web</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet" />
</head>
<body class="bg-bg text-gray-200 antialiased">
  <div id="root"></div>
  <script type="module" src="/src/main.jsx"></script>
</body>
</html>
```

**Step 5: Create entry files**

`src/styles/index.css`:
```css
@tailwind base;
@tailwind components;
@tailwind utilities;

body { margin: 0; overflow: hidden; }
```

`src/main.jsx`:
```jsx
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import App from "./App";
import "./styles/index.css";
createRoot(document.getElementById("root")).render(<StrictMode><App /></StrictMode>);
```

`src/App.jsx`: Minimal shell rendering "Problem Web" text.

**Step 6: Verify dev server starts**

Run: `cd visualize && npm run dev`
Expected: Vite dev server at localhost:5173, page renders.

**Step 7: Commit**

```
feat: scaffold problem-web vite+react project
```

---

### Task 2: Data layer

**Files:**
- Create: `visualize/src/data/problems.js`

**Step 1: Create the data module**

Extract from existing `problem-web.jsx`: DOMAINS, METHODS, PROBLEMS arrays. Add `status` and `links` fields to the problem schema.

Status values: `"solved"`, `"partial"`, `"open"`, `"contributed"`
Links: `{ paper: null, forum: null, lean: null }`

Also export computed edges and lookup maps (problemById, problemsByMethod, problemsByDomain) for O(1) access.

**Step 2: Verify import works**

Add a temporary console.log in App.jsx importing the data, check browser console.

**Step 3: Commit**

```
feat: add problem data layer with domains, methods, and edges
```

---

### Task 3: Force simulation hook (useForceGraph)

**Files:**
- Create: `visualize/src/hooks/useForceGraph.js`

**Step 1: Implement the hook**

Uses d3-force with:
- `forceCenter` — center of viewport
- `forceManyBody` — repulsion (strength -120)
- `forceLink` — edges with distance 180
- `forceX` / `forceY` — gravity toward domain center positions
- `forceCollide` — prevent overlap (radius based on node size)

Returns: `{ nodes, edges, simulation }` where nodes have `x, y` positions updated each tick.

Accepts: `{ problems, edges, width, height, filterMethod, filterDomain }`

On filter change: restart simulation with new nodes, preserve positions of nodes that remain.

**Step 2: Wire into App.jsx with a temporary SVG to verify nodes position correctly**

**Step 3: Commit**

```
feat: d3 force simulation hook with domain gravity
```

---

### Task 4: Canvas graph renderer (GraphCanvas)

**Files:**
- Create: `visualize/src/components/GraphCanvas.jsx`

**Step 1: Implement Canvas rendering**

- `<canvas>` element fills parent container
- `useRef` for canvas context
- `requestAnimationFrame` render loop driven by simulation ticks
- Draw order: grid background → edges (quadratic beziers) → nodes → glows
- Nodes: filled circle (method color) + stroke ring (domain color)
- Edges: curved bezier, method color at 15% opacity default
- Hit detection: track mouse position, find nearest node within radius for hover

**Step 2: Implement d3-zoom**

- Attach d3-zoom behavior to canvas
- Transform all drawing through zoom transform
- Clamp zoom to [0.3, 4]
- Store transform in state for MiniMap

**Step 3: Implement d3-drag**

- On mousedown near a node, fix that node's position
- On mousemove, update node position
- On mouseup, release (reheat simulation slightly)

**Step 4: Implement HTML overlay for labels**

- Absolutely positioned `<div>` layer on top of canvas
- For each visible node, position a label div using the zoom transform
- Only render labels when zoom > 0.6 (declutter when zoomed out)
- Truncate long names

**Step 5: Wire into App.jsx**

**Step 6: Commit**

```
feat: canvas graph renderer with zoom, pan, drag, and labels
```

---

### Task 5: Filter bar

**Files:**
- Create: `visualize/src/components/FilterBar.jsx`

**Step 1: Implement filter pills**

- Top bar with two rows: Methods and Domains
- Each is a toggleable pill button
- Active pill shows method/domain color, inactive is muted
- Clicking toggles filter, updates App state which flows to useForceGraph
- "All" button to clear filters
- Animate filter changes with Framer Motion (layoutId for pills)

**Step 2: Commit**

```
feat: method and domain filter bar with animated pills
```

---

### Task 6: Detail panel

**Files:**
- Create: `visualize/src/components/DetailPanel.jsx`

**Step 1: Implement the panel**

Right-side panel (320px), slides in with Framer Motion AnimatePresence.

Contents when a problem is selected/hovered:
- Problem name (large)
- Solver + year + prize badge
- Domain badge + method badge (colored)
- Description text
- Difficulty bar (gradient, wider range than original)
- Status badge (solved/partial/open/contributed with distinct colors)
- Connected problems list (clickable, shows domain dot + name)
- Links section (paper/forum/lean icons — gray if no link, colored if present)

Empty state: diamond icon + "Select a node to explore" message.

**Step 2: Commit**

```
feat: detail panel with problem info, connections, and links
```

---

### Task 7: Search (Cmd-K)

**Files:**
- Create: `visualize/src/hooks/useSearch.js`
- Create: `visualize/src/components/SearchBar.jsx`

**Step 1: Implement useSearch hook**

Uses fuse.js for fuzzy search across: name, solver, desc, domain name, method name.
Returns ranked results.

**Step 2: Implement SearchBar component**

- Cmd+K (or Ctrl+K) opens an overlay modal
- Input field at top, results below
- Each result shows: domain color dot, name, solver, method badge
- Arrow keys to navigate, Enter to select (centers graph on that node + selects it)
- Escape to close
- Framer Motion fade in/out

**Step 3: Commit**

```
feat: cmd-k fuzzy search with keyboard navigation
```

---

### Task 8: MiniMap + Legend

**Files:**
- Create: `visualize/src/components/MiniMap.jsx`
- Create: `visualize/src/components/Legend.jsx`

**Step 1: MiniMap**

- Small (140x100) canvas in bottom-left corner
- Draws all nodes as tiny dots (domain colored)
- Shows viewport rectangle based on current zoom transform
- Click on minimap to pan to that area
- Only visible when zoom > 1.2

**Step 2: Legend**

- Bottom-right corner, semi-transparent
- Shows: "● fill = method", "○ ring = domain", "— edge = shared method"
- Collapsible

**Step 3: Commit**

```
feat: minimap viewport indicator and visual legend
```

---

### Task 9: Polish and integration

**Files:**
- Modify: `visualize/src/App.jsx` (final assembly)
- Modify: `visualize/src/styles/index.css` (grid background, scrollbar styling)

**Step 1: Assemble all components in App.jsx**

Layout:
```
┌──────────────────────────────────┬────────────┐
│ [FilterBar]                      │            │
│ ┌──────────────────────────────┐ │  Detail    │
│ │                              │ │  Panel     │
│ │     GraphCanvas              │ │            │
│ │                              │ │            │
│ │  [MiniMap]        [Legend]   │ │            │
│ └──────────────────────────────┘ │            │
│ [Footer: author · count · date]  │            │
└──────────────────────────────────┴────────────┘
         [SearchBar overlay on Cmd-K]
```

**Step 2: Add grid background pattern**

CSS: subtle dot grid on the canvas container using radial-gradient.

**Step 3: Add responsive sizing**

GraphCanvas fills available space via ResizeObserver, simulation restarts on resize.

**Step 4: Double-click to center**

Double-click a node → smooth zoom transition to center that node at 2x zoom.

**Step 5: Keyboard shortcuts**

- Escape: deselect, close search
- `/` or Cmd+K: open search
- `r`: reset zoom to fit all

**Step 6: Final visual pass**

- Ensure all transitions are smooth
- Check color contrast
- Footer with "Mahmoud · 2026 · N problems · M methods"

**Step 7: Commit**

```
feat: final assembly, grid background, keyboard shortcuts, responsive layout
```

---

### Task 10: Clean up old file

**Files:**
- Delete: `visualize/problem-web.jsx` (replaced by the new app)

**Step 1: Remove the old standalone JSX**

**Step 2: Commit**

```
chore: remove legacy problem-web.jsx
```
