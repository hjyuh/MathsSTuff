import { useState, useEffect, useRef, useCallback } from "react";
import { motion, AnimatePresence } from "framer-motion";
import useSearch from "../hooks/useSearch.js";
import { DOMAINS, getPrimaryMethod } from "../data/problems.js";
import { METHOD_LOOKUP } from "../data/methodTree.js";

export default function SearchBar({ problems, onSelect }) {
  const [open, setOpen] = useState(false);
  const [query, setQuery] = useState("");
  const [highlightIdx, setHighlightIdx] = useState(0);
  const inputRef = useRef(null);
  const results = useSearch(query, problems);

  // Reset state when opening/closing
  const openModal = useCallback(() => {
    setQuery("");
    setHighlightIdx(0);
    setOpen(true);
  }, []);

  const closeModal = useCallback(() => setOpen(false), []);

  // Global keyboard shortcuts
  useEffect(() => {
    const handler = (e) => {
      // Cmd+K / Ctrl+K
      if ((e.metaKey || e.ctrlKey) && e.key === "k") {
        e.preventDefault();
        if (open) closeModal();
        else openModal();
        return;
      }
      // "/" when no input focused
      if (
        e.key === "/" &&
        !open &&
        document.activeElement?.tagName !== "INPUT" &&
        document.activeElement?.tagName !== "TEXTAREA"
      ) {
        e.preventDefault();
        openModal();
        return;
      }
      // Escape
      if (e.key === "Escape" && open) {
        e.preventDefault();
        closeModal();
      }
    };
    window.addEventListener("keydown", handler);
    return () => window.removeEventListener("keydown", handler);
  }, [open, openModal, closeModal]);

  // Autofocus input when modal opens
  useEffect(() => {
    if (open) {
      requestAnimationFrame(() => inputRef.current?.focus());
    }
  }, [open]);

  // Clamp highlight index when results change
  useEffect(() => {
    setHighlightIdx(0);
  }, [results.length, query]);

  const select = useCallback(
    (id) => {
      onSelect?.(id);
      closeModal();
    },
    [onSelect, closeModal]
  );

  const handleKeyDown = (e) => {
    if (e.key === "ArrowDown") {
      e.preventDefault();
      setHighlightIdx((i) => Math.min(i + 1, results.length - 1));
    } else if (e.key === "ArrowUp") {
      e.preventDefault();
      setHighlightIdx((i) => Math.max(i - 1, 0));
    } else if (e.key === "Enter" && results.length > 0) {
      e.preventDefault();
      select(results[highlightIdx].id);
    }
  };

  // ── Styles ──

  const backdropStyle = {
    position: "fixed",
    inset: 0,
    background: "rgba(0,0,0,0.5)",
    display: "flex",
    alignItems: "flex-start",
    justifyContent: "center",
    paddingTop: "15vh",
    zIndex: 9999,
  };

  const modalStyle = {
    width: 480,
    maxWidth: "90vw",
    background: "#0f0f14",
    border: "1px solid #1a1a2a",
    borderRadius: 12,
    overflow: "hidden",
    boxShadow: "0 25px 60px rgba(0,0,0,0.6)",
  };

  const inputStyle = {
    width: "100%",
    padding: "14px 16px",
    fontSize: 16,
    fontFamily: "'JetBrains Mono', monospace",
    background: "transparent",
    border: "none",
    borderBottom: "1px solid #1a1a2a",
    color: "#fff",
    outline: "none",
    boxSizing: "border-box",
  };

  const resultRowStyle = (isActive) => ({
    display: "flex",
    alignItems: "center",
    gap: 10,
    padding: "10px 16px",
    cursor: "pointer",
    background: isActive ? "rgba(255,255,255,0.06)" : "transparent",
    fontFamily: "'Inter', sans-serif",
    transition: "background 0.1s",
  });

  const dotStyle = (color) => ({
    width: 8,
    height: 8,
    borderRadius: "50%",
    background: color,
    flexShrink: 0,
  });

  const nameStyle = {
    color: "#fff",
    fontSize: 14,
    fontWeight: 500,
    whiteSpace: "nowrap",
    overflow: "hidden",
    textOverflow: "ellipsis",
  };

  const solverStyle = {
    color: "#666",
    fontSize: 13,
    whiteSpace: "nowrap",
    overflow: "hidden",
    textOverflow: "ellipsis",
    flexShrink: 1,
    minWidth: 0,
  };

  const badgeStyle = (color) => ({
    fontSize: 11,
    padding: "2px 6px",
    borderRadius: 4,
    background: color + "22",
    color: color,
    whiteSpace: "nowrap",
    flexShrink: 0,
    fontWeight: 500,
  });

  const noResultsStyle = {
    padding: "20px 16px",
    color: "#555",
    fontSize: 14,
    fontFamily: "'Inter', sans-serif",
    textAlign: "center",
  };

  const hintStyle = {
    padding: "16px",
    color: "#444",
    fontSize: 13,
    fontFamily: "'Inter', sans-serif",
    textAlign: "center",
  };

  return (
    <AnimatePresence>
      {open && (
        <motion.div
          key="search-backdrop"
          style={backdropStyle}
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          transition={{ duration: 0.15 }}
          onClick={(e) => {
            if (e.target === e.currentTarget) closeModal();
          }}
        >
          <motion.div
            key="search-modal"
            style={modalStyle}
            initial={{ opacity: 0, scale: 0.95, y: -10 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.95, y: -10 }}
            transition={{ duration: 0.15 }}
          >
            <input
              ref={inputRef}
              type="text"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              onKeyDown={handleKeyDown}
              placeholder="Search problems, methods, solvers..."
              style={inputStyle}
            />

            <div style={{ maxHeight: 360, overflowY: "auto" }}>
              {query.trim() === "" && (
                <div style={hintStyle}>
                  Type to search across problems, methods, and solvers
                </div>
              )}

              {query.trim() !== "" && results.length === 0 && (
                <div style={noResultsStyle}>No results</div>
              )}

              {results.map((p, i) => {
                const domainColor = DOMAINS[p.domain]?.color ?? "#888";
                const pm = getPrimaryMethod(p);
                const method = pm ? METHOD_LOOKUP[pm] : null;
                return (
                  <div
                    key={p.id}
                    style={resultRowStyle(i === highlightIdx)}
                    onClick={() => select(p.id)}
                    onMouseEnter={() => setHighlightIdx(i)}
                  >
                    <div style={dotStyle(domainColor)} />
                    <div style={nameStyle}>{p.name}</div>
                    <div style={{ flex: 1 }} />
                    <div style={solverStyle}>{p.solver}</div>
                    {method && (
                      <div style={badgeStyle(method.color)}>
                        {method.symbol} {method.name.split(" ")[0]}
                      </div>
                    )}
                  </div>
                );
              })}
            </div>
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
