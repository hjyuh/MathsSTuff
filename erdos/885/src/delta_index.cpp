#include "delta_index.hpp"

#include <algorithm>

#include "util.hpp"

namespace ep885 {

DeltaIndex build_delta_index(
    std::uint32_t delta_max,
    std::vector<std::uint64_t>& edges_packed) {
    DeltaIndex idx;
    idx.delta_max = delta_max;

    std::sort(edges_packed.begin(), edges_packed.end());
    edges_packed.erase(std::unique(edges_packed.begin(), edges_packed.end()), edges_packed.end());

    idx.offsets.assign(static_cast<std::size_t>(delta_max) + 2, 0);
    idx.support.assign(static_cast<std::size_t>(delta_max) + 1, 0);

    for (const auto e : edges_packed) {
        const std::uint32_t d = edge_delta(e);
        if (d <= delta_max) {
            idx.offsets[d + 1] += 1;
        }
    }

    for (std::uint32_t d = 0; d <= delta_max; ++d) {
        idx.offsets[d + 1] += idx.offsets[d];
    }

    idx.ids.assign(edges_packed.size(), 0);
    auto cursor = idx.offsets;

    for (const auto e : edges_packed) {
        const std::uint32_t d = edge_delta(e);
        if (d > delta_max) {
            continue;
        }
        idx.ids[cursor[d]] = edge_id(e);
        cursor[d] += 1;
    }

    for (std::uint32_t d = 0; d <= delta_max; ++d) {
        idx.support[d] = idx.offsets[d + 1] - idx.offsets[d];
    }

    return idx;
}

std::vector<std::uint32_t> prune_deltas(
    const DeltaIndex& idx,
    std::uint32_t min_support) {
    std::vector<std::uint32_t> kept;
    for (std::uint32_t d = 0; d <= idx.delta_max; ++d) {
        if (idx.support[d] >= min_support) {
            kept.push_back(d);
        }
    }

    std::sort(kept.begin(), kept.end(), [&](std::uint32_t a, std::uint32_t b) {
        if (idx.support[a] != idx.support[b]) {
            return idx.support[a] < idx.support[b];
        }
        return a < b;
    });
    return kept;
}

}  // namespace ep885

