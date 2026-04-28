import { useState, useCallback } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { DOMAINS } from "../data/problems.js";
import { METHOD_TREE, METHOD_CHILDREN, METHOD_LOOKUP } from "../data/methodTree.js";

// ── constants ──

const STEPS = ["Identity", "Domain", "Roles", "Details"];
const STATUS_OPTIONS = ["solved", "partial", "open"];
const ROLE_SLOTS = ["engine", "scaffold", "bridge", "closer"];

const ROLE_COLORS = {
  scaffold: "#0abde3",
  engine: "#ff9f43",
  bridge: "#4ecdc4",
  closer: "#a29bfe",
};

// Collect all leaf method keys
const ALL_LEAF_METHODS = [];
for (const catKey of Object.keys(METHOD_TREE)) {
  for (const leafKey of METHOD_CHILDREN[catKey]) {
    ALL_LEAF_METHODS.push(leafKey);
  }
}

// ── styles ──

const modalOverlay = {
  position: "fixed",
  inset: 0,
  background: "rgba(0,0,0,0.6)",
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
  zIndex: 9999,
};

const modalBox = {
  width: 520,
  maxWidth: "92vw",
  maxHeight: "85vh",
  background: "#0f0f14",
  border: "1px solid #1a1a2a",
  borderRadius: 12,
  overflow: "hidden",
  boxShadow: "0 25px 60px rgba(0,0,0,0.7)",
  display: "flex",
  flexDirection: "column",
};

const headerStyle = {
  padding: "16px 20px 0",
  fontFamily: "'JetBrains Mono', monospace",
};

const bodyStyle = {
  flex: 1,
  overflowY: "auto",
  padding: "16px 20px",
};

const footerStyle = {
  padding: "12px 20px",
  borderTop: "1px solid #1a1a2a",
  display: "flex",
  justifyContent: "space-between",
  alignItems: "center",
};

const labelStyle = {
  fontSize: 10,
  textTransform: "uppercase",
  letterSpacing: "0.08em",
  color: "#666",
  fontFamily: "JetBrains Mono, monospace",
  marginBottom: 6,
  display: "block",
};

const inputStyle = {
  width: "100%",
  padding: "8px 10px",
  fontSize: 13,
  fontFamily: "'JetBrains Mono', monospace",
  background: "#09090b",
  border: "1px solid #1a1a2a",
  borderRadius: 6,
  color: "#ddd",
  outline: "none",
  boxSizing: "border-box",
};

const chipBase = {
  padding: "3px 10px",
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

function chipActive(color) {
  return {
    ...chipBase,
    background: color + "33",
    borderColor: color + "80",
    color: color,
  };
}

const btnBase = {
  padding: "6px 16px",
  borderRadius: 6,
  fontSize: 12,
  fontFamily: "'JetBrains Mono', monospace",
  cursor: "pointer",
  border: "1px solid #1a1a2a",
  background: "transparent",
  color: "#888",
  transition: "all 0.15s ease",
};

const btnPrimary = {
  ...btnBase,
  background: "#4ecdc433",
  borderColor: "#4ecdc480",
  color: "#4ecdc4",
};

// ── slugify ──

function slugify(str) {
  return str
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "_")
    .replace(/^_+|_+$/g, "")
    .slice(0, 60);
}

// ── Step indicators ──

function StepIndicators({ current }) {
  return (
    <div style={{ display: "flex", gap: 8, marginBottom: 14 }}>
      {STEPS.map((label, i) => (
        <div
          key={label}
          style={{
            display: "flex",
            alignItems: "center",
            gap: 5,
          }}
        >
          <span
            style={{
              width: 20,
              height: 20,
              borderRadius: "50%",
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              fontSize: 10,
              fontFamily: "JetBrains Mono, monospace",
              fontWeight: 600,
              background: i === current ? "#4ecdc433" : i < current ? "#4ecdc422" : "#1a1a2a",
              color: i === current ? "#4ecdc4" : i < current ? "#4ecdc4aa" : "#555",
              border: i === current ? "1px solid #4ecdc480" : "1px solid transparent",
            }}
          >
            {i < current ? "\u2713" : i + 1}
          </span>
          <span
            style={{
              fontSize: 10,
              color: i === current ? "#ccc" : "#555",
              fontFamily: "JetBrains Mono, monospace",
            }}
          >
            {label}
          </span>
          {i < STEPS.length - 1 && (
            <span style={{ color: "#333", margin: "0 2px" }}>&mdash;</span>
          )}
        </div>
      ))}
    </div>
  );
}

// ── Step 0: Identity ──

function StepIdentity({ data, onChange }) {
  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 14 }}>
      <div>
        <label style={labelStyle}>Name *</label>
        <input
          style={inputStyle}
          value={data.name}
          onChange={(e) => onChange({ name: e.target.value })}
          placeholder="e.g. Green-Tao Theorem"
          autoFocus
        />
      </div>
      <div>
        <label style={labelStyle}>Status</label>
        <div style={{ display: "flex", gap: 6 }}>
          {STATUS_OPTIONS.map((s) => {
            const colors = { solved: "#4ecdc4", partial: "#feca57", open: "#ff6b6b" };
            const active = data.status === s;
            return (
              <button
                key={s}
                style={active ? chipActive(colors[s]) : chipBase}
                onClick={() => onChange({ status: s })}
              >
                <span style={{ textTransform: "capitalize" }}>{s}</span>
              </button>
            );
          })}
        </div>
      </div>
      <div>
        <label style={labelStyle}>Source (optional)</label>
        <input
          style={inputStyle}
          value={data.source}
          onChange={(e) => onChange({ source: e.target.value })}
          placeholder="IMO 2024 P3, arXiv:..."
        />
      </div>
    </div>
  );
}

// ── Step 1: Domain ──

function StepDomain({ data, onChange }) {
  return (
    <div>
      <label style={labelStyle}>What domain is the problem STATED in?</label>
      <div style={{ display: "flex", flexWrap: "wrap", gap: 6, marginTop: 8 }}>
        {Object.entries(DOMAINS).map(([key, d]) => (
          <button
            key={key}
            style={data.domain === key ? chipActive(d.color) : chipBase}
            onClick={() => onChange({ domain: key })}
          >
            <span
              style={{
                width: 6,
                height: 6,
                borderRadius: "50%",
                background: d.color,
                flexShrink: 0,
              }}
            />
            {d.name}
          </button>
        ))}
      </div>
    </div>
  );
}

// ── Step 2: Roles ──

function RoleSlot({ role, value, isOpen, onChange }) {
  const isEngine = role === "engine";
  const roleColor = ROLE_COLORS[role];
  const label = isOpen ? `${role} (Predicted)` : role;

  return (
    <div style={{ marginBottom: 12 }}>
      <div
        style={{
          display: "flex",
          alignItems: "center",
          gap: 6,
          marginBottom: 6,
        }}
      >
        <span
          style={{
            fontSize: 10,
            textTransform: "uppercase",
            letterSpacing: "0.08em",
            color: roleColor,
            fontFamily: "JetBrains Mono, monospace",
            fontWeight: isEngine ? 700 : 400,
          }}
        >
          {label}
          {isEngine && " (start here)"}
        </span>
      </div>
      <div style={{ display: "flex", flexWrap: "wrap", gap: 4 }}>
        <button
          style={!value ? chipActive("#555") : chipBase}
          onClick={() => onChange(null)}
        >
          skip
        </button>
        {ALL_LEAF_METHODS.map((leafKey) => {
          const info = METHOD_LOOKUP[leafKey];
          if (!info) return null;
          const active = value === leafKey;
          return (
            <button
              key={leafKey}
              style={active ? chipActive(info.color) : chipBase}
              onClick={() => onChange(leafKey)}
            >
              {info.symbol} {info.name.split("/")[0].trim()}
            </button>
          );
        })}
      </div>
    </div>
  );
}

function StepRoles({ data, onChange }) {
  const isOpen = data.status === "open";
  return (
    <div>
      {ROLE_SLOTS.map((role) => (
        <RoleSlot
          key={role}
          role={role}
          value={data.roles[role] || null}
          isOpen={isOpen}
          onChange={(val) =>
            onChange({
              roles: { ...data.roles, [role]: val },
            })
          }
        />
      ))}
      <div style={{ marginTop: 8 }}>
        <label style={labelStyle}>Bridge description (optional)</label>
        <input
          style={inputStyle}
          value={data.bridge_description}
          onChange={(e) => onChange({ bridge_description: e.target.value })}
          placeholder="How does the bridge connect domains?"
        />
      </div>
    </div>
  );
}

// ── Step 3: Details ──

function StepDetails({ data, onChange }) {
  const isOpen = data.status === "open";
  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 14 }}>
      <div>
        <label style={labelStyle}>One-line description *</label>
        <input
          style={inputStyle}
          value={data.desc}
          onChange={(e) => onChange({ desc: e.target.value })}
          placeholder="Dense sets contain 3-term APs..."
          autoFocus
        />
      </div>
      <div style={{ display: "flex", gap: 10 }}>
        <div style={{ flex: 1 }}>
          <label style={labelStyle}>Solver</label>
          <input
            style={inputStyle}
            value={data.solver}
            onChange={(e) => onChange({ solver: e.target.value })}
            placeholder="Green-Tao"
          />
        </div>
        <div style={{ width: 90 }}>
          <label style={labelStyle}>Year</label>
          <input
            style={inputStyle}
            type="number"
            value={data.year || ""}
            onChange={(e) => onChange({ year: e.target.value ? parseInt(e.target.value) : null })}
            placeholder="2024"
          />
        </div>
      </div>
      <div>
        <label style={labelStyle}>Difficulty (1-10): {data.layer}</label>
        <div style={{ display: "flex", gap: 4, marginTop: 4 }}>
          {[1, 2, 3, 4, 5, 6, 7, 8, 9, 10].map((n) => (
            <button
              key={n}
              style={{
                width: 28,
                height: 28,
                borderRadius: 4,
                border: data.layer === n ? "1px solid #4ecdc480" : "1px solid #1a1a2a",
                background: data.layer === n ? "#4ecdc433" : "#09090b",
                color: data.layer === n ? "#4ecdc4" : "#666",
                fontSize: 11,
                fontFamily: "JetBrains Mono, monospace",
                cursor: "pointer",
                padding: 0,
              }}
              onClick={() => onChange({ layer: n })}
            >
              {n}
            </button>
          ))}
        </div>
      </div>
      {isOpen && (
        <div>
          <label style={labelStyle}>Failed approaches</label>
          <input
            style={inputStyle}
            value={data.failed_approaches_text}
            onChange={(e) => onChange({ failed_approaches_text: e.target.value })}
            placeholder="Separate with semicolons..."
          />
        </div>
      )}
    </div>
  );
}

// ── Main modal ──

const INITIAL = {
  name: "",
  status: "solved",
  source: "",
  domain: "NT",
  roles: {},
  bridge_description: "",
  desc: "",
  solver: "",
  year: null,
  layer: 5,
  failed_approaches_text: "",
};

export default function AddProblemModal({ open, onClose, onAdd }) {
  const [step, setStep] = useState(0);
  const [data, setData] = useState(INITIAL);

  const update = useCallback((patch) => {
    setData((prev) => ({ ...prev, ...patch }));
  }, []);

  const reset = useCallback(() => {
    setStep(0);
    setData(INITIAL);
  }, []);

  const canNext = () => {
    if (step === 0) return data.name.trim().length > 0;
    if (step === 1) return !!data.domain;
    if (step === 2) return true;
    if (step === 3) return data.desc.trim().length > 0;
    return true;
  };

  const handleSubmit = () => {
    // Build roles and predicted
    const roles = {};
    const predicted = {};
    const isOpen = data.status === "open";

    for (const [role, val] of Object.entries(data.roles)) {
      if (val) {
        if (isOpen) {
          predicted[role] = val;
        } else {
          roles[role] = val;
        }
      }
    }

    const problem = {
      id: slugify(data.name),
      name: data.name.trim(),
      domain: data.domain,
      status: data.status,
      year: data.year || null,
      solver: data.solver || "",
      layer: data.layer,
      desc: data.desc.trim(),
      roles,
      ...(Object.keys(predicted).length > 0 ? { predicted } : {}),
      ...(data.bridge_description ? { bridge_description: data.bridge_description } : {}),
      ...(data.source ? { source: data.source } : {}),
      ...(isOpen && data.failed_approaches_text
        ? {
            failed_approaches: data.failed_approaches_text
              .split(";")
              .map((s) => s.trim())
              .filter(Boolean),
          }
        : {}),
      links: { paper: null, forum: null, lean: null },
    };

    onAdd(problem);
    reset();
    onClose();
  };

  const handleClose = () => {
    reset();
    onClose();
  };

  return (
    <AnimatePresence>
      {open && (
        <motion.div
          key="add-problem-backdrop"
          style={modalOverlay}
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          transition={{ duration: 0.15 }}
          onClick={(e) => {
            if (e.target === e.currentTarget) handleClose();
          }}
        >
          <motion.div
            key="add-problem-modal"
            style={modalBox}
            initial={{ opacity: 0, scale: 0.95, y: -10 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.95, y: -10 }}
            transition={{ duration: 0.15 }}
          >
            {/* Header */}
            <div style={headerStyle}>
              <div
                style={{
                  fontSize: 14,
                  fontWeight: 600,
                  color: "#ccc",
                  marginBottom: 12,
                }}
              >
                Add Problem
              </div>
              <StepIndicators current={step} />
            </div>

            {/* Body */}
            <div style={bodyStyle}>
              <AnimatePresence mode="wait">
                <motion.div
                  key={step}
                  initial={{ opacity: 0, x: 20 }}
                  animate={{ opacity: 1, x: 0 }}
                  exit={{ opacity: 0, x: -20 }}
                  transition={{ duration: 0.15 }}
                >
                  {step === 0 && <StepIdentity data={data} onChange={update} />}
                  {step === 1 && <StepDomain data={data} onChange={update} />}
                  {step === 2 && <StepRoles data={data} onChange={update} />}
                  {step === 3 && <StepDetails data={data} onChange={update} />}
                </motion.div>
              </AnimatePresence>
            </div>

            {/* Footer */}
            <div style={footerStyle}>
              <button
                style={btnBase}
                onClick={step === 0 ? handleClose : () => setStep((s) => s - 1)}
              >
                {step === 0 ? "Cancel" : "Back"}
              </button>
              <button
                style={{
                  ...btnPrimary,
                  opacity: canNext() ? 1 : 0.4,
                  pointerEvents: canNext() ? "auto" : "none",
                }}
                onClick={step === 3 ? handleSubmit : () => setStep((s) => s + 1)}
              >
                {step === 3 ? "Add Problem" : "Next"}
              </button>
            </div>
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
