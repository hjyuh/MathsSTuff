import { useState, useEffect, useCallback, useMemo, useRef } from "react";
import { zoomIdentity } from "d3-zoom";
import { SEED_PROBLEMS, DOMAINS, getProblemMethods, computeEdges, buildProblemById } from "./data/problems.js";
import { METHOD_CATEGORIES } from "./data/methodTree.js";
import useForceGraph from "./hooks/useForceGraph.js";
import GraphCanvas from "./components/GraphCanvas.jsx";
import MethodTree from "./components/MethodTree.jsx";
import Breadcrumbs from "./components/Breadcrumbs.jsx";
import DetailPanel from "./components/DetailPanel.jsx";
import SearchBar from "./components/SearchBar.jsx";
import MiniMap from "./components/MiniMap.jsx";
import Legend from "./components/Legend.jsx";
import AddProblemModal from "./components/AddProblemModal.jsx";

const STORAGE_KEY = "problem-web-problems";
const METHODS_STORAGE_KEY = "problem-web-methods";

function loadProblems() {
  try {
    const saved = localStorage.getItem(STORAGE_KEY);
    if (saved) return JSON.parse(saved);
  } catch { /* ignore parse errors */ }
  return SEED_PROBLEMS;
}

export default function App() {
  const [problems, setProblems] = useState(loadProblems);
  const [showAddModal, setShowAddModal] = useState(false);

  // Persist problems to localStorage
  useEffect(() => {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(problems));
  }, [problems]);

  // Save empty custom methods key for future use
  useEffect(() => {
    if (!localStorage.getItem(METHODS_STORAGE_KEY)) {
      localStorage.setItem(METHODS_STORAGE_KEY, JSON.stringify({}));
    }
  }, []);

  // Dynamic edge computation
  const edges = useMemo(() => computeEdges(problems), [problems]);

  // Dynamic problemById map
  const problemByIdMap = useMemo(() => buildProblemById(problems), [problems]);

  // Unique counts for footer
  const methodCount = useMemo(
    () => new Set(problems.flatMap((p) => getProblemMethods(p))).size,
    [problems],
  );
  const domainCount = useMemo(
    () => new Set(problems.map((p) => p.domain)).size,
    [problems],
  );

  const [hovered, setHovered] = useState(null);
  const [selected, setSelected] = useState(null);
  const [activePath, setActivePath] = useState(null);
  const [filterDomain, setFilterDomain] = useState(null);
  const [filterRole, setFilterRole] = useState(null);
  const [filterStatus, setFilterStatus] = useState(null);
  const [showEdges, setShowEdges] = useState(true);
  const [showLabels, setShowLabels] = useState(true);

  // Container size for the graph area (reported by GraphCanvas ResizeObserver)
  const [graphSize, setGraphSize] = useState({ w: 800, h: 600 });
  const handleGraphResize = useCallback((w, h) => setGraphSize({ w, h }), []);

  // Ref for zoom control from parent
  const zoomRef = useRef(null);

  // Force simulation — lifted here so MiniMap + GraphCanvas share state
  const {
    nodes,
    edges: simEdges,
    simulation,
    transform,
    setTransform,
    _tick,
  } = useForceGraph({
    problems,
    edges,
    width: graphSize.w,
    height: graphSize.h,
    activePath,
    filterDomain,
    filterRole,
    filterStatus,
  });

  // Connected IDs for DetailPanel
  const connectedIds = useMemo(() => {
    const active = selected || hovered;
    if (!active) return new Set();
    const ids = new Set();
    for (const e of edges) {
      if (e.source === active) ids.add(e.target);
      else if (e.target === active) ids.add(e.source);
    }
    return ids;
  }, [selected, hovered, edges]);

  // MiniMap pan handler
  const handleMiniMapPan = useCallback(
    (worldX, worldY) => {
      const k = transform.k;
      const newX = graphSize.w / 2 - worldX * k;
      const newY = graphSize.h / 2 - worldY * k;
      setTransform({ x: newX, y: newY, k });
    },
    [transform.k, graphSize.w, graphSize.h, setTransform],
  );

  // Keyboard shortcuts
  useEffect(() => {
    const handler = (e) => {
      // Escape: clear selection (SearchBar handles its own Escape)
      if (e.key === "Escape") {
        setSelected(null);
        setHovered(null);
      }
      // r: reset zoom
      if (
        e.key === "r" &&
        !e.metaKey &&
        !e.ctrlKey &&
        document.activeElement?.tagName !== "INPUT" &&
        document.activeElement?.tagName !== "TEXTAREA"
      ) {
        setTransform({ x: 0, y: 0, k: 1 });
        if (simulation.current) {
          simulation.current.alpha(0.3).restart();
        }
        // Also reset d3-zoom transform if available
        if (zoomRef.current) {
          const { zoom, selection } = zoomRef.current;
          selection.call(zoom.transform, zoomIdentity);
        }
      }
    };
    window.addEventListener("keydown", handler);
    return () => window.removeEventListener("keydown", handler);
  }, [setTransform, simulation]);

  // SearchBar select handler
  const handleSearchSelect = useCallback((id) => {
    setSelected(id);
  }, []);

  // Add problem handler
  const handleAddProblem = useCallback((problem) => {
    setProblems((prev) => [...prev, problem]);
  }, []);

  // Reset to defaults
  const handleReset = useCallback(() => {
    localStorage.removeItem(STORAGE_KEY);
    setProblems(SEED_PROBLEMS);
  }, []);

  // Export JSON
  const handleExport = useCallback(() => {
    const blob = new Blob([JSON.stringify(problems, null, 2)], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "problem-web-problems.json";
    a.click();
    URL.revokeObjectURL(url);
  }, [problems]);

  return (
    <div
      className="h-screen w-screen overflow-hidden flex flex-col"
      style={{ background: "#09090b" }}
    >
      {/* ── Main area: Sidebar + Graph + DetailPanel ── */}
      <div className="flex flex-1 min-h-0">
        {/* Sidebar */}
        <MethodTree
          problems={problems}
          activePath={activePath}
          onNavigate={setActivePath}
          filterDomain={filterDomain}
          setFilterDomain={setFilterDomain}
          filterRole={filterRole}
          setFilterRole={setFilterRole}
          filterStatus={filterStatus}
          setFilterStatus={setFilterStatus}
          showEdges={showEdges}
          setShowEdges={setShowEdges}
          showLabels={showLabels}
          setShowLabels={setShowLabels}
          onAddProblem={() => setShowAddModal(true)}
          onReset={handleReset}
          onExport={handleExport}
        />

        {/* Graph area */}
        <div className="relative flex-1 min-w-0">
          <Breadcrumbs activePath={activePath} onNavigate={setActivePath} />
          <GraphCanvas
            problems={problems}
            edges={edges}
            problemByIdMap={problemByIdMap}
            activePath={activePath}
            filterDomain={filterDomain}
            hovered={hovered}
            setHovered={setHovered}
            selected={selected}
            setSelected={setSelected}
            nodes={nodes}
            simEdges={simEdges}
            simulation={simulation}
            transform={transform}
            setTransform={setTransform}
            _tick={_tick}
            containerSize={graphSize}
            onContainerResize={handleGraphResize}
            zoomRef={zoomRef}
          />

          {/* MiniMap — bottom-left overlay */}
          <div className="absolute" style={{ bottom: 12, left: 12 }}>
            <MiniMap
              nodes={nodes}
              transform={transform}
              width={graphSize.w}
              height={graphSize.h}
              onPan={handleMiniMapPan}
            />
          </div>

          {/* Legend — bottom-right overlay */}
          <div className="absolute" style={{ bottom: 12, right: 12 }}>
            <Legend />
          </div>
        </div>

        {/* DetailPanel — right column */}
        <div className="flex-shrink-0 p-2" style={{ width: 336 }}>
          <DetailPanel
            problemId={selected || hovered}
            edges={edges}
            problemByIdMap={problemByIdMap}
            connectedIds={connectedIds}
            onSelectProblem={setSelected}
          />
        </div>
      </div>

      {/* ── Footer ── */}
      <div
        className="flex-shrink-0 flex items-center justify-center"
        style={{
          height: 28,
          fontFamily: "'JetBrains Mono', monospace",
          fontSize: 10,
          color: "#222",
          borderTop: "1px solid #1a1a2a",
        }}
      >
        Mahmoud &middot; March 2026 &middot; {problems.length} problems &middot;{" "}
        {methodCount} methods &middot; {domainCount} domains &middot;{" "}
        {edges.length} edges
      </div>

      {/* ── SearchBar overlay ── */}
      <SearchBar problems={problems} onSelect={handleSearchSelect} />

      {/* ── Add Problem Modal ── */}
      <AddProblemModal
        open={showAddModal}
        onClose={() => setShowAddModal(false)}
        onAdd={handleAddProblem}
      />
    </div>
  );
}
