#include "eclat.hpp"

#include <algorithm>

namespace ep885 {

EclatMiner::EclatMiner(
    const DeltaIndex& index,
    const std::vector<Candidate>& candidates,
    Logger& logger,
    EclatConfig cfg)
    : idx_(index), cand_(candidates), log_(logger), cfg_(cfg) {}

std::span<const std::uint32_t> EclatMiner::postings_(std::uint32_t delta) const {
    const auto a = idx_.offsets[delta];
    const auto b = idx_.offsets[delta + 1];
    return std::span<const std::uint32_t>(idx_.ids.data() + a, b - a);
}

void EclatMiner::intersect_sorted(
    std::span<const std::uint32_t> A,
    std::span<const std::uint32_t> B,
    std::vector<std::uint32_t>& out) {
    out.clear();
    if (A.size() > B.size()) {
        std::swap(A, B);
    }

    std::size_t i = 0;
    std::size_t j = 0;
    while (i < A.size() && j < B.size()) {
        const auto a = A[i];
        const auto b = B[j];
        if (a == b) {
            out.push_back(a);
            ++i;
            ++j;
        } else if (a < b) {
            ++i;
        } else {
            ++j;
        }
    }
}

void EclatMiner::report_biclique_(
    const std::vector<std::uint32_t>& deltas,
    const std::vector<std::uint32_t>& n_ids) {
    const std::size_t take = std::min<std::size_t>(n_ids.size(), cfg_.min_support);
    std::vector<std::uint32_t> ids(n_ids.begin(), n_ids.begin() + take);
    std::vector<std::uint64_t> vals;
    vals.reserve(take);
    for (const auto id : ids) {
        vals.push_back(cand_.at(id).n);
    }
    log_.log_biclique(cfg_.target_k, deltas, ids, vals);
}

void EclatMiner::dfs_(
    std::vector<std::uint32_t>& prefix,
    const std::vector<std::uint32_t>& inter,
    std::size_t start_idx) {
    if (inter.size() < cfg_.min_support) {
        return;
    }

    if (prefix.size() == cfg_.target_k) {
        if (log_.can_log_biclique()) {
            report_biclique_(prefix, inter);
        }
        return;
    }

    if (prefix.size() == 4 &&
        inter.size() >= cfg_.log_k4_min_support &&
        log_.can_log_k4()) {
        const std::size_t take = std::min<std::size_t>(inter.size(), 20);
        std::vector<std::uint32_t> sample_ids(inter.begin(), inter.begin() + take);
        std::vector<std::uint64_t> sample_vals;
        sample_vals.reserve(take);
        for (const auto id : sample_ids) {
            sample_vals.push_back(cand_.at(id).n);
        }
        log_.log_k4(prefix, static_cast<std::uint32_t>(inter.size()), sample_ids, sample_vals);
    }

    if (prefix.size() + (idx_.kept_deltas.size() - start_idx) < cfg_.target_k) {
        return;
    }

    for (std::size_t i = start_idx; i < idx_.kept_deltas.size(); ++i) {
        const std::uint32_t d = idx_.kept_deltas[i];
        const auto L = postings_(d);

        intersect_sorted(std::span<const std::uint32_t>(inter.data(), inter.size()), L, inter_buf_);
        if (inter_buf_.size() < cfg_.min_support) {
            continue;
        }

        prefix.push_back(d);
        const std::vector<std::uint32_t> next_inter = inter_buf_;
        dfs_(prefix, next_inter, i + 1);
        prefix.pop_back();
    }
}

void EclatMiner::run() {
    std::vector<std::uint32_t> prefix;
    prefix.reserve(cfg_.target_k);

    for (std::size_t i = 0; i < idx_.kept_deltas.size(); ++i) {
        const std::uint32_t d0 = idx_.kept_deltas[i];
        const auto L0 = postings_(d0);
        if (L0.size() < cfg_.min_support) {
            continue;
        }

        prefix.clear();
        prefix.push_back(d0);

        std::vector<std::uint32_t> inter(L0.begin(), L0.end());
        dfs_(prefix, inter, i + 1);
    }
}

}  // namespace ep885
