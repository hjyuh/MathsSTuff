#include <algorithm>
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

constexpr int kSmallPrimeLimit = 97;
constexpr int kBatchThreshold = 4096;
constexpr int kOmpBaseThreshold = 20000;

struct Options {
  int n_max = 10'000'000;
  std::string certificate_path = "erdos848_certificate_v2.tsv";
  bool quiet = false;
};

enum class EventType : std::uint8_t {
  Base = 0,
  RootPlus = 1,
  RootMinus = 2,
};

struct RootInfo {
  int p = 0;
  int p2 = 0;
  int r_plus = 0;
  int r_minus = 0;
};

struct WitnessRow {
  int x = 0;
  int exchange_count = 0;
  int degree = 0;
};

struct ResidueEntry {
  int residue = 0;
  int row_index = 0;
};

struct ResidueTable {
  int q = 0;
  int qq = 0;
  std::vector<ResidueEntry> entries;
  std::vector<int> base_targets;
};

struct WitnessSide {
  std::vector<int> witness_values;
  std::vector<WitnessRow> rows;
  std::vector<ResidueTable> small_tables;
  std::vector<int> marks;
  int mark_stamp = 0;
};

struct PrimeBlockState {
  RootInfo root;
  WitnessSide plus;
  WitnessSide minus;
  int current_raw_plus = 0;
  int current_raw_minus = 0;
  int current_smax = 0;
  int current_dmax = 0;
  int current_active_witness = 0;
  std::size_t next_plus_witness = 0;
  std::size_t next_minus_witness = 0;
  int current_margin = std::numeric_limits<int>::max() / 4;
};

struct Event {
  int n = 0;
  EventType type = EventType::Base;
  int p_index = -1;
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
  const i64 max_value = 25LL * n_max * ((n_max >= 7) ? ((n_max - 7) / 25 + 1LL) : 0LL);
  const int limit = static_cast<int>(std::sqrt(static_cast<long double>(max_value))) + 5;
  return sieve_primes(limit);
}

std::vector<int> build_small_primes(const std::vector<int> &mask_primes) {
  std::vector<int> small_primes;
  for (int p : mask_primes) {
    if (p > kSmallPrimeLimit) {
      break;
    }
    small_primes.push_back(p);
  }
  return small_primes;
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

bool is_non_squarefree_value_from(i64 value, const std::vector<i64> &prime_squares, std::size_t start_index) {
  for (std::size_t i = start_index; i < prime_squares.size(); ++i) {
    const i64 qq = prime_squares[i];
    if (qq > value) {
      break;
    }
    if (value % qq == 0) {
      return true;
    }
  }
  return false;
}

int count_non_squarefree_progression(i64 a, i64 b, int length, const std::vector<int> &primes) {
  if (length <= 0) {
    return 0;
  }
  const std::size_t word_count = static_cast<std::size_t>((length + 63) / 64);
  std::vector<u64> bits(word_count, 0);
  const i64 max_value = a * static_cast<i64>(length - 1) + b;
  for (int q : primes) {
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
    for (i64 n = r; n < length; n += mod) {
      bits[static_cast<std::size_t>(n) >> 6] |= (u64{1} << (n & 63));
    }
  }
  int total = 0;
  for (u64 word : bits) {
    total += std::popcount(word);
  }
  return total;
}

std::vector<ResidueTable> build_small_tables_for_values(
    const std::vector<int> &values,
    const std::vector<int> &small_primes) {
  std::vector<ResidueTable> tables;
  tables.reserve(small_primes.size());
  for (int q : small_primes) {
    ResidueTable table;
    table.q = q;
    table.qq = q * q;
    table.entries.reserve(values.size());
    for (int i = 0; i < static_cast<int>(values.size()); ++i) {
      table.entries.push_back(ResidueEntry{values[static_cast<std::size_t>(i)] % table.qq, i});
    }
    table.base_targets.resize(static_cast<std::size_t>(table.qq));
    for (int m = 0; m < table.qq; ++m) {
      const int y = (7 + static_cast<int>((25LL * m) % table.qq)) % table.qq;
      if (std::gcd(y, table.qq) != 1) {
        table.base_targets[static_cast<std::size_t>(m)] = -1;
        continue;
      }
      auto inv_opt = modinv(y, table.qq);
      if (!inv_opt) {
        table.base_targets[static_cast<std::size_t>(m)] = -1;
        continue;
      }
      table.base_targets[static_cast<std::size_t>(m)] = static_cast<int>((table.qq - *inv_opt) % table.qq);
    }
    std::sort(table.entries.begin(), table.entries.end(), [](const ResidueEntry &a, const ResidueEntry &b) {
      if (a.residue != b.residue) {
        return a.residue < b.residue;
      }
      return a.row_index < b.row_index;
    });
    tables.push_back(std::move(table));
  }
  return tables;
}

WitnessSide build_witness_side(const std::vector<int> &values, const std::vector<int> &small_primes) {
  WitnessSide side;
  side.witness_values = values;
  side.rows.resize(values.size());
  for (std::size_t i = 0; i < values.size(); ++i) {
    side.rows[i].x = values[i];
  }
  side.small_tables = build_small_tables_for_values(values, small_primes);
  side.marks.assign(values.size(), 0);
  return side;
}

std::vector<PrimeBlockState> build_prime_blocks(
    int n_max,
    bool quiet,
    const std::vector<int> &small_primes) {
  const auto roots = build_root_infos(n_max);
  std::vector<PrimeBlockState> blocks;
  blocks.reserve(roots.size());
  for (std::size_t i = 0; i < roots.size(); ++i) {
    PrimeBlockState block;
    block.root = roots[i];
    block.plus = build_witness_side(
        build_witness_values_for_root(roots[i].r_plus, roots[i].p2, n_max, roots, i),
        small_primes);
    block.minus = build_witness_side(
        build_witness_values_for_root(roots[i].r_minus, roots[i].p2, n_max, roots, i),
        small_primes);
    if (!quiet) {
      std::cerr << "Prepared p=" << block.root.p
                << " with witness outsiders +=" << block.plus.rows.size()
                << " -=" << block.minus.rows.size() << "\n";
    }
    blocks.push_back(std::move(block));
  }
  return blocks;
}

std::vector<Event> build_global_events(int n_max, const std::vector<PrimeBlockState> &blocks) {
  std::vector<Event> events;
  const int m_max = (n_max >= 7) ? ((n_max - 7) / 25 + 1) : 0;
  events.reserve(static_cast<std::size_t>(m_max) + 500000);
  for (int m = 0; m < m_max; ++m) {
    events.push_back(Event{7 + 25 * m, EventType::Base, -1});
  }
  for (int pidx = 0; pidx < static_cast<int>(blocks.size()); ++pidx) {
    const auto &rt = blocks[static_cast<std::size_t>(pidx)].root;
    for (int x = rt.r_plus; x <= n_max; x += rt.p2) {
      events.push_back(Event{x, EventType::RootPlus, pidx});
    }
    for (int x = rt.r_minus; x <= n_max; x += rt.p2) {
      events.push_back(Event{x, EventType::RootMinus, pidx});
    }
  }
  std::sort(events.begin(), events.end(), [](const Event &a, const Event &b) {
    if (a.n != b.n) {
      return a.n < b.n;
    }
    return static_cast<int>(a.type) < static_cast<int>(b.type);
  });
  return events;
}

void prepare_mark_pass(WitnessSide &side) {
  if (side.mark_stamp == std::numeric_limits<int>::max()) {
    std::fill(side.marks.begin(), side.marks.end(), 0);
    side.mark_stamp = 1;
  } else {
    ++side.mark_stamp;
  }
}

void collect_small_prime_hits(WitnessSide &side, int active_count, int y, std::vector<int> &touched) {
  if (active_count <= 0) {
    return;
  }
  for (const auto &table : side.small_tables) {
    if (y % table.q == 0) {
      continue;
    }
    auto inv_opt = modinv(y % table.qq, table.qq);
    if (!inv_opt) {
      continue;
    }
    const int residue = static_cast<int>((table.qq - *inv_opt) % table.qq);
    const auto begin = std::lower_bound(
        table.entries.begin(),
        table.entries.end(),
        residue,
        [](const ResidueEntry &entry, int value) { return entry.residue < value; });
    for (auto it = begin; it != table.entries.end() && it->residue == residue; ++it) {
      const int idx = it->row_index;
      if (idx >= active_count || side.marks[static_cast<std::size_t>(idx)] == side.mark_stamp) {
        continue;
      }
      side.marks[static_cast<std::size_t>(idx)] = side.mark_stamp;
      touched.push_back(idx);
    }
  }
}

void collect_small_prime_hits_for_base(
    WitnessSide &side,
    int active_count,
    int base_index,
    std::vector<int> &touched) {
  if (active_count <= 0) {
    return;
  }
  for (const auto &table : side.small_tables) {
    const int residue = table.base_targets[static_cast<std::size_t>(base_index % table.qq)];
    if (residue < 0) {
      continue;
    }
    const auto begin = std::lower_bound(
        table.entries.begin(),
        table.entries.end(),
        residue,
        [](const ResidueEntry &entry, int value) { return entry.residue < value; });
    for (auto it = begin; it != table.entries.end() && it->residue == residue; ++it) {
      const int idx = it->row_index;
      if (idx >= active_count || side.marks[static_cast<std::size_t>(idx)] == side.mark_stamp) {
        continue;
      }
      side.marks[static_cast<std::size_t>(idx)] = side.mark_stamp;
      touched.push_back(idx);
    }
  }
}

void handle_new_plus_witness(
    PrimeBlockState &block,
    int base_count,
    const std::vector<int> &mask_primes,
    const std::vector<i64> &prime_squares) {
  auto &row = block.plus.rows[block.next_plus_witness];
  row.exchange_count = count_non_squarefree_progression(25LL * row.x, 7LL * row.x + 1, base_count, mask_primes);
  row.degree = 0;
  for (std::size_t j = 0; j < block.next_minus_witness; ++j) {
    auto &opp = block.minus.rows[j];
    const i64 value = 1LL * row.x * opp.x + 1;
    if (!is_non_squarefree_value(value, prime_squares)) {
      continue;
    }
    ++row.degree;
    ++opp.degree;
    block.current_dmax = std::max(block.current_dmax, opp.degree);
  }
  block.current_smax = std::max(block.current_smax, row.exchange_count);
  block.current_dmax = std::max(block.current_dmax, row.degree);
  ++block.current_active_witness;
  ++block.next_plus_witness;
}

void handle_new_minus_witness(
    PrimeBlockState &block,
    int base_count,
    const std::vector<int> &mask_primes,
    const std::vector<i64> &prime_squares) {
  auto &row = block.minus.rows[block.next_minus_witness];
  row.exchange_count = count_non_squarefree_progression(25LL * row.x, 7LL * row.x + 1, base_count, mask_primes);
  row.degree = 0;
  for (std::size_t i = 0; i < block.next_plus_witness; ++i) {
    auto &opp = block.plus.rows[i];
    const i64 value = 1LL * row.x * opp.x + 1;
    if (!is_non_squarefree_value(value, prime_squares)) {
      continue;
    }
    ++row.degree;
    ++opp.degree;
    block.current_dmax = std::max(block.current_dmax, opp.degree);
  }
  block.current_smax = std::max(block.current_smax, row.exchange_count);
  block.current_dmax = std::max(block.current_dmax, row.degree);
  ++block.current_active_witness;
  ++block.next_minus_witness;
}

void advance_base_event(
    std::vector<PrimeBlockState> &blocks,
    int base_count,
    int y,
    const std::vector<i64> &prime_squares,
    const std::vector<i64> &large_prime_squares) {
#ifdef _OPENMP
#pragma omp parallel for if(base_count >= kOmpBaseThreshold && static_cast<int>(blocks.size()) >= 8) schedule(static)
#endif
  for (int block_index = 0; block_index < static_cast<int>(blocks.size()); ++block_index) {
    auto &block = blocks[static_cast<std::size_t>(block_index)];
    const auto advance_side = [&](WitnessSide &side) {
      const int active_count = static_cast<int>(&side == &block.plus ? block.next_plus_witness : block.next_minus_witness);
      if (active_count <= 0) {
        return;
      }
      if (active_count < kBatchThreshold) {
        for (int idx = 0; idx < active_count; ++idx) {
          auto &row = side.rows[static_cast<std::size_t>(idx)];
          const i64 value = 1LL * row.x * y + 1;
          if (!is_non_squarefree_value(value, prime_squares)) {
            continue;
          }
          ++row.exchange_count;
          block.current_smax = std::max(block.current_smax, row.exchange_count);
        }
        return;
      }
      std::vector<int> touched;
      prepare_mark_pass(side);
      collect_small_prime_hits_for_base(side, active_count, base_count - 1, touched);
      for (int idx = 0; idx < active_count; ++idx) {
        if (side.marks[static_cast<std::size_t>(idx)] == side.mark_stamp) {
          continue;
        }
        const i64 value = 1LL * side.rows[static_cast<std::size_t>(idx)].x * y + 1;
        if (!is_non_squarefree_value_from(value, large_prime_squares, 0)) {
          continue;
        }
        side.marks[static_cast<std::size_t>(idx)] = side.mark_stamp;
        touched.push_back(idx);
      }
      for (int idx : touched) {
        auto &row = side.rows[static_cast<std::size_t>(idx)];
        ++row.exchange_count;
        block.current_smax = std::max(block.current_smax, row.exchange_count);
      }
    };
    std::vector<int> touched;
    advance_side(block.plus);
    advance_side(block.minus);
  }
}

void recompute_current_margins(
    std::vector<PrimeBlockState> &blocks,
    int base_count,
    std::vector<int> &raw_total,
    std::vector<int> &suffix) {
  for (std::size_t i = 0; i < blocks.size(); ++i) {
    raw_total[i] = blocks[i].current_raw_plus + blocks[i].current_raw_minus;
  }
  suffix[blocks.size()] = 0;
  for (int i = static_cast<int>(blocks.size()) - 1; i >= 0; --i) {
    suffix[static_cast<std::size_t>(i)] = suffix[static_cast<std::size_t>(i + 1)] + raw_total[static_cast<std::size_t>(i)];
  }
  for (std::size_t i = 0; i < blocks.size(); ++i) {
    auto &block = blocks[i];
    if (block.current_active_witness == 0) {
      block.current_margin = std::numeric_limits<int>::max() / 4;
      continue;
    }
    const int v_p = std::max(block.current_raw_plus, block.current_raw_minus);
    const int lhs = block.current_smax + v_p + block.current_dmax + suffix[i + 1];
    block.current_margin = base_count - lhs;
  }
}

std::pair<int, int> worst_prime_and_margin(const std::vector<PrimeBlockState> &blocks, int base_count) {
  int best_p = 0;
  int best_margin = base_count + 1;
  bool found = false;
  for (const auto &block : blocks) {
    if (block.current_active_witness == 0) {
      continue;
    }
    if (!found || block.current_margin < best_margin) {
      found = true;
      best_margin = block.current_margin;
      best_p = block.root.p;
    }
  }
  return {best_p, best_margin};
}

void write_certificate_interval(std::ofstream &out, int start_n, int end_n, int worst_p, int margin, int base_count) {
  if (start_n > end_n) {
    return;
  }
  const char *status = (margin > 0) ? "PASS" : "FAIL";
  for (int n = start_n; n <= end_n; ++n) {
    out << n << '\t' << status << '\t' << margin << '\t' << worst_p << '\t' << base_count << '\n';
  }
}

Options parse_options(int argc, char **argv) {
  Options opts;
  for (int i = 1; i < argc; ++i) {
    const std::string arg = argv[i];
    if ((arg == "-n" || arg == "--n-max") && i + 1 < argc) {
      opts.n_max = std::stoi(argv[++i]);
    } else if ((arg == "-o" || arg == "--output") && i + 1 < argc) {
      opts.certificate_path = argv[++i];
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

    if (!opts.quiet) {
      std::cerr << "Building primes and witness blocks...\n";
    }
    const auto mask_primes = build_mask_primes(opts.n_max);
    const auto small_primes = build_small_primes(mask_primes);
    std::vector<i64> prime_squares;
    prime_squares.reserve(mask_primes.size());
    std::vector<i64> large_prime_squares;
    large_prime_squares.reserve(mask_primes.size());
    for (int p : mask_primes) {
      prime_squares.push_back(1LL * p * p);
      if (p > kSmallPrimeLimit) {
        large_prime_squares.push_back(1LL * p * p);
      }
    }
    auto blocks = build_prime_blocks(opts.n_max, opts.quiet, small_primes);
    auto events = build_global_events(opts.n_max, blocks);

    std::ofstream out(opts.certificate_path, std::ios::binary);
    if (!out) {
      throw std::runtime_error("failed to open certificate output: " + opts.certificate_path);
    }
    out << "N\tstatus\tmargin\tworst_p\tM\n";

    int current_base_count = 0;
    int previous_n = 1;
    int current_best_margin = current_base_count + 1;
    int current_worst_p = 0;
    std::vector<int> raw_total(blocks.size(), 0);
    std::vector<int> suffix(blocks.size() + 1, 0);

    std::size_t e = 0;
    while (e < events.size()) {
      const int n = events[e].n;
      write_certificate_interval(out, previous_n + 1, n - 1, current_worst_p, current_best_margin, current_base_count);

      bool changed = false;
      while (e < events.size() && events[e].n == n) {
        const Event ev = events[e];
        if (ev.type == EventType::Base) {
          ++current_base_count;
          advance_base_event(blocks, current_base_count, n, prime_squares, large_prime_squares);
          changed = true;
        } else {
          auto &block = blocks[static_cast<std::size_t>(ev.p_index)];
          if (ev.type == EventType::RootPlus) {
            ++block.current_raw_plus;
            while (block.next_plus_witness < block.plus.witness_values.size() &&
                   block.plus.witness_values[block.next_plus_witness] == n) {
              handle_new_plus_witness(block, current_base_count, mask_primes, prime_squares);
            }
          } else {
            ++block.current_raw_minus;
            while (block.next_minus_witness < block.minus.witness_values.size() &&
                   block.minus.witness_values[block.next_minus_witness] == n) {
              handle_new_minus_witness(block, current_base_count, mask_primes, prime_squares);
            }
          }
          changed = true;
        }
        ++e;
      }

      if (changed) {
        recompute_current_margins(blocks, current_base_count, raw_total, suffix);
        std::tie(current_worst_p, current_best_margin) = worst_prime_and_margin(blocks, current_base_count);
      }

      write_certificate_interval(out, n, n, current_worst_p, current_best_margin, current_base_count);
      previous_n = n;

      if (!opts.quiet && (n % 100000 == 0 || n == opts.n_max)) {
        std::cerr << "Reached N=" << n << ", worst_p=" << current_worst_p
                  << ", margin=" << current_best_margin << ", M=" << current_base_count << "\n";
      }
    }

    if (previous_n < opts.n_max) {
      write_certificate_interval(out, previous_n + 1, opts.n_max, current_worst_p, current_best_margin, current_base_count);
    }

    out.flush();
    std::cout << "Certificate written to " << opts.certificate_path << "\n";
    std::cout << "Final base count M(" << opts.n_max << ") = " << current_base_count << "\n";
    std::cout << "Worst active prime at N=" << opts.n_max << ": p=" << current_worst_p
              << ", margin=" << current_best_margin << "\n";
    return (current_best_margin > 0) ? 0 : 1;
  } catch (const std::exception &ex) {
    std::cerr << "error: " << ex.what() << "\n";
    return 1;
  }
}
