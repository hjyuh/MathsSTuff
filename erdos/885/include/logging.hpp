#pragma once

#include <cstdint>
#include <fstream>
#include <string>
#include <vector>

#include "factor.hpp"

namespace ep885 {

struct LogPaths {
    std::string candidates_tsv;
    std::string bicliques_jsonl;
    std::string k4_jsonl;
    std::string stats_txt;
};

class Logger {
public:
    explicit Logger(const std::string& out_dir);

    const LogPaths& paths() const { return paths_; }

    void set_limits(std::uint32_t k4_max, std::uint32_t biclique_max);
    bool can_log_k4() const { return k4_count_ < k4_max_; }
    bool can_log_biclique() const { return biclique_count_ < biclique_max_; }

    void log_candidate(const Candidate& c);
    void log_stats_line(const std::string& line);
    void log_biclique(
        std::uint32_t k,
        const std::vector<std::uint32_t>& deltas,
        const std::vector<std::uint32_t>& n_ids,
        const std::vector<std::uint64_t>& n_values);
    void log_k4(
        const std::vector<std::uint32_t>& deltas4,
        std::uint32_t support,
        const std::vector<std::uint32_t>& sample_n_ids,
        const std::vector<std::uint64_t>& sample_n_values);

private:
    void ensure_dir_(const std::string& out_dir);

    LogPaths paths_;
    std::ofstream cand_;
    std::ofstream bic_;
    std::ofstream k4_;
    std::ofstream stats_;

    std::uint32_t k4_count_ = 0;
    std::uint32_t biclique_count_ = 0;
    std::uint32_t k4_max_ = 50'000;
    std::uint32_t biclique_max_ = 10'000;
};

}  // namespace ep885

