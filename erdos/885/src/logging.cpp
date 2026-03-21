#include "logging.hpp"

#include <filesystem>
#include <ostream>

namespace ep885 {

Logger::Logger(const std::string& out_dir) {
    ensure_dir_(out_dir);

    paths_.candidates_tsv = out_dir + "/candidates.tsv";
    paths_.bicliques_jsonl = out_dir + "/bicliques.jsonl";
    paths_.k4_jsonl = out_dir + "/k4.jsonl";
    paths_.stats_txt = out_dir + "/stats.txt";

    cand_.open(paths_.candidates_tsv, std::ios::out);
    bic_.open(paths_.bicliques_jsonl, std::ios::out);
    k4_.open(paths_.k4_jsonl, std::ios::out);
    stats_.open(paths_.stats_txt, std::ios::out);

    cand_ << "id\tn\ttau\tfactorization\n";
}

void Logger::set_limits(std::uint32_t k4_max, std::uint32_t biclique_max) {
    k4_max_ = k4_max;
    biclique_max_ = biclique_max;
}

void Logger::ensure_dir_(const std::string& out_dir) {
    std::filesystem::create_directories(out_dir);
}

void Logger::log_candidate(const Candidate& c) {
    cand_ << c.id << "\t" << c.n << "\t" << c.tau << "\t" << c.fac.to_string() << "\n";
}

void Logger::log_stats_line(const std::string& line) {
    stats_ << line << "\n";
    stats_.flush();
}

static void write_u32_array_json(std::ostream& os, const std::vector<std::uint32_t>& v) {
    os << "[";
    for (std::size_t i = 0; i < v.size(); ++i) {
        if (i > 0) {
            os << ",";
        }
        os << v[i];
    }
    os << "]";
}

static void write_u64_array_json(std::ostream& os, const std::vector<std::uint64_t>& v) {
    os << "[";
    for (std::size_t i = 0; i < v.size(); ++i) {
        if (i > 0) {
            os << ",";
        }
        os << v[i];
    }
    os << "]";
}

void Logger::log_biclique(
    std::uint32_t k,
    const std::vector<std::uint32_t>& deltas,
    const std::vector<std::uint32_t>& n_ids,
    const std::vector<std::uint64_t>& n_values) {
    if (!can_log_biclique()) {
        return;
    }
    ++biclique_count_;

    bic_ << "{"
         << "\"type\":\"biclique\","
         << "\"k\":" << k << ","
         << "\"support\":" << n_ids.size() << ","
         << "\"deltas\":";
    write_u32_array_json(bic_, deltas);
    bic_ << ",\"n_ids\":";
    write_u32_array_json(bic_, n_ids);
    bic_ << ",\"n_values\":";
    write_u64_array_json(bic_, n_values);
    bic_ << "}\n";
    bic_.flush();
}

void Logger::log_k4(
    const std::vector<std::uint32_t>& deltas4,
    std::uint32_t support,
    const std::vector<std::uint32_t>& sample_n_ids,
    const std::vector<std::uint64_t>& sample_n_values) {
    if (!can_log_k4()) {
        return;
    }
    ++k4_count_;

    k4_ << "{"
        << "\"type\":\"k4\","
        << "\"support\":" << support << ","
        << "\"deltas\":";
    write_u32_array_json(k4_, deltas4);
    k4_ << ",\"sample_n_ids\":";
    write_u32_array_json(k4_, sample_n_ids);
    k4_ << ",\"sample_n_values\":";
    write_u64_array_json(k4_, sample_n_values);
    k4_ << "}\n";
    k4_.flush();
}

}  // namespace ep885

