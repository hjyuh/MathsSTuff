import { useRef, useCallback, useMemo } from "react";
import { DOMAINS } from "../data/problems";

export default function MiniMap({ nodes, transform, width, height, onPan }) {
  const canvasRef = useRef(null);
  const MAP_W = 160;
  const MAP_H = height && width ? Math.round((MAP_W * height) / width) : 90;

  // Don't render when not zoomed in enough
  if (!transform || transform.k <= 1.2) return null;

  const scaleX = MAP_W / width;
  const scaleY = MAP_H / height;

  // Viewport rectangle in minimap coordinates
  const vx = (-transform.x / transform.k) * scaleX;
  const vy = (-transform.y / transform.k) * scaleY;
  const vw = (width / transform.k) * scaleX;
  const vh = (height / transform.k) * scaleY;

  const handleClick = useCallback(
    (e) => {
      const rect = e.currentTarget.getBoundingClientRect();
      const mx = e.clientX - rect.left;
      const my = e.clientY - rect.top;
      // Convert minimap coords to world coords
      const worldX = mx / scaleX;
      const worldY = my / scaleY;
      onPan?.(worldX, worldY);
    },
    [scaleX, scaleY, onPan]
  );

  const containerStyle = {
    width: MAP_W,
    height: MAP_H,
    background: "rgba(10, 10, 15, 0.9)",
    border: "1px solid #1a1a2a",
    borderRadius: 6,
    position: "relative",
    cursor: "pointer",
    overflow: "hidden",
  };

  const viewportStyle = {
    position: "absolute",
    left: Math.max(0, vx),
    top: Math.max(0, vy),
    width: Math.min(vw, MAP_W),
    height: Math.min(vh, MAP_H),
    border: "1px solid rgba(255,255,255,0.7)",
    borderRadius: 1,
    pointerEvents: "none",
    boxSizing: "border-box",
  };

  return (
    <div style={containerStyle} onClick={handleClick} ref={canvasRef}>
      {/* Nodes as tiny dots */}
      <svg
        width={MAP_W}
        height={MAP_H}
        style={{ position: "absolute", top: 0, left: 0 }}
      >
        {nodes?.map((n) => {
          const color = DOMAINS[n.domain]?.color ?? "#666";
          return (
            <circle
              key={n.id}
              cx={n.x * scaleX}
              cy={n.y * scaleY}
              r={2}
              fill={color}
            />
          );
        })}
      </svg>

      {/* Viewport rectangle */}
      <div style={viewportStyle} />
    </div>
  );
}
