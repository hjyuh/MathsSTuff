#pragma once

#include <cstdint>
#include <vector>

#include "factor.hpp"

namespace ep885 {

std::vector<SmoothNumber> generate_smooth(
    std::uint64_t limit,
    const std::vector<std::uint32_t>& primes);

std::vector<Candidate> build_stageA_candidates(
    std::uint64_t X,
    std::uint32_t m_max,
    const std::vector<std::uint32_t>& primes,
    std::uint32_t max_candidates);

}  // namespace ep885

