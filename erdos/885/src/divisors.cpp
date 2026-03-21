#include "divisors.hpp"

#include <algorithm>
#include <cstdint>
#include <vector>

#include "util.hpp"

namespace ep885 {

bool enumerate_divisors(
    const Factorization& fac,
    std::vector<std::uint64_t>& out,
    std::uint32_t max_divisors) {
    out.clear();
    out.push_back(1);

    for (std::size_t i = 0; i < fac.primes.size(); ++i) {
        const std::uint64_t p = fac.primes[i];
        const std::uint32_t e = fac.exps[i];

        const std::vector<std::uint64_t> cur = out;
        std::uint64_t pow = 1;

        for (std::uint32_t k = 1; k <= e; ++k) {
            if (pow > UINT64_MAX / p) {
                return false;
            }
            pow *= p;
            for (std::uint64_t d : cur) {
                if (out.size() >= max_divisors) {
                    return false;
                }
                out.push_back(d * pow);
            }
        }
    }
    return true;
}

std::vector<std::uint32_t> deltas_from_divisors(
    std::uint64_t n,
    const std::vector<std::uint64_t>& divisors,
    std::uint32_t delta_max) {
    std::vector<std::uint32_t> deltas;
    const std::uint64_t s = isqrt_u64(n);

    for (std::uint64_t a : divisors) {
        if (a == 0 || a > s || (n % a) != 0) {
            continue;
        }
        const std::uint64_t b = n / a;
        const std::uint64_t d = (b >= a) ? (b - a) : (a - b);
        if (d <= delta_max) {
            deltas.push_back(static_cast<std::uint32_t>(d));
        }
    }

    std::sort(deltas.begin(), deltas.end());
    deltas.erase(std::unique(deltas.begin(), deltas.end()), deltas.end());
    return deltas;
}

}  // namespace ep885

