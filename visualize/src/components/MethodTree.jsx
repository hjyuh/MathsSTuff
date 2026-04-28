import { useState, useMemo } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { METHOD_TREE, METHOD_CHILDREN, METHOD_LOOKUP } from "../data/methodTree.js";
import { DOMAINS, getProblemMethods } from "../data/problems.js";

// ── helpers ──

function hexAlpha(hex, alpha) {
  const a = Math.round(alpha * 255).toString(16).padStart(2, "0");
  return hex + a;
}

const ROLE_SYMBOLS = {
  scaffold: "\u25A3",
  engine: "\u2699",
  bridge: "\u27BF",
  closer: "\u22A3",
};

const ROLE_COLORS = {
  scaffold: "#0abde3",
  engine: "#ff9f43",
  bridge: "#4ecdc4",
  closer: "#a29bfe",
};

const STATUS_COLORS = {
  solved: "#4ecdc4",
  partial: "#feca57",
  open: "#ff6b6b",
};

/** Count problems matching a leaf method */
function useMethodCounts(problems) {
  return useMemo(() => {
    const leafCounts = {};
    const catCounts = {};
    for (const p of problems) {
      const methods = getProblemMethods(p);
      for (const m of methods) {
        leafCounts[m] = (leafCounts[m] || 0) + 1;
      }
    }
    for (const [catKey, children] of Object.entries(METHOD_CHILDREN)) {
      catCounts[catKey] = 0;
      for (const leaf of children) {
        catCounts[catKey] += leafCounts[leaf] || 0;
      }
    }
    return { leafCounts, catCounts };
  }, [problems]);
}

// ── styles ──

const labelStyle = {
  fontSize: 9,
  textTransform: "uppercase",
  letterSpacing: "0.1em",
  color: "#666",
  fontFamily: "JetBrains Mono, monospace",
  whiteSpace: "nowrap",
  lineHeight: 1,
  userSelect: "none",
};

const pillBase = {
  padding: "2px 10px",
  borderRadius: 4,
  fontSize: 11,
  fontFamily: "JetBrains Mono, monospace",
  cursor: "pointer",
  border: "1px solid #1a1a2a",
  background: "transparent",
  color: "#555",
  whiteSpace: "nowrap",
  lineHeight: "18px",
  display: "inline-flex",
  alignItems: "center",
  gap: 4,
  transition: "all 0.15s ease",
};

function pillActiveStyle(color) {
  return {
    ...pillBase,
    background: color + "33",
    borderColor: color + "80",
    color: color,
  };
}

function CountBadge({ count, color }) {
  return (
    <span
      style={{
        fontSize: 9,
        fontFamily: "JetBrains Mono, monospace",
        padding: "1px 5px",
        borderRadius: 3,
        background: hexAlpha(color, 0.12),
        color: hexAlpha(color, 0.7),
        marginLeft: "auto",
        flexShrink: 0,
      }}
    >
      {count}
    </span>
  );
}

function TogglePill({ label, active, onChange }) {
  return (
    <button
      style={{
        ...pillBase,
        ...(active
          ? {
              background: "rgba(255,255,255,0.10)",
              borderColor: "rgba(255,255,255,0.25)",
              color: "#ccc",
            }
          : {}),
        gap: 5,
      }}
      onClick={() => onChange(!active)}
    >
      <span
        style={{
          display: "inline-block",
          width: 10,
          height: 10,
          borderRadius: 2,
          border: active ? "1px solid rgba(255,255,255,0.4)" : "1px solid #444",
          background: active ? "rgba(255,255,255,0.25)" : "transparent",
          fontSize: 8,
          lineHeight: "10px",
          textAlign: "center",
        }}
      >
        {active ? "\u2713" : ""}
      </span>
      {label}
    </button>
  );
}

// ── main component ──

export default function MethodTree({
  problems,
  activePath,
  onNavigate,
  filterDomain,
  setFilterDomain,
  filterRole,
  setFilterRole,
  filterStatus,
  setFilterStatus,
  showEdges,
  setShowEdges,
  showLabels,
  setShowLabels,
  onAddProblem,
  onReset,
  onExport,
}) {
  const [expanded, setExpanded] = useState({});
  const { leafCounts, catCounts } = useMethodCounts(problems);

  const toggleExpand = (catKey) => {
    setExpanded((prev) => ({ ...prev, [catKey]: !prev[catKey] }));
  };

  const isActiveCategory = (catKey) =>
    activePath && activePath.length >= 1 && activePath[0] === catKey;

  const isActiveLeaf = (catKey, leafKey) =>
    activePath &&
    activePath.length >= 2 &&
    activePath[0] === catKey &&
    activePath[1] === leafKey;

  const handleCategoryClick = (catKey) => {
    if (isActiveCategory(catKey) && activePath.length === 1) {
      onNavigate(null);
    } else {
      onNavigate([catKey]);
    }
  };

  const handleLeafClick = (catKey, leafKey) => {
    if (isActiveLeaf(catKey, leafKey)) {
      onNavigate([catKey]);
    } else {
      onNavigate([catKey, leafKey]);
    }
  };

  return (
    <div
      style={{
        width: 260,
        flexShrink: 0,
        background: "#0f0f14",
        borderRight: "1px solid #1a1a2a",
        borderRadius: "0 0 0 0",
        display: "flex",
        flexDirection: "column",
        overflow: "hidden",
        fontFamily: "Inter, sans-serif",
      }}
    >
      {/* Scrollable tree area */}
      <div style={{ flex: 1, overflowY: "auto", padding: "12px 10px" }}>
        {/* Header */}
        <div
          style={{
            display: "flex",
            alignItems: "center",
            justifyContent: "space-between",
            marginBottom: 10,
          }}
        >
          <div
            style={{
              ...labelStyle,
              fontSize: 10,
            }}
          >
            Solution Methods
          </div>
          <button
            onClick={onAddProblem}
            style={{
              width: 22,
              height: 22,
              borderRadius: 4,
              border: "1px solid #1a1a2a",
              background: "transparent",
              color: "#666",
              fontSize: 14,
              fontFamily: "JetBrains Mono, monospace",
              cursor: "pointer",
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              padding: 0,
              lineHeight: 1,
              transition: "all 0.15s ease",
            }}
            onMouseEnter={(e) => {
              e.currentTarget.style.borderColor = "#4ecdc4";
              e.currentTarget.style.color = "#4ecdc4";
            }}
            onMouseLeave={(e) => {
              e.currentTarget.style.borderColor = "#1a1a2a";
              e.currentTarget.style.color = "#666";
            }}
            title="Add Problem"
          >
            +
          </button>
        </div>

        {/* All button */}
        <button
          onClick={() => onNavigate(null)}
          style={{
            display: "flex",
            alignItems: "center",
            gap: 6,
            width: "100%",
            padding: "5px 8px",
            borderRadius: 4,
            border: "none",
            background: activePath === null ? "rgba(255,255,255,0.08)" : "transparent",
            color: activePath === null ? "#fff" : "#888",
            fontSize: 12,
            fontFamily: "Inter, sans-serif",
            cursor: "pointer",
            textAlign: "left",
            marginBottom: 4,
            transition: "background 0.15s",
          }}
        >
          All
          <CountBadge count={problems.length} color="#888" />
        </button>

        {/* Category tree */}
        {Object.entries(METHOD_TREE).map(([catKey, cat]) => {
          const isExpanded = expanded[catKey] || isActiveCategory(catKey);
          const children = METHOD_CHILDREN[catKey] || [];
          const catActive = isActiveCategory(catKey) && activePath.length === 1;

          return (
            <div key={catKey} style={{ marginBottom: 2 }}>
              {/* Category row */}
              <div
                style={{
                  display: "flex",
                  alignItems: "center",
                  gap: 4,
                  padding: "4px 4px 4px 0",
                  borderRadius: 4,
                  background: catActive ? hexAlpha(cat.color, 0.08) : "transparent",
                  transition: "background 0.15s",
                }}
              >
                {/* Chevron */}
                <button
                  onClick={(e) => {
                    e.stopPropagation();
                    toggleExpand(catKey);
                  }}
                  style={{
                    width: 20,
                    height: 20,
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                    background: "transparent",
                    border: "none",
                    color: "#666",
                    cursor: "pointer",
                    fontSize: 10,
                    padding: 0,
                    flexShrink: 0,
                    transition: "transform 0.15s",
                    transform: isExpanded ? "rotate(90deg)" : "rotate(0deg)",
                  }}
                >
                  &#9656;
                </button>

                {/* Colored dot */}
                <span
                  style={{
                    width: 8,
                    height: 8,
                    borderRadius: "50%",
                    background: cat.color,
                    flexShrink: 0,
                  }}
                />

                {/* Category name — clickable */}
                <button
                  onClick={() => handleCategoryClick(catKey)}
                  style={{
                    flex: 1,
                    background: "transparent",
                    border: "none",
                    color: catActive ? cat.color : "#bbb",
                    fontSize: 12,
                    fontFamily: "Inter, sans-serif",
                    cursor: "pointer",
                    textAlign: "left",
                    padding: "2px 0",
                    fontWeight: catActive ? 600 : 400,
                  }}
                >
                  {cat.name}
                </button>

                <CountBadge count={catCounts[catKey] || 0} color={cat.color} />
              </div>

              {/* Children (expanded) */}
              <AnimatePresence initial={false}>
                {isExpanded && (
                  <motion.div
                    key={catKey + "-children"}
                    initial={{ height: 0, opacity: 0 }}
                    animate={{ height: "auto", opacity: 1 }}
                    exit={{ height: 0, opacity: 0 }}
                    transition={{ duration: 0.2, ease: "easeInOut" }}
                    style={{ overflow: "hidden" }}
                  >
                    {children.map((leafKey) => {
                      const leaf = METHOD_LOOKUP[leafKey];
                      if (!leaf) return null;
                      const leafActive = isActiveLeaf(catKey, leafKey);

                      return (
                        <button
                          key={leafKey}
                          onClick={() => handleLeafClick(catKey, leafKey)}
                          style={{
                            display: "flex",
                            alignItems: "center",
                            gap: 6,
                            width: "100%",
                            padding: "4px 8px 4px 32px",
                            borderRadius: 4,
                            border: "none",
                            background: leafActive
                              ? hexAlpha(leaf.color, 0.1)
                              : "transparent",
                            color: leafActive ? leaf.color : "#888",
                            fontSize: 11,
                            fontFamily: "Inter, sans-serif",
                            cursor: "pointer",
                            textAlign: "left",
                            fontWeight: leafActive ? 600 : 400,
                            transition: "background 0.15s, color 0.15s",
                          }}
                        >
                          <span
                            style={{
                              width: 6,
                              height: 6,
                              borderRadius: "50%",
                              background: leaf.color,
                              flexShrink: 0,
                            }}
                          />
                          {leaf.name}
                          <CountBadge
                            count={leafCounts[leafKey] || 0}
                            color={leaf.color}
                          />
                        </button>
                      );
                    })}
                  </motion.div>
                )}
              </AnimatePresence>
            </div>
          );
        })}

        {/* ── Domain section ── */}
        <div style={{ marginTop: 16, borderTop: "1px solid #1a1a2a", paddingTop: 12 }}>
          <div style={{ ...labelStyle, marginBottom: 8, fontSize: 10 }}>
            Source Domain
          </div>
          <div style={{ display: "flex", flexWrap: "wrap", gap: 4 }}>
            <motion.button
              style={
                filterDomain === null
                  ? {
                      ...pillBase,
                      background: "rgba(255,255,255,0.12)",
                      borderColor: "rgba(255,255,255,0.3)",
                      color: "#fff",
                    }
                  : pillBase
              }
              onClick={() => setFilterDomain(null)}
              whileHover={{ scale: 1.04 }}
              whileTap={{ scale: 0.97 }}
              transition={{ type: "spring", stiffness: 500, damping: 30 }}
            >
              All
            </motion.button>
            {Object.entries(DOMAINS).map(([key, d]) => (
              <motion.button
                key={key}
                style={
                  filterDomain === key ? pillActiveStyle(d.color) : pillBase
                }
                onClick={() =>
                  setFilterDomain(filterDomain === key ? null : key)
                }
                whileHover={{ scale: 1.04 }}
                whileTap={{ scale: 0.97 }}
                transition={{ type: "spring", stiffness: 500, damping: 30 }}
              >
                {d.name}
              </motion.button>
            ))}
          </div>
        </div>

        {/* ── Role filter section ── */}
        <div style={{ marginTop: 16, borderTop: "1px solid #1a1a2a", paddingTop: 12 }}>
          <div style={{ ...labelStyle, marginBottom: 8, fontSize: 10 }}>
            Role
          </div>
          <div style={{ display: "flex", flexWrap: "wrap", gap: 4 }}>
            <motion.button
              style={
                filterRole === null
                  ? {
                      ...pillBase,
                      background: "rgba(255,255,255,0.12)",
                      borderColor: "rgba(255,255,255,0.3)",
                      color: "#fff",
                    }
                  : pillBase
              }
              onClick={() => setFilterRole(null)}
              whileHover={{ scale: 1.04 }}
              whileTap={{ scale: 0.97 }}
              transition={{ type: "spring", stiffness: 500, damping: 30 }}
            >
              All
            </motion.button>
            {Object.entries(ROLE_SYMBOLS).map(([role, symbol]) => (
              <motion.button
                key={role}
                style={
                  filterRole === role ? pillActiveStyle(ROLE_COLORS[role]) : pillBase
                }
                onClick={() =>
                  setFilterRole(filterRole === role ? null : role)
                }
                whileHover={{ scale: 1.04 }}
                whileTap={{ scale: 0.97 }}
                transition={{ type: "spring", stiffness: 500, damping: 30 }}
              >
                <span style={{ fontSize: 12 }}>{symbol}</span>
                <span style={{ textTransform: "capitalize" }}>{role}</span>
              </motion.button>
            ))}
          </div>
        </div>

        {/* ── Status filter section ── */}
        <div style={{ marginTop: 16, borderTop: "1px solid #1a1a2a", paddingTop: 12 }}>
          <div style={{ ...labelStyle, marginBottom: 8, fontSize: 10 }}>
            Status
          </div>
          <div style={{ display: "flex", flexWrap: "wrap", gap: 4 }}>
            <motion.button
              style={
                filterStatus === null
                  ? {
                      ...pillBase,
                      background: "rgba(255,255,255,0.12)",
                      borderColor: "rgba(255,255,255,0.3)",
                      color: "#fff",
                    }
                  : pillBase
              }
              onClick={() => setFilterStatus(null)}
              whileHover={{ scale: 1.04 }}
              whileTap={{ scale: 0.97 }}
              transition={{ type: "spring", stiffness: 500, damping: 30 }}
            >
              All
            </motion.button>
            {Object.entries(STATUS_COLORS).map(([status, color]) => (
              <motion.button
                key={status}
                style={
                  filterStatus === status ? pillActiveStyle(color) : pillBase
                }
                onClick={() =>
                  setFilterStatus(filterStatus === status ? null : status)
                }
                whileHover={{ scale: 1.04 }}
                whileTap={{ scale: 0.97 }}
                transition={{ type: "spring", stiffness: 500, damping: 30 }}
              >
                <span style={{ textTransform: "capitalize" }}>{status}</span>
              </motion.button>
            ))}
          </div>
        </div>

        {/* ── Toggles section ── */}
        <div style={{ marginTop: 16, borderTop: "1px solid #1a1a2a", paddingTop: 12 }}>
          <div style={{ ...labelStyle, marginBottom: 8, fontSize: 10 }}>
            Display
          </div>
          <div style={{ display: "flex", flexWrap: "wrap", gap: 4 }}>
            <TogglePill label="Edges" active={showEdges} onChange={setShowEdges} />
            <TogglePill label="Labels" active={showLabels} onChange={setShowLabels} />
          </div>
        </div>

        {/* ── Actions section ── */}
        <div style={{ marginTop: 16, borderTop: "1px solid #1a1a2a", paddingTop: 12 }}>
          <div style={{ display: "flex", flexDirection: "column", gap: 6 }}>
            <button
              onClick={onExport}
              style={{
                ...pillBase,
                width: "100%",
                justifyContent: "center",
                color: "#888",
              }}
              onMouseEnter={(e) => { e.currentTarget.style.color = "#ccc"; e.currentTarget.style.borderColor = "#333"; }}
              onMouseLeave={(e) => { e.currentTarget.style.color = "#888"; e.currentTarget.style.borderColor = "#1a1a2a"; }}
            >
              Export JSON
            </button>
            <button
              onClick={onReset}
              style={{
                ...pillBase,
                width: "100%",
                justifyContent: "center",
                color: "#ff6b6b88",
              }}
              onMouseEnter={(e) => { e.currentTarget.style.color = "#ff6b6b"; e.currentTarget.style.borderColor = "#ff6b6b44"; }}
              onMouseLeave={(e) => { e.currentTarget.style.color = "#ff6b6b88"; e.currentTarget.style.borderColor = "#1a1a2a"; }}
            >
              Reset to Defaults
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
