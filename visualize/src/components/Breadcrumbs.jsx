import { METHOD_TREE, METHOD_LOOKUP } from "../data/methodTree.js";

export default function Breadcrumbs({ activePath, onNavigate }) {
  if (!activePath || activePath.length === 0) return null;

  const segments = [];

  // "All" root
  segments.push({
    label: "All",
    color: "#888",
    onClick: () => onNavigate(null),
  });

  // Category level
  if (activePath.length >= 1) {
    const cat = METHOD_TREE[activePath[0]];
    segments.push({
      label: cat?.name || activePath[0],
      color: cat?.color || "#888",
      onClick: () => onNavigate([activePath[0]]),
    });
  }

  // Leaf level
  if (activePath.length >= 2) {
    const leaf = METHOD_LOOKUP[activePath[1]];
    segments.push({
      label: leaf?.name || activePath[1],
      color: leaf?.color || "#888",
      onClick: null, // current level, no click
    });
  }

  return (
    <div
      style={{
        position: "absolute",
        top: 0,
        left: 0,
        right: 0,
        height: 28,
        padding: "0 12px",
        display: "flex",
        alignItems: "center",
        gap: 0,
        fontFamily: "'JetBrains Mono', monospace",
        fontSize: 11,
        zIndex: 10,
        pointerEvents: "auto",
        background: "linear-gradient(to bottom, rgba(9,9,11,0.7) 0%, transparent 100%)",
      }}
    >
      {segments.map((seg, i) => {
        const isLast = i === segments.length - 1;
        return (
          <span key={i} style={{ display: "inline-flex", alignItems: "center" }}>
            {i > 0 && (
              <span style={{ color: "#444", margin: "0 6px", userSelect: "none" }}>
                &gt;
              </span>
            )}
            {isLast ? (
              <span style={{ color: "#ccc", userSelect: "none" }}>
                {seg.label}
              </span>
            ) : (
              <button
                onClick={seg.onClick}
                style={{
                  background: "transparent",
                  border: "none",
                  color: "#888",
                  cursor: "pointer",
                  padding: 0,
                  fontFamily: "'JetBrains Mono', monospace",
                  fontSize: 11,
                  transition: "color 0.15s",
                }}
                onMouseEnter={(e) => (e.currentTarget.style.color = "#bbb")}
                onMouseLeave={(e) => (e.currentTarget.style.color = "#888")}
              >
                {seg.label}
              </button>
            )}
          </span>
        );
      })}
    </div>
  );
}
