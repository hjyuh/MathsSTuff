#pragma once

#include <cstdint>
#include <string>

namespace ep885 {

std::uint64_t isqrt_u64(std::uint64_t x);
bool is_square_u64(std::uint64_t x, std::uint64_t* root = nullptr);
std::string now_utc_compact();

inline std::uint64_t pack_edge(std::uint32_t delta, std::uint32_t id) {
    return (std::uint64_t(delta) << 32) | std::uint64_t(id);
}

inline std::uint32_t edge_delta(std::uint64_t e) {
    return std::uint32_t(e >> 32);
}

inline std::uint32_t edge_id(std::uint64_t e) {
    return std::uint32_t(e & 0xffffffffULL);
}

}  // namespace ep885

