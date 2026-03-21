#pragma once

#include <cstdint>
#include <vector>

namespace ep885 {

struct DeltaIndex {
    std::uint32_t delta_max = 0;
    std::vector<std::uint32_t> offsets;
    std::vector<std::uint32_t> ids;
    std::vector<std::uint32_t> support;
    std::vector<std::uint32_t> kept_deltas;
};

DeltaIndex build_delta_index(
    std::uint32_t delta_max,
    std::vector<std::uint64_t>& edges_packed);

std::vector<std::uint32_t> prune_deltas(
    const DeltaIndex& idx,
    std::uint32_t min_support);

}  // namespace ep885

