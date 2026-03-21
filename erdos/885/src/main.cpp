#include <iostream>
#include <vector>

#include "config.hpp"
#include "delta_index.hpp"
#include "divisors.hpp"
#include "eclat.hpp"
#include "logging.hpp"
#include "smooth.hpp"
#include "util.hpp"

using namespace ep885;

int main() {
    StageAConfig cfg;

    Logger logger(cfg.out_dir);
    logger.set_limits(cfg.log_k4_max_records, cfg.log_biclique_max_records);

    logger.log_stats_line("run_id=" + now_utc_compact());
    logger.log_stats_line("X=" + std::to_string(cfg.X));
    logger.log_stats_line("delta_max=" + std::to_string(cfg.delta_max));
    logger.log_stats_line("min_support=" + std::to_string(cfg.min_support));
    logger.log_stats_line("target_k=" + std::to_string(cfg.target_k));
    logger.log_stats_line("m_max=" + std::to_string(cfg.m_max));
    logger.log_stats_line("max_candidates=" + std::to_string(cfg.max_candidates));

    auto candidates = build_stageA_candidates(
        cfg.X, cfg.m_max, cfg.primes, cfg.max_candidates);
    logger.log_stats_line("candidates=" + std::to_string(candidates.size()));

    for (const auto& c : candidates) {
        logger.log_candidate(c);
    }

    std::vector<std::uint64_t> edges;
    edges.reserve(static_cast<std::size_t>(candidates.size()) * 64);

    std::vector<std::uint64_t> divisors;
    std::uint32_t skipped_divisor_heavy = 0;

    for (const auto& c : candidates) {
        divisors.clear();
        if (!enumerate_divisors(c.fac, divisors, cfg.max_divisors)) {
            ++skipped_divisor_heavy;
            continue;
        }
        auto deltas = deltas_from_divisors(c.n, divisors, cfg.delta_max);
        for (std::uint32_t d : deltas) {
            edges.push_back(pack_edge(d, c.id));
        }
    }

    logger.log_stats_line("raw_edges=" + std::to_string(edges.size()));
    logger.log_stats_line("skipped_divisor_heavy=" + std::to_string(skipped_divisor_heavy));

    auto index = build_delta_index(cfg.delta_max, edges);
    index.kept_deltas = prune_deltas(index, cfg.min_support);

    logger.log_stats_line("unique_edges=" + std::to_string(index.ids.size()));
    logger.log_stats_line("kept_deltas=" + std::to_string(index.kept_deltas.size()));

    EclatConfig ecfg;
    ecfg.target_k = cfg.target_k;
    ecfg.min_support = cfg.min_support;
    ecfg.log_k4_min_support = cfg.log_k4_min_support;

    EclatMiner miner(index, candidates, logger, ecfg);
    miner.run();

    logger.log_stats_line("done=1");
    std::cerr << "Done. Outputs in: " << cfg.out_dir << "\n";
    return 0;
}

