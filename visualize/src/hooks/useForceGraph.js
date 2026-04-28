import { useRef, useState, useEffect, useMemo } from "react";
import * as d3Force from "d3-force";

import { METHOD_CHILDREN, getMethodPosition } from "../data/methodTree.js";
import { getProblemMethods, getPrimaryMethod, ROLE_KEYS } from "../data/problems.js";

export default function useForceGraph({
  problems,
  edges,
  width,
  height,
  activePath,
  filterDomain,
  filterRole,
  filterStatus,
}) {
  const simRef = useRef(null);
  const prevPositions = useRef(new Map());
  const [tick, setTick] = useState(0);
  const [transform, setTransform] = useState({ x: 0, y: 0, k: 1 });

  const filtered = useMemo(() => {
    let fp = problems;

    if (activePath && activePath.length === 1) {
      const children = METHOD_CHILDREN[activePath[0]] || [];
      fp = fp.filter((p) => getProblemMethods(p).some((m) => children.includes(m)));
    } else if (activePath && activePath.length >= 2) {
      const leafMethod = activePath[activePath.length - 1];
      if (filterRole) {
        // Only show problems where that method plays that specific role
        fp = fp.filter((p) => {
          const roleMethod = p.roles?.[filterRole] || p.predicted?.[filterRole];
          return roleMethod === leafMethod;
        });
      } else {
        fp = fp.filter((p) => getProblemMethods(p).includes(leafMethod));
      }
    }

    if (filterDomain) fp = fp.filter((p) => p.domain === filterDomain);
    if (filterStatus) fp = fp.filter((p) => p.status === filterStatus);

    const idSet = new Set(fp.map((p) => p.id));
    const fe = edges.filter(
      (e) => idSet.has(e.source) && idSet.has(e.target),
    );
    return { problems: fp, edges: fe };
  }, [problems, edges, activePath, filterDomain, filterRole, filterStatus]);

  useEffect(() => {
    if (!width || !height || filtered.problems.length === 0) {
      if (simRef.current) {
        simRef.current.stop();
        simRef.current = null;
      }
      return;
    }

    const nodes = filtered.problems.map((p) => {
      const prev = prevPositions.current.get(p.id);
      const primaryMethod = getPrimaryMethod(p);
      const pos = primaryMethod ? getMethodPosition(primaryMethod) : { x: 0.5, y: 0.5 };
      return {
        id: p.id,
        x: prev ? prev.x : pos.x * width + (Math.random() - 0.5) * 60,
        y: prev ? prev.y : pos.y * height + (Math.random() - 0.5) * 60,
        vx: prev ? prev.vx : 0,
        vy: prev ? prev.vy : 0,
        domain: p.domain,
        primaryMethod,
        allMethods: getProblemMethods(p),
        layer: p.layer,
        status: p.status,
        roles: p.roles,
        predicted: p.predicted,
      };
    });

    const linkData = filtered.edges.map((e) => ({
      source: e.source,
      target: e.target,
      method: e.method,
      type: e.type,
    }));

    if (simRef.current) simRef.current.stop();

    const sim = d3Force
      .forceSimulation(nodes)
      .force("center", d3Force.forceCenter(width / 2, height / 2).strength(0.03))
      .force("charge", d3Force.forceManyBody().strength(-120))
      .force(
        "link",
        d3Force
          .forceLink(linkData)
          .id((d) => d.id)
          .distance(180)
          .strength(0.3),
      )
      .force(
        "x",
        d3Force.forceX((d) => {
          const pos = d.primaryMethod ? getMethodPosition(d.primaryMethod) : { x: 0.5, y: 0.5 };
          return pos.x * width;
        }).strength(0.08),
      )
      .force(
        "y",
        d3Force.forceY((d) => {
          const pos = d.primaryMethod ? getMethodPosition(d.primaryMethod) : { x: 0.5, y: 0.5 };
          return pos.y * height;
        }).strength(0.08),
      )
      .force(
        "collide",
        d3Force.forceCollide((d) => Math.max(12, d.layer * 1.5)),
      )
      .alphaDecay(0.02)
      .velocityDecay(0.3)
      .stop(); // Don't use d3's internal rAF timer — we tick manually

    simRef.current = sim;

    // Manual tick loop via setInterval (works in background tabs + headless)
    const interval = setInterval(() => {
      if (sim.alpha() < sim.alphaMin()) {
        clearInterval(interval);
        return;
      }
      sim.tick();
      // Stash positions
      for (const n of sim.nodes()) {
        prevPositions.current.set(n.id, {
          x: n.x, y: n.y, vx: n.vx, vy: n.vy,
        });
      }
      setTick((t) => t + 1);
    }, 16); // ~60fps

    return () => {
      clearInterval(interval);
      sim.stop();
    };
  }, [filtered, width, height]);

  const nodes = simRef.current ? simRef.current.nodes() : [];
  const simEdges = useMemo(() => {
    if (!simRef.current) return [];
    const linkForce = simRef.current.force("link");
    return linkForce ? linkForce.links() : [];
  }, [tick]); // eslint-disable-line react-hooks/exhaustive-deps

  return {
    nodes,
    edges: simEdges,
    simulation: simRef,
    transform,
    setTransform,
    _tick: tick,
  };
}
