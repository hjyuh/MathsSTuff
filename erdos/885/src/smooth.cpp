#include "smooth.hpp"

#include <algorithm>
#include <utility>

namespace ep885 {

static void dfs_smooth_(
    std::size_t i,
    std::uint64_t cur,
    const std::vector<std::uint32_t>& primes,
    std::uint64_t limit,
    Factorization& fac,
    std::vector<SmoothNumber>& out) {
    if (i == primes.size()) {
        SmoothNumber sn;
        sn.value = cur;
        sn.fac = fac;
        out.push_back(std::move(sn));
        return;
    }

    const std::uint32_t p = primes[i];
    std::uint64_t x = cur;
    std::uint32_t e = 0;

    fac.primes.resize(i + 1);
    fac.exps.resize(i + 1);
    fac.primes[i] = p;

    while (x <= limit) {
        fac.exps[i] = e;
        dfs_smooth_(i + 1, x, primes, limit, fac, out);
        if (x > limit / p) {
            break;
        }
        x *= p;
        ++e;
    }

    fac.primes.resize(i);
    fac.exps.resize(i);
}

std::vector<SmoothNumber> generate_smooth(
    std::uint64_t limit,
    const std::vector<std::uint32_t>& primes) {
    std::vector<SmoothNumber> out;
    Factorization fac;
    dfs_smooth_(0, 1, primes, limit, fac, out);

    std::sort(out.begin(), out.end(), [](const SmoothNumber& a, const SmoothNumber& b) {
        return a.value < b.value;
    });
    out.erase(std::unique(out.begin(), out.end(),
                          [](const SmoothNumber& a, const SmoothNumber& b) {
                              return a.value == b.value;
                          }),
              out.end());
    return out;
}

std::vector<Candidate> build_stageA_candidates(
    std::uint64_t X,
    std::uint32_t m_max,
    const std::vector<std::uint32_t>& primes,
    std::uint32_t max_candidates) {
    auto smooth = generate_smooth(m_max, primes);

    std::vector<Candidate> cands;
    cands.reserve(std::min<std::size_t>(smooth.size(), max_candidates));

    for (const auto& sn : smooth) {
        const std::uint64_t m = sn.value;
        if (m == 0 || m > X / m) {
            continue;
        }
        const std::uint64_t n = m * m;
        if (n > X) {
            continue;
        }

        Candidate c;
        c.n = n;
        c.fac.primes = sn.fac.primes;
        c.fac.exps = sn.fac.exps;
        for (auto& e : c.fac.exps) {
            e *= 2U;
        }
        c.tau = c.fac.tau();

        cands.push_back(std::move(c));
        if (cands.size() >= max_candidates) {
            break;
        }
    }

    std::sort(cands.begin(), cands.end(), [](const Candidate& a, const Candidate& b) {
        return a.n < b.n;
    });
    cands.erase(std::unique(cands.begin(), cands.end(),
                            [](const Candidate& a, const Candidate& b) {
                                return a.n == b.n;
                            }),
                cands.end());

    for (std::uint32_t i = 0; i < cands.size(); ++i) {
        cands[i].id = i;
    }
    return cands;
}

}  // namespace ep885

