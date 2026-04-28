import { useRef, useEffect, useCallback, useMemo, useState } from "react";
import * as d3Zoom from "d3-zoom";
import * as d3Selection from "d3-selection";

import { DOMAINS } from "../data/problems.js";
import { METHOD_TREE, METHOD_LOOKUP, getMethodColor } from "../data/methodTree.js";

// ── helpers ──────────────────────────────────────────────────────────────────

function nodeRadius(layer) {
  return Math.max(6, Math.min(12, layer * 1.1));
}

function truncate(s, max = 22) {
  return s.length > max ? s.slice(0, max - 1) + "\u2026" : s;
}

/** Deterministic perpendicular offset for bezier control point */
function ctrlPoint(sx, sy, tx, ty, idx) {
  const mx = (sx + tx) / 2;
  const my = (sy + ty) / 2;
  const dx = tx - sx;
  const dy = ty - sy;
  const len = Math.sqrt(dx * dx + dy * dy) || 1;
  // perpendicular unit vector
  const px = -dy / len;
  const py = dx / len;
  // offset alternates direction based on index
  const off = (20 + (idx % 3) * 10) * (idx % 2 === 0 ? 1 : -1);
  return { cx: mx + px * off, cy: my + py * off };
}

/** Get dash pattern and line width for edge type */
function edgeStyle(type) {
  switch (type) {
    case "engine":     return { dash: null, lineWidth: 2 };
    case "bridge":     return { dash: [8, 4], lineWidth: 1.5 };
    case "scaffold":   return { dash: [3, 3], lineWidth: 1 };
    case "closer":     return { dash: [3, 3], lineWidth: 1 };
    case "cross-role": return { dash: [8, 3, 2, 3], lineWidth: 1 };
    default:           return { dash: null, lineWidth: 1 };
  }
}

// ── component ────────────────────────────────────────────────────────────────

export default function GraphCanvas({
  problems,
  edges: rawEdges,
  problemByIdMap,
  activePath,
  filterDomain,
  hovered,
  setHovered,
  selected,
  setSelected,
  // Force graph results (lifted from useForceGraph)
  nodes,
  simEdges,
  simulation,
  transform,
  setTransform,
  _tick,
  // Container size
  containerSize,
  onContainerResize,
  // Zoom ref exposed for parent
  zoomRef: externalZoomRef,
}) {
  const containerRef = useRef(null);
  const canvasRef = useRef(null);
  const overlayRef = useRef(null);
  const dragState = useRef(null);
  const internalZoomRef = useRef(null);

  // Pulse animation time for open nodes
  const [pulseTime, setPulseTime] = useState(0);
  useEffect(() => {
    let frame;
    const animate = () => {
      setPulseTime(Date.now());
      frame = requestAnimationFrame(animate);
    };
    frame = requestAnimationFrame(animate);
    return () => cancelAnimationFrame(frame);
  }, []);

  // Container size via ResizeObserver — report to parent
  useEffect(() => {
    const el = containerRef.current;
    if (!el) return;
    const ro = new ResizeObserver((entries) => {
      for (const e of entries) {
        const { width: w, height: h } = e.contentRect;
        if (w > 0 && h > 0) onContainerResize?.(w, h);
      }
    });
    ro.observe(el);
    return () => ro.disconnect();
  }, [onContainerResize]);

  const width = containerSize?.w || 800;
  const height = containerSize?.h || 600;

  // Build adjacency set for highlighting connected nodes
  const adjacency = useMemo(() => {
    const adj = new Map();
    for (const e of simEdges) {
      const sid = typeof e.source === "object" ? e.source.id : e.source;
      const tid = typeof e.target === "object" ? e.target.id : e.target;
      if (!adj.has(sid)) adj.set(sid, new Set());
      if (!adj.has(tid)) adj.set(tid, new Set());
      adj.get(sid).add(tid);
      adj.get(tid).add(sid);
    }
    return adj;
  }, [simEdges]);

  const isConnected = useCallback(
    (id) => {
      const active = hovered || selected;
      if (!active) return true;
      if (id === active) return true;
      const neighbors = adjacency.get(active);
      return neighbors ? neighbors.has(id) : false;
    },
    [hovered, selected, adjacency],
  );

  // ── d3-zoom setup ──────────────────────────────────────────────────────────
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const sel = d3Selection.select(canvas);

    const zoom = d3Zoom
      .zoom()
      .scaleExtent([0.3, 4])
      .filter((event) => {
        // Allow wheel zoom and drag (but not when we are node-dragging)
        if (dragState.current) return false;
        return true;
      })
      .on("zoom", (event) => {
        const t = event.transform;
        setTransform({ x: t.x, y: t.y, k: t.k });
      });

    sel.call(zoom);
    internalZoomRef.current = zoom;
    if (externalZoomRef) externalZoomRef.current = { zoom, selection: sel };

    // Double-click: zoom to node
    sel.on("dblclick.zoom", null); // remove default d3 dblclick
    sel.on("dblclick", (event) => {
      const rect = canvas.getBoundingClientRect();
      const mx = (event.clientX - rect.left);
      const my = (event.clientY - rect.top);

      // Inverse transform
      const ix = (mx - transform.x) / transform.k;
      const iy = (my - transform.y) / transform.k;

      // Find nearest node
      let best = null;
      let bestDist = Infinity;
      for (const n of nodes) {
        const d = Math.hypot(n.x - ix, n.y - iy);
        if (d < nodeRadius(n.layer) + 5 && d < bestDist) {
          bestDist = d;
          best = n;
        }
      }

      if (best) {
        // Smooth zoom to node at 2x
        const targetK = 2;
        const targetX = width / 2 - best.x * targetK;
        const targetY = height / 2 - best.y * targetK;
        const t = d3Zoom.zoomIdentity.translate(targetX, targetY).scale(targetK);
        sel.transition().duration(500).call(zoom.transform, t);
      }
    });

    return () => {
      sel.on(".zoom", null);
      sel.on("dblclick", null);
    };
  }, [width, height]); // re-attach if size changes; transform/nodes accessed via refs below

  // ── pointer events (hover, click, drag) ────────────────────────────────────
  const findNodeAt = useCallback(
    (mx, my) => {
      const ix = (mx - transform.x) / transform.k;
      const iy = (my - transform.y) / transform.k;
      let best = null;
      let bestDist = Infinity;
      for (const n of nodes) {
        const d = Math.hypot(n.x - ix, n.y - iy);
        const r = nodeRadius(n.layer) + 5;
        if (d < r && d < bestDist) {
          bestDist = d;
          best = n;
        }
      }
      return best;
    },
    [nodes, transform],
  );

  const handlePointerDown = useCallback(
    (event) => {
      const rect = canvasRef.current.getBoundingClientRect();
      const mx = event.clientX - rect.left;
      const my = event.clientY - rect.top;
      const node = findNodeAt(mx, my);
      if (node && simulation.current) {
        dragState.current = { node, startX: mx, startY: my, moved: false };
        node.fx = node.x;
        node.fy = node.y;
        simulation.current.alphaTarget(0.3).restart();
      }
    },
    [findNodeAt, simulation],
  );

  const handlePointerMove = useCallback(
    (event) => {
      const rect = canvasRef.current.getBoundingClientRect();
      const mx = event.clientX - rect.left;
      const my = event.clientY - rect.top;

      if (dragState.current) {
        const ds = dragState.current;
        const dx = mx - ds.startX;
        const dy = my - ds.startY;
        if (Math.abs(dx) > 3 || Math.abs(dy) > 3) ds.moved = true;

        const ix = (mx - transform.x) / transform.k;
        const iy = (my - transform.y) / transform.k;
        ds.node.fx = ix;
        ds.node.fy = iy;
        return;
      }

      // Hover detection
      const node = findNodeAt(mx, my);
      setHovered(node ? node.id : null);
    },
    [findNodeAt, transform, setHovered],
  );

  const handlePointerUp = useCallback(
    (event) => {
      if (dragState.current) {
        const ds = dragState.current;
        ds.node.fx = null;
        ds.node.fy = null;
        if (simulation.current) simulation.current.alphaTarget(0);

        if (!ds.moved) {
          // Click
          const clickedId = ds.node.id;
          setSelected((prev) => (prev === clickedId ? null : clickedId));
        }
        dragState.current = null;
        return;
      }
    },
    [simulation, setSelected],
  );

  // Attach pointer events to canvas
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    canvas.addEventListener("pointerdown", handlePointerDown);
    canvas.addEventListener("pointermove", handlePointerMove);
    canvas.addEventListener("pointerup", handlePointerUp);
    return () => {
      canvas.removeEventListener("pointerdown", handlePointerDown);
      canvas.removeEventListener("pointermove", handlePointerMove);
      canvas.removeEventListener("pointerup", handlePointerUp);
    };
  }, [handlePointerDown, handlePointerMove, handlePointerUp]);

  // ── Canvas draw ────────────────────────────────────────────────────────────
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const dpr = window.devicePixelRatio || 1;
    canvas.width = width * dpr;
    canvas.height = height * dpr;
    canvas.style.width = width + "px";
    canvas.style.height = height + "px";

    const ctx = canvas.getContext("2d");
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, width, height);

    const t = transform;
    const active = hovered || selected;
    const now = pulseTime;

    // ── 1. Dot grid background (no transform — screen space) ──
    ctx.fillStyle = "rgba(255,255,255,0.03)";
    const step = 30;
    for (let gx = 0; gx < width; gx += step) {
      for (let gy = 0; gy < height; gy += step) {
        ctx.beginPath();
        ctx.arc(gx, gy, 1, 0, Math.PI * 2);
        ctx.fill();
      }
    }

    // Apply zoom transform for everything else
    ctx.save();
    ctx.translate(t.x, t.y);
    ctx.scale(t.k, t.k);

    // ── 2. Method category regions ──
    for (const [key, cat] of Object.entries(METHOD_TREE)) {
      const dx = cat.x * width;
      const dy = cat.y * height;
      const r = Math.min(width, height) * 0.22;

      ctx.beginPath();
      ctx.arc(dx, dy, r, 0, Math.PI * 2);
      ctx.fillStyle = cat.color + "0d"; // ~5% opacity
      ctx.fill();

      ctx.font = "bold 13px 'JetBrains Mono', monospace";
      ctx.fillStyle = cat.color + "55";
      ctx.textAlign = "center";
      ctx.fillText(cat.name, dx, dy - r - 8);
    }

    // ── 3. Edges (bezier curves) with role-based styles ──
    for (let i = 0; i < simEdges.length; i++) {
      const e = simEdges[i];
      const src = typeof e.source === "object" ? e.source : null;
      const tgt = typeof e.target === "object" ? e.target : null;
      if (!src || !tgt) continue;

      const methodInfo = METHOD_LOOKUP[e.method];
      const color = methodInfo ? methodInfo.color : "#888";

      const highlighted =
        active && (src.id === active || tgt.id === active);

      const { cx, cy } = ctrlPoint(src.x, src.y, tgt.x, tgt.y, i);

      const eType = e.type || "engine";
      const es = edgeStyle(eType);

      ctx.beginPath();
      ctx.moveTo(src.x, src.y);
      ctx.quadraticCurveTo(cx, cy, tgt.x, tgt.y);
      ctx.strokeStyle = highlighted ? color + "cc" : color + "1f";
      ctx.lineWidth = highlighted ? es.lineWidth + 0.5 : es.lineWidth;
      if (es.dash) {
        ctx.setLineDash(es.dash);
      } else {
        ctx.setLineDash([]);
      }
      ctx.stroke();
      ctx.setLineDash([]);
    }

    // ── 4. Node glows (hovered/selected) ──
    for (const n of nodes) {
      if (n.id !== hovered && n.id !== selected) continue;
      const r = nodeRadius(n.layer);
      const grad = ctx.createRadialGradient(n.x, n.y, r, n.x, n.y, r * 4);
      const mc = getMethodColor(n.primaryMethod);
      grad.addColorStop(0, mc + "44");
      grad.addColorStop(1, mc + "00");
      ctx.beginPath();
      ctx.arc(n.x, n.y, r * 4, 0, Math.PI * 2);
      ctx.fillStyle = grad;
      ctx.fill();
    }

    // ── 5. Open node pulse glows ──
    for (const n of nodes) {
      if (n.status !== "open") continue;
      const r = nodeRadius(n.layer);
      const pulseAlpha = 0.15 + 0.12 * Math.sin(now * 0.003);
      const predictedEngine = n.predicted?.engine;
      const pulseColor = predictedEngine ? getMethodColor(predictedEngine) : "#666";
      const grad = ctx.createRadialGradient(n.x, n.y, r, n.x, n.y, r * 3);
      grad.addColorStop(0, pulseColor + Math.round(pulseAlpha * 255).toString(16).padStart(2, "0"));
      grad.addColorStop(1, pulseColor + "00");
      ctx.beginPath();
      ctx.arc(n.x, n.y, r * 3, 0, Math.PI * 2);
      ctx.fillStyle = grad;
      ctx.fill();
    }

    // ── 6. Nodes ──
    for (const n of nodes) {
      const r = nodeRadius(n.layer);
      const mc = getMethodColor(n.primaryMethod);
      const dc = DOMAINS[n.domain]?.color || "#888";
      const connected = isConnected(n.id);
      const isActive = n.id === hovered || n.id === selected;
      const isOpen = n.status === "open";
      const isPartial = n.status === "partial";

      if (active && !connected) {
        // Dimmed node
        ctx.beginPath();
        ctx.arc(n.x, n.y, r, 0, Math.PI * 2);
        ctx.globalAlpha = 0.25;
        ctx.fillStyle = "#222";
        ctx.fill();
        ctx.strokeStyle = "#333";
        ctx.lineWidth = 2;
        ctx.setLineDash([]);
        ctx.stroke();
        ctx.globalAlpha = 1;
      } else if (isOpen) {
        // Open node: hollow circle, dashed domain ring in predicted engine color
        const predictedEngine = n.predicted?.engine;
        const openColor = predictedEngine ? getMethodColor(predictedEngine) : "#666";

        ctx.beginPath();
        ctx.arc(n.x, n.y, r, 0, Math.PI * 2);
        ctx.fillStyle = "#09090b";
        ctx.fill();

        ctx.beginPath();
        ctx.arc(n.x, n.y, r, 0, Math.PI * 2);
        ctx.strokeStyle = openColor;
        ctx.lineWidth = isActive ? 3 : 2;
        ctx.setLineDash([4, 3]);
        ctx.stroke();
        ctx.setLineDash([]);
      } else if (isPartial) {
        // Partial node: solid fill, arc ring with 60 degree gap at top
        ctx.beginPath();
        ctx.arc(n.x, n.y, r, 0, Math.PI * 2);
        ctx.fillStyle = mc;
        ctx.fill();

        // Draw arc from ~30deg to ~330deg (leaving 60deg gap at top, centered at -PI/2)
        ctx.beginPath();
        ctx.arc(n.x, n.y, r, -Math.PI / 2 + Math.PI / 6, -Math.PI / 2 + 11 * Math.PI / 6);
        ctx.strokeStyle = dc;
        ctx.lineWidth = isActive ? 3 : 2;
        ctx.setLineDash([]);
        ctx.stroke();
      } else {
        // Solved node: solid fill, solid domain ring
        ctx.beginPath();
        ctx.arc(n.x, n.y, r, 0, Math.PI * 2);
        ctx.fillStyle = mc;
        ctx.fill();
        ctx.strokeStyle = dc;
        ctx.lineWidth = isActive ? 3 : 2;
        ctx.setLineDash([]);
        ctx.stroke();
      }
    }

    ctx.restore();
  }, [
    width,
    height,
    nodes,
    simEdges,
    transform,
    hovered,
    selected,
    _tick,
    isConnected,
    pulseTime,
  ]);

  // ── HTML overlay for labels ────────────────────────────────────────────────
  const labels = useMemo(() => {
    if (transform.k < 0.5) return null;
    const active = hovered || selected;
    return nodes.map((n) => {
      const sx = n.x * transform.k + transform.x;
      const sy = n.y * transform.k + transform.y;
      const r = nodeRadius(n.layer) * transform.k;
      const isActive = n.id === hovered || n.id === selected;
      const connected = isConnected(n.id);
      const dimmed = active && !connected;

      return (
        <div
          key={n.id}
          className="absolute whitespace-nowrap"
          style={{
            left: sx,
            top: sy + r + 4,
            transform: "translateX(-50%)",
            fontFamily: "'JetBrains Mono', monospace",
            fontSize: 10,
            color: dimmed ? "#444" : isActive ? "#fff" : "#666",
            pointerEvents: "none",
            opacity: dimmed ? 0.25 : 1,
            transition: "color 0.15s, opacity 0.15s",
          }}
        >
          {truncate(problemByIdMap?.get(n.id)?.name || n.id)}
        </div>
      );
    });
  }, [nodes, transform, hovered, selected, _tick, isConnected]);

  return (
    <div ref={containerRef} className="relative w-full h-full overflow-hidden">
      <canvas
        ref={canvasRef}
        className="absolute inset-0"
        style={{ touchAction: "none" }}
      />
      <div
        ref={overlayRef}
        className="absolute inset-0 pointer-events-none overflow-hidden"
      >
        {labels}
      </div>
    </div>
  );
}
