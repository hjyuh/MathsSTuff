#pragma once

#include <cstdint>
#include <sstream>
#include <string>
#include <vector>

namespace ep885 {

struct Factorization {
    std::vector<std::uint32_t> primes;
    std::vector<std::uint32_t> exps;

    std::uint32_t tau() const {
        std::uint64_t t = 1;
        for (std::size_t i = 0; i < exps.size(); ++i) {
            t *= std::uint64_t(exps[i]) + 1ULL;
            if (t > 0xffffffffULL) {
                return 0xffffffffU;
            }
        }
        return static_cast<std::uint32_t>(t);
    }

    std::string to_string() const {
        std::ostringstream oss;
        bool first = true;
        for (std::size_t i = 0; i < primes.size(); ++i) {
            if (i >= exps.size() || exps[i] == 0) {
                continue;
            }
            if (!first) {
                oss << "*";
            }
            first = false;
            oss << primes[i] << "^" << exps[i];
        }
        if (first) {
            return "1";
        }
        return oss.str();
    }
};

struct SmoothNumber {
    std::uint64_t value = 1;
    Factorization fac;
};

struct Candidate {
    std::uint32_t id = 0;
    std::uint64_t n = 0;
    Factorization fac;
    std::uint32_t tau = 0;
};

}  // namespace ep885

