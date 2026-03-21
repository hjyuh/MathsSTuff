#pragma once

#include <cstdint>
#include <vector>

#include "factor.hpp"

namespace ep885 {

bool enumerate_divisors(
    const Factorization& fac,
    std::vector<std::uint64_t>& out,
    std::uint32_t max_divisors);

std::vector<std::uint32_t> deltas_from_divisors(
    std::uint64_t n,
    const std::vector<std::uint64_t>& divisors,
    std::uint32_t delta_max);

}  // namespace ep885

