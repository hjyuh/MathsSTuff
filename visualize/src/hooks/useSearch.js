import { useMemo } from "react";
import Fuse from "fuse.js";
import { DOMAINS, getProblemMethods } from "../data/problems.js";
import { METHOD_LOOKUP } from "../data/methodTree.js";

export default function useSearch(query, problems) {
  const fuse = useMemo(() => {
    if (!problems || problems.length === 0) return null;
    const enriched = problems.map((p) => ({
      ...p,
      domainName: DOMAINS[p.domain]?.name ?? "",
      methodName: getProblemMethods(p)
        .map((m) => METHOD_LOOKUP[m]?.name ?? "")
        .filter(Boolean)
        .join(" "),
    }));
    return new Fuse(enriched, {
      keys: ["name", "solver", "desc", "domainName", "methodName"],
      threshold: 0.4,
      includeScore: true,
    });
  }, [problems]);

  return useMemo(() => {
    if (!query || !query.trim() || !fuse) return [];
    return fuse
      .search(query.trim(), { limit: 12 })
      .map((r) => r.item);
  }, [query, fuse]);
}
