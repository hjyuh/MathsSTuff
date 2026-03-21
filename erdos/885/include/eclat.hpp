#pragma once

#include <cstdint>
#include <span>
#include <vector>

#include "delta_index.hpp"
#include "factor.hpp"
#include "logging.hpp"

namespace ep885 {

struct EclatConfig {
    std::uint32_t target_k = 5;
    std::uint32_t min_support = 5;
    std::uint32_t log_k4_min_support = 10;
};

class EclatMiner {
public:
    EclatMiner(
        const DeltaIndex& index,
        const std::vector<Candidate>& candidates,
        Logger& logger,
        EclatConfig cfg);

    void run();

private:
    const DeltaIndex& idx_;
    const std::vector<Candidate>& cand_;
    Logger& log_;
    EclatConfig cfg_;

    std::vector<std::uint32_t> inter_buf_;

    std::span<const std::uint32_t> postings_(std::uint32_t delta) const;

    static void intersect_sorted(
        std::span<const std::uint32_t> A,
        std::span<const std::uint32_t> B,
        std::vector<std::uint32_t>& out);

    void dfs_(
        std::vector<std::uint32_t>& prefix,
        const std::vector<std::uint32_t>& inter,
        std::size_t start_idx);

    void report_biclique_(
        const std::vector<std::uint32_t>& deltas,
        const std::vector<std::uint32_t>& n_ids);
};

}  // namespace ep885

