#pragma once

#include <cstdint>
#include <string>
#include <vector>

namespace ep885 {

struct StageAConfig {
    std::uint64_t X = 10'000'000'000ULL;
    std::uint32_t delta_max = 20'000;
    std::uint32_t min_support = 5;
    std::uint32_t target_k = 5;

    std::uint32_t m_max = 200'000;
    std::vector<std::uint32_t> primes = {2, 3, 5, 7, 11, 13, 17, 19};

    std::uint32_t max_candidates = 80'000;
    std::uint32_t max_divisors = 200'000;
    std::uint32_t threads = 1;

    std::uint32_t log_k4_min_support = 10;
    std::uint32_t log_k4_max_records = 50'000;
    std::uint32_t log_biclique_max_records = 10'000;

    std::string out_dir = "out_stageA";
};

}  // namespace ep885

