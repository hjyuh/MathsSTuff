#include "util.hpp"

#include <chrono>
#include <cmath>
#include <ctime>
#include <iomanip>
#include <sstream>

namespace ep885 {

std::uint64_t isqrt_u64(std::uint64_t x) {
    std::uint64_t r = static_cast<std::uint64_t>(std::sqrt(static_cast<long double>(x)));
    while ((r + 1) > r && (r + 1) <= x / (r + 1)) {
        ++r;
    }
    while (r > 0 && r > x / r) {
        --r;
    }
    return r;
}

bool is_square_u64(std::uint64_t x, std::uint64_t* root) {
    const std::uint64_t r = isqrt_u64(x);
    if (r <= x / r && r * r == x) {
        if (root != nullptr) {
            *root = r;
        }
        return true;
    }
    return false;
}

std::string now_utc_compact() {
    using namespace std::chrono;
    const auto t = system_clock::to_time_t(system_clock::now());
    std::tm tm{};
#if defined(_WIN32)
    gmtime_s(&tm, &t);
#else
    gmtime_r(&t, &tm);
#endif
    std::ostringstream oss;
    oss << std::put_time(&tm, "%Y%m%dT%H%M%SZ");
    return oss.str();
}

}  // namespace ep885

