#include <algorithm>
#include <atomic>
#include <bit>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
#include <numeric>
#include <optional>
#ifdef _OPENMP
#include <omp.h>
#endif
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

namespace {

using i64 = long long;
using u64 = std::uint64_t;
using i128 = __int128_t;

struct Options {
  int n_max = 10'000'000;
  std::string certificate_path = "erdos848_certificate_v4.tsv";
  bool quiet = false;
  int resume_n = 0;
};

struct RootInfo {
  int p = 0;
  int p2 = 0;
  int r_plus = 0;
  int r_minus = 0;
};

struct RootEvent {
  int n = 0;
  int p_index = -1;
};

struct BitMatrix {
  int rows = 0;
  int cols = 0;
  int words_per_row = 0;
  std::vector<u64> words;

  BitMatrix() = default;

  BitMatrix(int row_count, int col_count)
      : rows(row_count),
        cols(col_count),
        words_per_row((col_count + 63) / 64),
        words(static_cast<std::size_t>(row_count) * static_cast<std::size_t>((col_count + 63) / 64), 0) {}

  u64 *row_ptr(int row) {
    return words.data() + static_cast<std::size_t>(row) * static_cast<std::size_t>(words_per_row);
  }

  const u64 *row_ptr(int row) const {
    return words.data() + static_cast<std::size_t>(row) * static_cast<std::size_t>(words_per_row);
  }

  void set_bit(int row, int col) {
    row_ptr(row)[static_cast<std::size_t>(col) >> 6] |= (u64{1} << (col & 63));
  }

  bool test_bit(int row, int col) const {
    return ((row_ptr(row)[static_cast<std::size_t>(col) >> 6] >> (col & 63)) & u64{1}) != 0;
  }

  int prefix_popcount(int row, int length) const {
    if (length <= 0) {
      return 0;
    }
    if (length > cols) {
      length = cols;
    }
    const u64 *ptr = row_ptr(row);
    const int full_words = length >> 6;
    const int trailing_bits = length & 63;
    int total = 0;
    for (int i = 0; i < full_words; ++i) {
      total += std::popcount(ptr[i]);
    }
    if (trailing_bits != 0) {
      const u64 mask = (u64{1} << trailing_bits) - 1;
      total += std::popcount(ptr[full_words] & mask);
    }
    return total;
  }
};

struct PrimeBlockData {
  RootInfo root;
  std::vector<int> plus_values;
  std::vector<int> minus_values;
  BitMatrix plus_masks;
  BitMatrix minus_masks;
};

bool is_base_residue(int x) {
  const int r = x % 25;
  return r == 7 || r == 18;
}

std::optional<i64> modinv(i64 a, i64 m) {
  if (m == 1) {
    return 0;
  }
  a %= m;
  if (a < 0) {
    a += m;
  }
  i128 t = 0;
  i128 new_t = 1;
  i128 r = m;
  i128 new_r = a;
  while (new_r != 0) {
    const i128 q = r / new_r;
    const i128 next_t = t - q * new_t;
    t = new_t;
    new_t = next_t;
    const i128 next_r = r - q * new_r;
    r = new_r;
    new_r = next_r;
  }
  if (r != 1) {
    return std::nullopt;
  }
  t %= static_cast<i128>(m);
  if (t < 0) {
    t += static_cast<i128>(m);
  }
  return static_cast<i64>(t);
}

i64 mul_mod(i64 a, i64 b, i64 mod) {
  return static_cast<i64>((static_cast<i128>(a) * static_cast<i128>(b)) % static_cast<i128>(mod));
}

std::vector<int> sieve_primes(int limit) {
  std::vector<bool> is_prime(limit + 1, true);
  if (limit >= 0) {
    is_prime[0] = false;
  }
  if (limit >= 1) {
    is_prime[1] = false;
  }
  for (int i = 2; 1LL * i * i <= limit; ++i) {
    if (!is_prime[i]) {
      continue;
    }
    for (int j = i * i; j <= limit; j += i) {
      is_prime[j] = false;
    }
  }
  std::vector<int> primes;
  for (int i = 2; i <= limit; ++i) {
    if (is_prime[i]) {
      primes.push_back(i);
    }
  }
  return primes;
}

RootInfo hensel_root_prime_square(int p) {
  int r0 = -1;
  for (int r = 1; r < p; ++r) {
    if ((1LL * r * r + 1) % p == 0) {
      r0 = r;
      break;
    }
  }
  if (r0 < 0) {
    throw std::runtime_error("failed to find root mod p");
  }
  const i64 p2 = 1LL * p * p;
  const i64 t = ((1LL * r0 * r0 + 1) / p) % p;
  auto inv_opt = modinv((2LL * r0) % p, p);
  if (!inv_opt) {
    throw std::runtime_error("failed to invert derivative in hensel lift");
  }
  i64 k = (-t * *inv_opt) % p;
  if (k < 0) {
    k += p;
  }
  i64 r = r0 + k * p;
  r %= p2;
  if (r <= 0) {
    r += p2;
  }
  if (((r * r) + 1) % p2 != 0) {
    throw std::runtime_error("hensel lift verification failed");
  }
  return RootInfo{p, static_cast<int>(p2), static_cast<int>(r), static_cast<int>(p2 - r)};
}

std::vector<RootInfo> build_root_infos(int n_max) {
  const int limit = static_cast<int>(std::sqrt(static_cast<long double>(n_max))) + 5;
  const auto primes = sieve_primes(limit);
  std::vector<RootInfo> roots;
  for (int p : primes) {
    if (p < 13 || p % 4 != 1) {
      continue;
    }
    if (1LL * p * p > n_max) {
      break;
    }
    roots.push_back(hensel_root_prime_square(p));
  }
  return roots;
}

int least_witness_prime(int x, const std::vector<RootInfo> &roots, std::size_t up_to) {
  for (std::size_t i = 0; i <= up_to; ++i) {
    const auto &rt = roots[i];
    const int mod = x % rt.p2;
    if (mod == rt.r_plus || mod == rt.r_minus) {
      return rt.p;
    }
  }
  return 0;
}

std::vector<int> build_witness_values_for_root(
    int residue,
    int p2,
    int n_max,
    const std::vector<RootInfo> &roots,
    std::size_t p_index) {
  std::vector<int> values;
  for (int x = residue; x <= n_max; x += p2) {
    if (is_base_residue(x)) {
      continue;
    }
    if (least_witness_prime(x, roots, p_index) == roots[p_index].p) {
      values.push_back(x);
    }
  }
  return values;
}

std::vector<int> build_mask_primes(int n_max) {
  const i64 m_max = (n_max >= 7) ? ((n_max - 7) / 25 + 1LL) : 0LL;
  const i64 y_max = (m_max > 0) ? (7LL + 25LL * (m_max - 1)) : 0LL;
  const i64 max_value = static_cast<i64>(n_max) * y_max + 1;
  const int limit = static_cast<int>(std::sqrt(static_cast<long double>(max_value))) + 5;
  return sieve_primes(limit);
}

bool is_non_squarefree_value(i64 value, const std::vector<i64> &prime_squares) {
  for (i64 qq : prime_squares) {
    if (qq > value) {
      break;
    }
    if (value % qq == 0) {
      return true;
    }
  }
  return false;
}

void mark_progression_bits(u64 *row_words, int cols, i64 start, i64 step) {
  for (i64 idx = start; idx < cols; idx += step) {
    row_words[static_cast<std::size_t>(idx) >> 6] |= (u64{1} << (idx & 63));
  }
}

BitMatrix build_base_masks_for_values(
    const std::vector<int> &values,
    int m_max,
    const std::vector<int> &mask_primes,
    bool quiet,
    int p,
    const char *label) {
  BitMatrix matrix(static_cast<int>(values.size()), m_max);
  if (values.empty() || m_max == 0) {
    return matrix;
  }
  std::atomic<int> completed_rows{0};

#ifdef _OPENMP
#pragma omp parallel for schedule(dynamic, 8)
#endif
  for (int row = 0; row < static_cast<int>(values.size()); ++row) {
    const i64 x = values[static_cast<std::size_t>(row)];
    const i64 a = 25LL * x;
    const i64 b = 7LL * x + 1;
    const i64 max_value = x * (7LL + 25LL * (m_max - 1)) + 1;
    u64 *row_words = matrix.row_ptr(row);
    for (int q : mask_primes) {
      const i64 qq = 1LL * q * q;
      if (qq > max_value) {
        break;
      }
      const i64 g = std::gcd(a, qq);
      if (b % g != 0) {
        continue;
      }
      const i64 a1 = a / g;
      const i64 mod = qq / g;
      const i64 b1 = b / g;
      auto inv_opt = modinv(a1, mod);
      if (!inv_opt) {
        continue;
      }
      i64 r = ((-b1) % mod + mod) % mod;
      r = mul_mod(r, *inv_opt, mod);
      mark_progression_bits(row_words, m_max, r, mod);
    }
    if (!quiet) {
      const int done = completed_rows.fetch_add(1) + 1;
      if (done % 10000 == 0 || done == static_cast<int>(values.size())) {
#ifdef _OPENMP
#pragma omp critical
#endif
        {
          std::cerr << "[p=" << p << "] building masks " << label
                    << ": row " << done << "/" << values.size()
                    << " (" << (100 * done / std::max<int>(1, static_cast<int>(values.size()))) << "%)\n";
        }
      }
    }
  }

  if (!quiet) {
    std::cerr << "Built " << label << " base masks for p=" << p
              << " rows=" << values.size() << " cols=" << m_max << "\n";
  }
  return matrix;
}

PrimeBlockData build_prime_block_data(
    int n_max,
    int m_max,
    const std::vector<RootInfo> &roots,
    std::size_t p_index,
    const std::vector<int> &mask_primes,
    bool quiet) {
  PrimeBlockData block;
  block.root = roots[p_index];
  block.plus_values = build_witness_values_for_root(roots[p_index].r_plus, roots[p_index].p2, n_max, roots, p_index);
  block.minus_values = build_witness_values_for_root(roots[p_index].r_minus, roots[p_index].p2, n_max, roots, p_index);
  block.plus_masks = build_base_masks_for_values(block.plus_values, m_max, mask_primes, quiet, block.root.p, "+");
  block.minus_masks = build_base_masks_for_values(block.minus_values, m_max, mask_primes, quiet, block.root.p, "-");
  return block;
}

std::vector<RootEvent> build_global_root_events(int n_max, const std::vector<RootInfo> &roots) {
  std::vector<RootEvent> events;
  for (int pidx = 0; pidx < static_cast<int>(roots.size()); ++pidx) {
    const auto &rt = roots[static_cast<std::size_t>(pidx)];
    for (int x = rt.r_plus; x <= n_max; x += rt.p2) {
      events.push_back(RootEvent{x, pidx});
    }
    for (int x = rt.r_minus; x <= n_max; x += rt.p2) {
      events.push_back(RootEvent{x, pidx});
    }
  }
  std::sort(events.begin(), events.end(), [](const RootEvent &a, const RootEvent &b) {
    if (a.n != b.n) {
      return a.n < b.n;
    }
    return a.p_index < b.p_index;
  });
  return events;
}

std::vector<int> build_global_breakpoints(
    int n_max,
    int m_max,
    const std::vector<RootEvent> &global_root_events) {
  std::vector<int> breakpoints;
  breakpoints.reserve(static_cast<std::size_t>(m_max) + global_root_events.size() + 8);
  for (int m = 0; m < m_max; ++m) {
    breakpoints.push_back(7 + 25 * m);
  }
  for (const auto &ev : global_root_events) {
    if (ev.n >= 2 && ev.n <= n_max) {
      breakpoints.push_back(ev.n);
    }
  }
  std::sort(breakpoints.begin(), breakpoints.end());
  breakpoints.erase(std::unique(breakpoints.begin(), breakpoints.end()), breakpoints.end());
  return breakpoints;
}

void write_certificate_interval(
    std::ofstream &out,
    int start_n,
    int end_n,
    int margin,
    int worst_p) {
  if (start_n > end_n) {
    return;
  }
  for (int n = start_n; n <= end_n; ++n) {
    const int base_count = (n >= 7) ? ((n - 7) / 25 + 1) : 0;
    const char *status = (margin > 0) ? "PASS" : "FAIL";
    out << n << '\t' << status << '\t' << margin << '\t' << worst_p << '\t' << base_count << '\n';
    if (n % 10000 == 0 || n == end_n) {
      out.flush();
    }
  }
}

int read_last_certificate_n(const std::string &path) {
  std::ifstream in(path, std::ios::binary);
  if (!in) {
    throw std::runtime_error("resume requested but certificate file does not exist: " + path);
  }
  std::string line;
  int last_n = -1;
  while (std::getline(in, line)) {
    if (line.empty() || line[0] < '0' || line[0] > '9') {
      continue;
    }
    const auto tab = line.find('\t');
    if (tab == std::string::npos) {
      continue;
    }
    last_n = std::stoi(line.substr(0, tab));
  }
  if (last_n < 0) {
    throw std::runtime_error("resume requested but certificate file has no data rows: " + path);
  }
  return last_n;
}

Options parse_options(int argc, char **argv) {
  Options opts;
  for (int i = 1; i < argc; ++i) {
    const std::string arg = argv[i];
    if ((arg == "-n" || arg == "--n-max") && i + 1 < argc) {
      opts.n_max = std::stoi(argv[++i]);
    } else if ((arg == "-o" || arg == "--output") && i + 1 < argc) {
      opts.certificate_path = argv[++i];
    } else if (arg == "--resume" && i + 1 < argc) {
      opts.resume_n = std::stoi(argv[++i]);
    } else if (arg == "-q" || arg == "--quiet") {
      opts.quiet = true;
    } else {
      throw std::runtime_error("unknown argument: " + arg);
    }
  }
  return opts;
}

}  // namespace

int main(int argc, char **argv) {
  try {
    const Options opts = parse_options(argc, argv);
    if (opts.n_max < 2) {
      throw std::runtime_error("n_max must be at least 2");
    }
    if (opts.resume_n < 0 || opts.resume_n > opts.n_max) {
      throw std::runtime_error("resume value must satisfy 0 <= resume <= n_max");
    }

    const int m_max = (opts.n_max >= 7) ? ((opts.n_max - 7) / 25 + 1) : 0;
    if (!opts.quiet) {
      std::cerr << "Building primes and root data...\n";
    }
    const auto mask_primes = build_mask_primes(opts.n_max);
    std::vector<i64> prime_squares;
    prime_squares.reserve(mask_primes.size());
    for (int p : mask_primes) {
      prime_squares.push_back(1LL * p * p);
    }
    const auto roots = build_root_infos(opts.n_max);
    const auto global_root_events = build_global_root_events(opts.n_max, roots);
    const auto breakpoints = build_global_breakpoints(opts.n_max, m_max, global_root_events);
    const std::size_t resume_breakpoint_index = static_cast<std::size_t>(
        std::upper_bound(breakpoints.begin(), breakpoints.end(), opts.resume_n) - breakpoints.begin());
    const std::size_t resume_segment_index = resume_breakpoint_index;
    std::vector<int> best_segment_margin(breakpoints.size() + 1, std::numeric_limits<int>::max() / 4);
    std::vector<int> best_segment_p(breakpoints.size() + 1, 0);

    for (std::size_t p_index = 0; p_index < roots.size(); ++p_index) {
      const auto &root = roots[p_index];
      if (!opts.quiet) {
        std::cerr << "Preparing block p=" << root.p << " (" << (p_index + 1) << "/" << roots.size() << ")...\n";
      }

      PrimeBlockData block = build_prime_block_data(opts.n_max, m_max, roots, p_index, mask_primes, opts.quiet);
      if (!opts.quiet) {
        std::cerr << "Sweeping block p=" << root.p
                  << " outsiders+=" << block.plus_values.size()
                  << " -=" << block.minus_values.size() << "\n";
      }

      std::vector<int> plus_exchange(block.plus_values.size(), 0);
      std::vector<int> minus_exchange(block.minus_values.size(), 0);
      std::vector<int> plus_degree(block.plus_values.size(), 0);
      std::vector<int> minus_degree(block.minus_values.size(), 0);

      int current_raw_plus = 0;
      int current_raw_minus = 0;
      int current_smax = 0;
      int current_dmax = 0;
      int current_active_witness = 0;
      int current_margin = std::numeric_limits<int>::max() / 4;
      int current_r_gt = 0;
      int current_base_count = 0;

      std::size_t next_plus_outsider = 0;
      std::size_t next_minus_outsider = 0;
      std::size_t next_global_root = 0;
      int next_base_index = 0;
      int next_base_n = (m_max > 0) ? 7 : std::numeric_limits<int>::max();
      int next_plus_raw_n = root.r_plus;
      int next_minus_raw_n = root.r_minus;
      if (next_plus_raw_n > opts.n_max) {
        next_plus_raw_n = std::numeric_limits<int>::max();
      }
      if (next_minus_raw_n > opts.n_max) {
        next_minus_raw_n = std::numeric_limits<int>::max();
      }
      int next_progress_breakpoint = 10000;
      int processed_recorded_breakpoints = 0;
      const int total_recorded_breakpoints = static_cast<int>(breakpoints.size() - resume_breakpoint_index);

      for (std::size_t breakpoint_index = 0; breakpoint_index < breakpoints.size(); ++breakpoint_index) {
        const int n = breakpoints[breakpoint_index];

        if (n == next_base_n) {
          ++current_base_count;
          const int base_index = current_base_count - 1;
          for (std::size_t i = 0; i < next_plus_outsider; ++i) {
            if (block.plus_masks.test_bit(static_cast<int>(i), base_index)) {
              ++plus_exchange[i];
              current_smax = std::max(current_smax, plus_exchange[i]);
            }
          }
          for (std::size_t i = 0; i < next_minus_outsider; ++i) {
            if (block.minus_masks.test_bit(static_cast<int>(i), base_index)) {
              ++minus_exchange[i];
              current_smax = std::max(current_smax, minus_exchange[i]);
            }
          }
          ++next_base_index;
          next_base_n = (next_base_index < m_max) ? (7 + 25 * next_base_index) : std::numeric_limits<int>::max();
        }

        if (n == next_plus_raw_n) {
          ++current_raw_plus;
          while (next_plus_outsider < block.plus_values.size() && block.plus_values[next_plus_outsider] == n) {
            const int row = static_cast<int>(next_plus_outsider);
            plus_exchange[next_plus_outsider] = block.plus_masks.prefix_popcount(row, current_base_count);
            current_smax = std::max(current_smax, plus_exchange[next_plus_outsider]);
            int degree = 0;
            for (std::size_t j = 0; j < next_minus_outsider; ++j) {
              const i64 value = 1LL * block.plus_values[next_plus_outsider] * block.minus_values[j] + 1;
              if (!is_non_squarefree_value(value, prime_squares)) {
                continue;
              }
              ++degree;
              ++minus_degree[j];
              current_dmax = std::max(current_dmax, minus_degree[j]);
            }
            plus_degree[next_plus_outsider] = degree;
            current_dmax = std::max(current_dmax, degree);
            ++current_active_witness;
            ++next_plus_outsider;
          }
          next_plus_raw_n += root.p2;
          if (next_plus_raw_n > opts.n_max) {
            next_plus_raw_n = std::numeric_limits<int>::max();
          }
        }

        if (n == next_minus_raw_n) {
          ++current_raw_minus;
          while (next_minus_outsider < block.minus_values.size() && block.minus_values[next_minus_outsider] == n) {
            const int row = static_cast<int>(next_minus_outsider);
            minus_exchange[next_minus_outsider] = block.minus_masks.prefix_popcount(row, current_base_count);
            current_smax = std::max(current_smax, minus_exchange[next_minus_outsider]);
            int degree = 0;
            for (std::size_t i = 0; i < next_plus_outsider; ++i) {
              const i64 value = 1LL * block.minus_values[next_minus_outsider] * block.plus_values[i] + 1;
              if (!is_non_squarefree_value(value, prime_squares)) {
                continue;
              }
              ++degree;
              ++plus_degree[i];
              current_dmax = std::max(current_dmax, plus_degree[i]);
            }
            minus_degree[next_minus_outsider] = degree;
            current_dmax = std::max(current_dmax, degree);
            ++current_active_witness;
            ++next_minus_outsider;
          }
          next_minus_raw_n += root.p2;
          if (next_minus_raw_n > opts.n_max) {
            next_minus_raw_n = std::numeric_limits<int>::max();
          }
        }

        while (next_global_root < global_root_events.size() && global_root_events[next_global_root].n == n) {
          if (global_root_events[next_global_root].p_index > static_cast<int>(p_index)) {
            ++current_r_gt;
          }
          ++next_global_root;
        }

        if (current_active_witness == 0) {
          current_margin = std::numeric_limits<int>::max() / 4;
        } else {
          const int v_p = std::max(current_raw_plus, current_raw_minus);
          const int lhs = current_smax + v_p + current_dmax + current_r_gt;
          current_margin = current_base_count - lhs;
        }
        if (breakpoint_index + 1 >= resume_segment_index &&
            current_margin < best_segment_margin[breakpoint_index + 1]) {
          best_segment_margin[breakpoint_index + 1] = current_margin;
          best_segment_p[breakpoint_index + 1] = root.p;
        }
        if (n > opts.resume_n) {
          ++processed_recorded_breakpoints;
          if (!opts.quiet && (processed_recorded_breakpoints >= next_progress_breakpoint ||
                              breakpoint_index + 1 == breakpoints.size())) {
            std::cerr << "[p=" << root.p << "] breakpoint " << processed_recorded_breakpoints
                      << "/" << total_recorded_breakpoints
                      << " (" << (100 * processed_recorded_breakpoints / std::max(1, total_recorded_breakpoints)) << "%)"
                      << " N=" << n
                      << " margin=" << current_margin << "\n";
            next_progress_breakpoint += 10000;
          }
        }
      }
    }

    const bool resuming = opts.resume_n > 0;
    if (resuming) {
      const int last_n = read_last_certificate_n(opts.certificate_path);
      if (last_n != opts.resume_n) {
        throw std::runtime_error("resume requested but certificate last N does not match resume value");
      }
    }

    std::ofstream out(
        opts.certificate_path,
        std::ios::binary | (resuming ? std::ios::app : std::ios::trunc));
    if (!out) {
      throw std::runtime_error("failed to open certificate output: " + opts.certificate_path);
    }
    if (!resuming) {
      out << "N\tstatus\tmargin\tworst_p\tM\n";
      out.flush();
    }

    const int write_start_n = std::max(2, opts.resume_n + 1);
    if (write_start_n <= opts.n_max) {
      if (breakpoints.empty()) {
        write_certificate_interval(out, write_start_n, opts.n_max, 1, 0);
      } else {
        std::size_t segment_index = static_cast<std::size_t>(
            std::upper_bound(breakpoints.begin(), breakpoints.end(), opts.resume_n) - breakpoints.begin());
        while (segment_index <= breakpoints.size()) {
          const int segment_start = (segment_index == 0) ? 2 : breakpoints[segment_index - 1];
          const int segment_end = (segment_index < breakpoints.size()) ? (breakpoints[segment_index] - 1) : opts.n_max;
          const int interval_start = std::max(write_start_n, segment_start);
          if (interval_start <= segment_end && interval_start <= opts.n_max) {
            if (segment_index == 0) {
              write_certificate_interval(out, interval_start, std::min(segment_end, opts.n_max), 1, 0);
            } else {
              const int base_count = (interval_start >= 7) ? ((interval_start - 7) / 25 + 1) : 0;
              const int margin = (best_segment_margin[segment_index] >= std::numeric_limits<int>::max() / 8)
                  ? (base_count + 1)
                  : best_segment_margin[segment_index];
              const int p = best_segment_p[segment_index];
              write_certificate_interval(out, interval_start, std::min(segment_end, opts.n_max), margin, p);
            }
          }
          if (segment_index == breakpoints.size()) {
            break;
          }
          ++segment_index;
        }
      }
    }

    const int final_base_count = (opts.n_max >= 7) ? ((opts.n_max - 7) / 25 + 1) : 0;
    int final_segment = 0;
    if (!breakpoints.empty()) {
      final_segment = static_cast<int>(breakpoints.size());
    }
    const int final_margin = (best_segment_margin[static_cast<std::size_t>(final_segment)] >= std::numeric_limits<int>::max() / 8)
        ? (final_base_count + 1)
        : best_segment_margin[static_cast<std::size_t>(final_segment)];
    const int final_p = best_segment_p[static_cast<std::size_t>(final_segment)];

    out.flush();
    std::cout << "Certificate written to " << opts.certificate_path << "\n";
    std::cout << "Final base count M(" << opts.n_max << ") = " << final_base_count << "\n";
    std::cout << "Worst active prime at N=" << opts.n_max << ": p=" << final_p
              << ", margin=" << final_margin << "\n";
    return (final_margin > 0) ? 0 : 1;
  } catch (const std::exception &ex) {
    std::cerr << "error: " << ex.what() << "\n";
    return 1;
  }
}
