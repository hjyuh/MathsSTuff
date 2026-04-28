import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";

const ITEMS = [
  "\u25CF fill = engine method",
  "\u25CB ring = source domain",
  "\u2014 solid edge = same engine",
  "--- dashed edge = same bridge",
  "\u00B7\u00B7\u00B7 dotted edge = same scaffold",
];

export default function Legend() {
  const [open, setOpen] = useState(false);

  const btnStyle = {
    width: 24,
    height: 24,
    borderRadius: 6,
    border: "1px solid #1a1a2a",
    background: "rgba(10, 10, 15, 0.85)",
    color: "#888",
    fontSize: 12,
    fontFamily: "'JetBrains Mono', monospace",
    cursor: "pointer",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    padding: 0,
    lineHeight: 1,
  };

  const panelStyle = {
    background: "rgba(10, 10, 15, 0.85)",
    border: "1px solid #1a1a2a",
    borderRadius: 6,
    padding: "8px 12px",
    fontFamily: "'JetBrains Mono', monospace",
    fontSize: 10,
    color: "#999",
    display: "flex",
    flexDirection: "column",
    gap: 4,
    whiteSpace: "nowrap",
  };

  return (
    <div style={{ display: "flex", flexDirection: "column", alignItems: "flex-end", gap: 4 }}>
      <button style={btnStyle} onClick={() => setOpen((v) => !v)}>
        ?
      </button>

      <AnimatePresence>
        {open && (
          <motion.div
            key="legend-panel"
            initial={{ opacity: 0, height: 0, overflow: "hidden" }}
            animate={{ opacity: 1, height: "auto", overflow: "hidden" }}
            exit={{ opacity: 0, height: 0, overflow: "hidden" }}
            transition={{ duration: 0.2, ease: "easeInOut" }}
          >
            <div style={panelStyle}>
              {ITEMS.map((item) => (
                <span key={item}>{item}</span>
              ))}
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}
