import { DOMAINS, ROLE_KEYS, getProblemMethods, getPrimaryMethod } from "../data/problems";
import { METHOD_LOOKUP, getCategoryColor, getMethodColor } from "../data/methodTree.js";
import { motion, AnimatePresence } from "framer-motion";

/* ── shared micro-styles ── */

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

const STATUS_COLORS = {
  solved:      "#4ecdc4",
  partial:     "#feca57",
  open:        "#ff6b6b",
  contributed: "#ff9f43",
};

const ROLE_SYMBOLS = {
  scaffold: "▣",
  engine: "⚙",
  bridge: "⟿",
  closer: "⊣",
};

const ROLE_COLORS = {
  scaffold: "#0abde3",
  engine: "#ff9f43",
  bridge: "#4ecdc4",
  closer: "#a29bfe",
};

/* ── helpers ── */

function hexAlpha(hex, alpha) {
  const a = Math.round(alpha * 255).toString(16).padStart(2, "0");
  return hex + a;
}

function getConnected(problemId, edges) {
  const result = [];
  for (const e of edges) {
    if (e.source === problemId) result.push({ id: e.target, type: e.type });
    else if (e.target === problemId) result.push({ id: e.source, type: e.type });
  }
  return result;
}

function edgeTypeLabel(type) {
  switch (type) {
    case "engine": return "same engine";
    case "scaffold": return "same scaffold";
    case "bridge": return "same bridge";
    case "closer": return "same closer";
    case "cross-role": return "cross-role";
    default: return "shared method";
  }
}

/* ── sub-components ── */

function Badge({ color, children }) {
  return (
    <span
      style={{
        display: "inline-flex",
        alignItems: "center",
        gap: 3,
        fontSize: 10,
        fontFamily: "JetBrains Mono, monospace",
        padding: "2px 8px",
        borderRadius: 4,
        background: hexAlpha(color, 0.12),
        border: `1px solid ${hexAlpha(color, 0.25)}`,
        color: color,
        whiteSpace: "nowrap",
      }}
    >
      {children}
    </span>
  );
}

function StatusBadge({ status }) {
  const bg = STATUS_COLORS[status] || "#666";
  return (
    <span
      style={{
        display: "inline-flex",
        alignItems: "center",
        gap: 3,
        fontSize: 9,
        fontFamily: "JetBrains Mono, monospace",
        textTransform: "uppercase",
        padding: "2px 8px",
        borderRadius: 999,
        background: hexAlpha(bg, 0.2),
        color: bg,
        letterSpacing: "0.05em",
      }}
    >
      {status === "contributed" && (
        <span style={{ fontSize: 10 }}>&#9733;</span>
      )}
      {status}
    </span>
  );
}

function RoleRow({ role, methodKey, isPredicted }) {
  const info = METHOD_LOOKUP[methodKey];
  if (!info) return null;
  const roleColor = ROLE_COLORS[role] || "#888";
  const symbol = ROLE_SYMBOLS[role] || "?";

  return (
    <div
      style={{
        display: "flex",
        alignItems: "center",
        gap: 8,
        padding: "3px 0",
        fontStyle: isPredicted ? "italic" : "normal",
        opacity: isPredicted ? 0.7 : 1,
      }}
    >
      <span style={{ fontSize: 12, color: roleColor, width: 16, textAlign: "center" }}>
        {symbol}
      </span>
      <span
        style={{
          fontSize: 10,
          fontFamily: "JetBrains Mono, monospace",
          color: roleColor,
          textTransform: "capitalize",
          width: 60,
          flexShrink: 0,
        }}
      >
        {role}
      </span>
      <Badge color={info.color}>
        {info.symbol} {info.name}
      </Badge>
      {isPredicted && (
        <span style={{ fontSize: 8, color: "#666", fontFamily: "JetBrains Mono, monospace" }}>
          predicted
        </span>
      )}
    </div>
  );
}

function ProofArchitecture({ problem }) {
  const hasRoles = problem.roles && Object.keys(problem.roles).length > 0;
  const hasPredicted = problem.predicted && Object.keys(problem.predicted).length > 0;

  if (!hasRoles && !hasPredicted) return null;

  return (
    <div style={{ marginTop: 14 }}>
      <div style={{ ...labelStyle, marginBottom: 6 }}>
        Proof Architecture
      </div>
      <div style={{ display: "flex", flexDirection: "column", gap: 2 }}>
        {ROLE_KEYS.map((role) => {
          if (problem.roles?.[role]) {
            return <RoleRow key={role} role={role} methodKey={problem.roles[role]} isPredicted={false} />;
          }
          return null;
        })}
        {hasPredicted && ROLE_KEYS.map((role) => {
          if (problem.predicted?.[role] && !problem.roles?.[role]) {
            return <RoleRow key={"pred-" + role} role={role} methodKey={problem.predicted[role]} isPredicted={true} />;
          }
          return null;
        })}
      </div>
    </div>
  );
}

function BridgeDescription({ description }) {
  if (!description) return null;
  return (
    <div style={{ marginTop: 14 }}>
      <div style={{ ...labelStyle, marginBottom: 6 }}>
        Bridge Invariant
      </div>
      <div
        style={{
          fontSize: 11,
          color: "#999",
          fontFamily: "Inter, sans-serif",
          lineHeight: 1.5,
          fontStyle: "italic",
          paddingLeft: 8,
          borderLeft: "2px solid #4ecdc433",
        }}
      >
        {description}
      </div>
    </div>
  );
}

function FailedApproaches({ approaches }) {
  if (!approaches || approaches.length === 0) return null;
  return (
    <div style={{ marginTop: 14 }}>
      <div style={{ ...labelStyle, marginBottom: 6, color: "#ff6b6b99" }}>
        Tried &amp; Failed
      </div>
      <div style={{ display: "flex", flexDirection: "column", gap: 4 }}>
        {approaches.map((a, i) => (
          <div
            key={i}
            style={{
              fontSize: 11,
              color: "#888",
              fontFamily: "Inter, sans-serif",
              lineHeight: 1.4,
              paddingLeft: 10,
            }}
          >
            <span style={{ color: "#ff6b6b66", marginRight: 4 }}>&bull;</span>
            {a}
          </div>
        ))}
      </div>
    </div>
  );
}

function DifficultyBar({ layer, methodColor }) {
  return (
    <div style={{ marginTop: 12 }}>
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          marginBottom: 4,
        }}
      >
        <span style={{ ...labelStyle }}>Difficulty</span>
        <span
          style={{
            fontSize: 11,
            fontFamily: "JetBrains Mono, monospace",
            color: "#888",
          }}
        >
          {layer}/10
        </span>
      </div>
      <div
        style={{
          height: 5,
          borderRadius: 3,
          background: "#1a1a2a",
          overflow: "hidden",
        }}
      >
        <div
          style={{
            height: "100%",
            width: `${layer * 10}%`,
            borderRadius: 3,
            background: `linear-gradient(90deg, #4ecdc4, ${methodColor})`,
            transition: "width 0.4s ease",
          }}
        />
      </div>
    </div>
  );
}

function LinksSection({ links }) {
  const hasAny = links && (links.paper || links.forum || links.lean);

  return (
    <div style={{ marginTop: 14 }}>
      <div style={{ ...labelStyle, marginBottom: 6 }}>Links</div>
      {!hasAny ? (
        <span style={{ fontSize: 11, color: "#444", fontFamily: "Inter, sans-serif" }}>
          No links yet
        </span>
      ) : (
        <div style={{ display: "flex", gap: 10 }}>
          {links.paper ? (
            <a
              href={links.paper}
              target="_blank"
              rel="noreferrer"
              style={{ fontSize: 12, color: "#4ecdc4", textDecoration: "none" }}
            >
              Paper
            </a>
          ) : (
            <span style={{ fontSize: 12, color: "#333" }}>Paper</span>
          )}
          {links.forum ? (
            <a
              href={links.forum}
              target="_blank"
              rel="noreferrer"
              style={{ fontSize: 12, color: "#feca57", textDecoration: "none" }}
            >
              Forum
            </a>
          ) : (
            <span style={{ fontSize: 12, color: "#333" }}>Forum</span>
          )}
          {links.lean ? (
            <a
              href={links.lean}
              target="_blank"
              rel="noreferrer"
              style={{ fontSize: 12, color: "#a29bfe", textDecoration: "none" }}
            >
              Lean
            </a>
          ) : (
            <span style={{ fontSize: 12, color: "#333" }}>Lean</span>
          )}
        </div>
      )}
    </div>
  );
}

function ConnectedList({ problemId, edges, problemByIdMap, onSelectProblem }) {
  const connections = getConnected(problemId, edges);
  if (connections.length === 0) return null;

  // Group by type
  const grouped = {};
  for (const c of connections) {
    const label = edgeTypeLabel(c.type);
    if (!grouped[label]) grouped[label] = [];
    grouped[label].push(c.id);
  }

  return (
    <div style={{ marginTop: 14 }}>
      <div style={{ ...labelStyle, marginBottom: 6 }}>
        Connected Problems
      </div>
      <div
        style={{
          maxHeight: 160,
          overflowY: "auto",
          display: "flex",
          flexDirection: "column",
          gap: 6,
        }}
      >
        {Object.entries(grouped).map(([label, ids]) => (
          <div key={label}>
            <div style={{ fontSize: 9, color: "#555", fontFamily: "JetBrains Mono, monospace", marginBottom: 2, textTransform: "uppercase" }}>
              {label}
            </div>
            {ids.map((id) => {
              const p = problemByIdMap.get(id);
              if (!p) return null;
              const domainColor = DOMAINS[p.domain]?.color || "#888";
              return (
                <button
                  key={id}
                  onClick={() => onSelectProblem(id)}
                  style={{
                    display: "flex",
                    alignItems: "center",
                    gap: 6,
                    background: "transparent",
                    border: "none",
                    padding: "3px 4px",
                    borderRadius: 4,
                    cursor: "pointer",
                    textAlign: "left",
                    fontSize: 12,
                    fontFamily: "Inter, sans-serif",
                    color: "#ccc",
                    transition: "background 0.15s",
                    width: "100%",
                  }}
                  onMouseEnter={(e) =>
                    (e.currentTarget.style.background = "#1a1a2a")
                  }
                  onMouseLeave={(e) =>
                    (e.currentTarget.style.background = "transparent")
                  }
                >
                  <span
                    style={{
                      width: 6,
                      height: 6,
                      borderRadius: "50%",
                      background: domainColor,
                      flexShrink: 0,
                    }}
                  />
                  {p.name}
                </button>
              );
            })}
          </div>
        ))}
      </div>
    </div>
  );
}

function EmptyState() {
  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        height: "100%",
        gap: 12,
        padding: "40px 16px",
        textAlign: "center",
      }}
    >
      <span style={{ fontSize: 32, color: "#333", lineHeight: 1 }}>
        &#9671;
      </span>
      <span
        style={{
          fontSize: 12,
          color: "#555",
          fontFamily: "Inter, sans-serif",
          lineHeight: 1.5,
        }}
      >
        Select a node to explore connections
      </span>
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          gap: 4,
          fontSize: 10,
          color: "#444",
          fontFamily: "JetBrains Mono, monospace",
        }}
      >
        <span>fill = engine method</span>
        <span>ring = source domain</span>
        <span>edges = shared method</span>
      </div>
    </div>
  );
}

/* ── main component ── */

const panelTransition = { duration: 0.25, ease: "easeOut" };

export default function DetailPanel({
  problemId,
  edges,
  problemByIdMap,
  connectedIds,
  onSelectProblem,
}) {
  const problem = problemId ? problemByIdMap.get(problemId) : null;
  const domain = problem ? DOMAINS[problem.domain] : null;

  // Get primary method color
  const primaryMethod = problem ? getPrimaryMethod(problem) : null;
  const primaryMethodInfo = primaryMethod ? METHOD_LOOKUP[primaryMethod] : null;
  const primaryMethodColor = primaryMethodInfo ? primaryMethodInfo.color : "#888";

  return (
    <div
      style={{
        width: 320,
        flexShrink: 0,
        background: "#0f0f14",
        border: "1px solid #1a1a2a",
        borderRadius: 10,
        padding: 16,
        fontFamily: "Inter, sans-serif",
        display: "flex",
        flexDirection: "column",
        overflow: "hidden",
      }}
    >
      <AnimatePresence mode="wait">
        {problem ? (
          <motion.div
            key={problem.id}
            initial={{ opacity: 0, y: 8 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -8 }}
            transition={panelTransition}
            style={{ display: "flex", flexDirection: "column", overflowY: "auto", flex: 1 }}
          >
            {/* 1. Name */}
            <div
              style={{
                fontSize: 16,
                fontWeight: 700,
                color: "#fff",
                lineHeight: 1.3,
              }}
            >
              {problem.name}
            </div>

            {/* 2. Solver / Year / Prize */}
            <div
              style={{
                fontSize: 11,
                color: "#666",
                fontFamily: "JetBrains Mono, monospace",
                marginTop: 4,
              }}
            >
              {problem.solver && <>{problem.solver} &middot; </>}
              {problem.year || "Open"}
              {problem.prize && (
                <span style={{ color: "#feca57", marginLeft: 6 }}>
                  {problem.prize}
                </span>
              )}
              {problem.source && (
                <span style={{ color: "#ff9f43", marginLeft: 6 }}>
                  {problem.source}
                </span>
              )}
            </div>

            {/* 3. Domain badge + Status badge */}
            <div
              style={{
                display: "flex",
                flexWrap: "wrap",
                gap: 6,
                marginTop: 10,
              }}
            >
              {domain && <Badge color={domain.color}>{domain.name}</Badge>}
              <StatusBadge status={problem.status} />
            </div>

            {/* 4. Description */}
            <div
              style={{
                fontSize: 12,
                color: "#aaa",
                lineHeight: 1.6,
                marginTop: 10,
                fontFamily: "Inter, sans-serif",
              }}
            >
              {problem.desc}
            </div>

            {/* 5. Proof Architecture */}
            <ProofArchitecture problem={problem} />

            {/* 6. Bridge Description */}
            <BridgeDescription description={problem.bridge_description} />

            {/* 7. Failed Approaches (open problems) */}
            {problem.status === "open" && (
              <FailedApproaches approaches={problem.failed_approaches} />
            )}

            {/* 8. Difficulty bar */}
            <DifficultyBar
              layer={problem.layer}
              methodColor={primaryMethodColor}
            />

            {/* 9. Links */}
            <LinksSection links={problem.links} />

            {/* 10. Connected problems */}
            <ConnectedList
              problemId={problem.id}
              edges={edges}
              problemByIdMap={problemByIdMap}
              onSelectProblem={onSelectProblem}
            />
          </motion.div>
        ) : (
          <motion.div
            key="empty"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            transition={panelTransition}
          >
            <EmptyState />
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}
