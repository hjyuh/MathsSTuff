import Mathlib

open Nat

private theorem centralBinom_factorization_eq_of_card
    (n p b e : ℕ) (hp : p.Prime) (hlog : Nat.log p (2 * n) < b)
    (hcard : ({i ∈ Finset.Ico 1 b | p ^ i ≤ n % p ^ i + n % p ^ i}.card = e)) :
    (Nat.centralBinom n).factorization p = e := by
  rw [Nat.centralBinom_eq_two_mul_choose]
  rw [Nat.factorization_choose hp (by omega : n ≤ 2 * n) hlog]
  have hsub : 2 * n - n = n := by omega
  simpa [hsub] using hcard

private theorem prime_pow_dvd_centralBinom_of_card
    (n p b a e : ℕ) (hp : p.Prime) (hlog : Nat.log p (2 * n) < b)
    (hcard : ({i ∈ Finset.Ico 1 b | p ^ i ≤ n % p ^ i + n % p ^ i}.card = e))
    (hae : a ≤ e) :
    p ^ a ∣ Nat.centralBinom n := by
  have hfac := centralBinom_factorization_eq_of_card n p b e hp hlog hcard
  exact (hp.pow_dvd_iff_le_factorization (Nat.centralBinom_ne_zero n)).2 (by
    simpa [hfac] using hae)

private theorem descFactorial_dvd_centralBinom_of_factorization_le {k n : ℕ}
    (hkn : k + 1 ≤ n)
    (hfac : (n.descFactorial (k + 1)).factorization ≤ (Nat.centralBinom n).factorization) :
    n.descFactorial (k + 1) ∣ Nat.centralBinom n := by
  exact (Nat.factorization_le_iff_dvd (Nat.descFactorial_pos.mpr hkn).ne'
    (Nat.centralBinom_ne_zero n)).mp hfac

private theorem descFactorial_dvd_centralBinom_of_carry_count_le {k n : ℕ}
    (hkn : k + 1 ≤ n)
    (hfac : ∀ p, p.Prime →
      (n.descFactorial (k + 1)).factorization p ≤
        ({i ∈ Finset.Ico 1 (Nat.log p (2 * n) + 1) |
          p ^ i ≤ n % p ^ i + n % p ^ i}.card)) :
    n.descFactorial (k + 1) ∣ Nat.centralBinom n := by
  refine descFactorial_dvd_centralBinom_of_factorization_le hkn ?_
  intro p
  by_cases hp : p.Prime
  · have hcentral := centralBinom_factorization_eq_of_card n p (Nat.log p (2 * n) + 1)
      ({i ∈ Finset.Ico 1 (Nat.log p (2 * n) + 1) |
        p ^ i ≤ n % p ^ i + n % p ^ i}.card) hp (by omega) rfl
    simpa [hcentral] using hfac p hp
  · have hleft : (n.descFactorial (k + 1)).factorization p = 0 := by
      exact Nat.factorization_eq_zero_of_not_prime (n.descFactorial (k + 1)) hp
    rw [hleft]
    exact Nat.zero_le _

theorem erdos_396_k0 : ∃ n : ℕ, n.descFactorial (0 + 1) ∣ Nat.centralBinom n := by
  refine ⟨2, ?_⟩
  norm_num [Nat.descFactorial, Nat.centralBinom, Nat.choose]

theorem erdos_396_k1 : ∃ n : ℕ, n.descFactorial (1 + 1) ∣ Nat.centralBinom n := by
  refine ⟨2, ?_⟩
  norm_num [Nat.descFactorial, Nat.centralBinom, Nat.choose]

theorem erdos_396_k2_witness :
    (2480 : ℕ).descFactorial (2 + 1) ∣ Nat.centralBinom 2480 := by
  let C := Nat.centralBinom 2480
  have h32 : 32 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 2480 2 13 5 5 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h3 : 3 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 2480 3 8 1 4 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h5 : 5 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 2480 5 6 1 3 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h7 : 7 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 2480 7 5 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h31 : 31 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 2480 31 4 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h37 : 37 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 2480 37 4 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h59 : 59 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 2480 59 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h67 : 67 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 2480 67 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h96 : 96 ∣ C := by
    have hcop : Nat.Coprime 32 3 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h32 h3
  have h480 : 480 ∣ C := by
    have hcop : Nat.Coprime 96 5 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h96 h5
  have h3360 : 3360 ∣ C := by
    have hcop : Nat.Coprime 480 7 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h480 h7
  have h104160 : 104160 ∣ C := by
    have hcop : Nat.Coprime 3360 31 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h3360 h31
  have h3853920 : 3853920 ∣ C := by
    have hcop : Nat.Coprime 104160 37 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h104160 h37
  have h227381280 : 227381280 ∣ C := by
    have hcop : Nat.Coprime 3853920 59 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h3853920 h59
  have hprod : 15234545760 ∣ C := by
    have hcop : Nat.Coprime 227381280 67 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h227381280 h67
  norm_num [Nat.descFactorial]
  exact hprod

theorem erdos_396_k2 : ∃ n : ℕ, n.descFactorial (2 + 1) ∣ Nat.centralBinom n :=
  ⟨2480, erdos_396_k2_witness⟩

theorem erdos_396_k3_witness :
    (8178 : ℕ).descFactorial (3 + 1) ∣ Nat.centralBinom 8178 := by
  let C := Nat.centralBinom 8178
  have h32 : 32 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 8178 2 14 5 10 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h9 : 9 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 8178 3 9 2 5 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h25 : 25 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 8178 5 7 2 3 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h7 : 7 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 8178 7 5 1 2 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h13 : 13 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 8178 13 4 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h17 : 17 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 8178 17 4 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h29 : 29 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 8178 29 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h37 : 37 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 8178 37 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h47 : 47 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 8178 47 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h73 : 73 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 8178 73 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h109 : 109 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 8178 109 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h288 : 288 ∣ C := by
    have hcop : Nat.Coprime 32 9 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h32 h9
  have h7200 : 7200 ∣ C := by
    have hcop : Nat.Coprime 288 25 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h288 h25
  have h50400 : 50400 ∣ C := by
    have hcop : Nat.Coprime 7200 7 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h7200 h7
  have h655200 : 655200 ∣ C := by
    have hcop : Nat.Coprime 50400 13 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h50400 h13
  have h11138400 : 11138400 ∣ C := by
    have hcop : Nat.Coprime 655200 17 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h655200 h17
  have h323013600 : 323013600 ∣ C := by
    have hcop : Nat.Coprime 11138400 29 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h11138400 h29
  have h11951503200 : 11951503200 ∣ C := by
    have hcop : Nat.Coprime 323013600 37 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h323013600 h37
  have h561720650400 : 561720650400 ∣ C := by
    have hcop : Nat.Coprime 11951503200 47 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h11951503200 h47
  have h41005607479200 : 41005607479200 ∣ C := by
    have hcop : Nat.Coprime 561720650400 73 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h561720650400 h73
  have hprod : 4469611215232800 ∣ C := by
    have hcop : Nat.Coprime 41005607479200 109 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h41005607479200 h109
  norm_num [Nat.descFactorial]
  exact hprod

theorem erdos_396_k3 : ∃ n : ℕ, n.descFactorial (3 + 1) ∣ Nat.centralBinom n :=
  ⟨8178, erdos_396_k3_witness⟩

theorem erdos_396_k4_witness :
    (45153 : ℕ).descFactorial (4 + 1) ∣ Nat.centralBinom 45153 := by
  let C := Nat.centralBinom 45153
  have h64 : 64 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 45153 2 17 6 6 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h27 : 27 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 45153 3 11 3 5 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h25 : 25 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 45153 5 8 2 3 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h7 : 7 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 45153 7 6 1 3 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h13 : 13 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 45153 13 5 1 2 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h17 : 17 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 45153 17 5 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h23 : 23 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 45153 23 4 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h29 : 29 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 45153 29 4 1 2 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h43 : 43 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 45153 43 4 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h83 : 83 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 45153 83 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h151 : 151 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 45153 151 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h163 : 163 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 45153 163 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h173 : 173 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 45153 173 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h277 : 277 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 45153 277 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h1728 : 1728 ∣ C := by
    have hcop : Nat.Coprime 64 27 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h64 h27
  have h43200 : 43200 ∣ C := by
    have hcop : Nat.Coprime 1728 25 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h1728 h25
  have h302400 : 302400 ∣ C := by
    have hcop : Nat.Coprime 43200 7 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h43200 h7
  have h3931200 : 3931200 ∣ C := by
    have hcop : Nat.Coprime 302400 13 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h302400 h13
  have h66830400 : 66830400 ∣ C := by
    have hcop : Nat.Coprime 3931200 17 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h3931200 h17
  have h1537099200 : 1537099200 ∣ C := by
    have hcop : Nat.Coprime 66830400 23 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h66830400 h23
  have h44575876800 : 44575876800 ∣ C := by
    have hcop : Nat.Coprime 1537099200 29 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h1537099200 h29
  have h1916762702400 : 1916762702400 ∣ C := by
    have hcop : Nat.Coprime 44575876800 43 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h44575876800 h43
  have h159091304299200 : 159091304299200 ∣ C := by
    have hcop : Nat.Coprime 1916762702400 83 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h1916762702400 h83
  have h24022786949179200 : 24022786949179200 ∣ C := by
    have hcop : Nat.Coprime 159091304299200 151 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h159091304299200 h151
  have h3915714272716209600 : 3915714272716209600 ∣ C := by
    have hcop : Nat.Coprime 24022786949179200 163 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h24022786949179200 h163
  have h677418569179904260800 : 677418569179904260800 ∣ C := by
    have hcop : Nat.Coprime 3915714272716209600 173 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h3915714272716209600 h173
  have hprod : 187644943662833480241600 ∣ C := by
    have hcop : Nat.Coprime 677418569179904260800 277 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h677418569179904260800 h277
  norm_num [Nat.descFactorial]
  exact hprod

theorem erdos_396_k4 : ∃ n : ℕ, n.descFactorial (4 + 1) ∣ Nat.centralBinom n :=
  ⟨45153, erdos_396_k4_witness⟩

theorem erdos_396_k5_witness :
    (3648841 : ℕ).descFactorial (5 + 1) ∣ Nat.centralBinom 3648841 := by
  let C := Nat.centralBinom 3648841
  have h64 : 64 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 3648841 2 23 6 13 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h9 : 9 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 3648841 3 15 2 6 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h5 : 5 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 3648841 5 10 1 6 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h7 : 7 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 3648841 7 9 1 2 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h13 : 13 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 3648841 13 7 1 5 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h19 : 19 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 3648841 19 6 1 3 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h29 : 29 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 3648841 29 5 1 2 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h41 : 41 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 3648841 41 5 1 2 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h53 : 53 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 3648841 53 4 1 2 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h61 : 61 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 3648841 61 4 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h127 : 127 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 3648841 127 4 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h157 : 157 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 3648841 157 4 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h383 : 383 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 3648841 383 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h1171 : 1171 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 3648841 1171 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h1187 : 1187 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 3648841 1187 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h1361 : 1361 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 3648841 1361 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h1427 : 1427 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 3648841 1427 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h2339 : 2339 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 3648841 2339 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h2557 : 2557 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 3648841 2557 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h576 : 576 ∣ C := by
    have hcop : Nat.Coprime 64 9 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h64 h9
  have h2880 : 2880 ∣ C := by
    have hcop : Nat.Coprime 576 5 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h576 h5
  have h20160 : 20160 ∣ C := by
    have hcop : Nat.Coprime 2880 7 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h2880 h7
  have h262080 : 262080 ∣ C := by
    have hcop : Nat.Coprime 20160 13 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h20160 h13
  have h4979520 : 4979520 ∣ C := by
    have hcop : Nat.Coprime 262080 19 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h262080 h19
  have h144406080 : 144406080 ∣ C := by
    have hcop : Nat.Coprime 4979520 29 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h4979520 h29
  have h5920649280 : 5920649280 ∣ C := by
    have hcop : Nat.Coprime 144406080 41 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h144406080 h41
  have h313794411840 : 313794411840 ∣ C := by
    have hcop : Nat.Coprime 5920649280 53 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h5920649280 h53
  have h19141459122240 : 19141459122240 ∣ C := by
    have hcop : Nat.Coprime 313794411840 61 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h313794411840 h61
  have h2430965308524480 : 2430965308524480 ∣ C := by
    have hcop : Nat.Coprime 19141459122240 127 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h19141459122240 h127
  have h381661553438343360 : 381661553438343360 ∣ C := by
    have hcop : Nat.Coprime 2430965308524480 157 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h2430965308524480 h157
  have h146176374966885506880 : 146176374966885506880 ∣ C := by
    have hcop : Nat.Coprime 381661553438343360 383 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h381661553438343360 h383
  have h171172535086222928556480 : 171172535086222928556480 ∣ C := by
    have hcop : Nat.Coprime 146176374966885506880 1171 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h146176374966885506880 h1171
  have h203181799147346616196541760 : 203181799147346616196541760 ∣ C := by
    have hcop : Nat.Coprime 171172535086222928556480 1187 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h171172535086222928556480 h1187
  have h276530428639538744643493335360 : 276530428639538744643493335360 ∣ C := by
    have hcop : Nat.Coprime 203181799147346616196541760 1361 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h203181799147346616196541760 h1361
  have h394608921668621788606264989558720 : 394608921668621788606264989558720 ∣ C := by
    have hcop : Nat.Coprime 276530428639538744643493335360 1427 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h276530428639538744643493335360 h1427
  have h922990267782906363550053810577846080 : 922990267782906363550053810577846080 ∣ C := by
    have hcop : Nat.Coprime 394608921668621788606264989558720 2339 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h394608921668621788606264989558720 h2339
  have hprod : 2360086114720891571597487593647552426560 ∣ C := by
    have hcop : Nat.Coprime 922990267782906363550053810577846080 2557 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h922990267782906363550053810577846080 h2557
  norm_num [Nat.descFactorial]
  exact hprod

theorem erdos_396_k5 : ∃ n : ℕ, n.descFactorial (5 + 1) ∣ Nat.centralBinom n :=
  ⟨3648841, erdos_396_k5_witness⟩

theorem erdos_396_k6_witness :
    (7979090 : ℕ).descFactorial (6 + 1) ∣ Nat.centralBinom 7979090 := by
  let C := Nat.centralBinom 7979090
  have h256 : 256 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 7979090 2 24 8 10 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h27 : 27 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 7979090 3 16 3 6 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h25 : 25 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 7979090 5 11 2 5 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h7 : 7 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 7979090 7 9 1 5 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h13 : 13 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 7979090 13 7 1 3 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h17 : 17 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 7979090 17 6 1 2 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h19 : 19 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 7979090 19 6 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h29 : 29 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 7979090 29 5 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h31 : 31 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 7979090 31 5 1 3 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h37 : 37 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 7979090 37 5 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h233 : 233 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 7979090 233 4 1 2 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h331 : 331 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 7979090 331 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h379 : 379 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 7979090 379 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h503 : 503 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 7979090 503 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h509 : 509 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 7979090 509 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h547 : 547 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 7979090 547 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h569 : 569 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 7979090 569 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h673 : 673 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 7979090 673 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h709 : 709 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 7979090 709 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h761 : 761 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 7979090 761 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h3677 : 3677 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 7979090 3677 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h3919 : 3919 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 7979090 3919 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h6912 : 6912 ∣ C := by
    have hcop : Nat.Coprime 256 27 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h256 h27
  have h172800 : 172800 ∣ C := by
    have hcop : Nat.Coprime 6912 25 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h6912 h25
  have h1209600 : 1209600 ∣ C := by
    have hcop : Nat.Coprime 172800 7 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h172800 h7
  have h15724800 : 15724800 ∣ C := by
    have hcop : Nat.Coprime 1209600 13 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h1209600 h13
  have h267321600 : 267321600 ∣ C := by
    have hcop : Nat.Coprime 15724800 17 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h15724800 h17
  have h5079110400 : 5079110400 ∣ C := by
    have hcop : Nat.Coprime 267321600 19 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h267321600 h19
  have h147294201600 : 147294201600 ∣ C := by
    have hcop : Nat.Coprime 5079110400 29 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h5079110400 h29
  have h4566120249600 : 4566120249600 ∣ C := by
    have hcop : Nat.Coprime 147294201600 31 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h147294201600 h31
  have h168946449235200 : 168946449235200 ∣ C := by
    have hcop : Nat.Coprime 4566120249600 37 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h4566120249600 h37
  have h39364522671801600 : 39364522671801600 ∣ C := by
    have hcop : Nat.Coprime 168946449235200 233 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h168946449235200 h233
  have h13029657004366329600 : 13029657004366329600 ∣ C := by
    have hcop : Nat.Coprime 39364522671801600 331 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h39364522671801600 h331
  have h4938240004654838918400 : 4938240004654838918400 ∣ C := by
    have hcop : Nat.Coprime 13029657004366329600 379 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h13029657004366329600 h379
  have h2483934722341383975955200 : 2483934722341383975955200 ∣ C := by
    have hcop : Nat.Coprime 4938240004654838918400 503 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h4938240004654838918400 h503
  have h1264322773671764443761196800 : 1264322773671764443761196800 ∣ C := by
    have hcop : Nat.Coprime 2483934722341383975955200 509 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h2483934722341383975955200 h509
  have h691584557198455150737374649600 : 691584557198455150737374649600 ∣ C := by
    have hcop : Nat.Coprime 1264322773671764443761196800 547 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h1264322773671764443761196800 h547
  have h393511613045920980769566175622400 : 393511613045920980769566175622400 ∣ C := by
    have hcop : Nat.Coprime 691584557198455150737374649600 569 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h691584557198455150737374649600 h569
  have h264833315579904820057918036193875200 : 264833315579904820057918036193875200 ∣ C := by
    have hcop : Nat.Coprime 393511613045920980769566175622400 673 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h393511613045920980769566175622400 h673
  have h187766820746152517421063887661457516800 :
      187766820746152517421063887661457516800 ∣ C := by
    have hcop : Nat.Coprime 264833315579904820057918036193875200 709 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h264833315579904820057918036193875200 h709
  have h142890550587822065757429618510369170284800 :
      142890550587822065757429618510369170284800 ∣ C := by
    have hcop : Nat.Coprime 187766820746152517421063887661457516800 761 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h187766820746152517421063887661457516800 h761
  have h525408554511421735790068707262627439137209600 :
      525408554511421735790068707262627439137209600 ∣ C := by
    have hcop : Nat.Coprime 142890550587822065757429618510369170284800 3677 := by
      norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h142890550587822065757429618510369170284800 h3677
  have hprod : 2059076125130261782561279263762236933978724422400 ∣ C := by
    have hcop : Nat.Coprime 525408554511421735790068707262627439137209600 3919 := by
      norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h525408554511421735790068707262627439137209600 h3919
  norm_num [Nat.descFactorial]
  exact hprod

theorem erdos_396_k6 : ∃ n : ℕ, n.descFactorial (6 + 1) ∣ Nat.centralBinom n :=
  ⟨7979090, erdos_396_k6_witness⟩

theorem erdos_396_k7_witness :
    (101130029 : ℕ).descFactorial (7 + 1) ∣ Nat.centralBinom 101130029 := by
  let C := Nat.centralBinom 101130029
  have h128 : 128 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 101130029 2 28 7 14 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h9 : 9 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 101130029 3 18 2 10 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h25 : 25 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 101130029 5 12 2 4 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h343 : 343 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 101130029 7 10 3 6 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h11 : 11 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 101130029 11 8 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h13 : 13 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 101130029 13 8 1 5 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h17 : 17 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 101130029 17 7 1 2 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h19 : 19 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 101130029 19 7 1 2 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h31 : 31 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 101130029 31 6 1 3 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h37 : 37 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 101130029 37 6 1 2 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h41 : 41 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 101130029 41 6 1 3 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h43 : 43 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 101130029 43 6 1 3 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h83 : 83 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 101130029 83 5 1 2 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h113 : 113 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 101130029 113 5 1 2 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h149 : 149 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 101130029 149 4 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h167 : 167 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 101130029 167 4 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h347 : 347 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 101130029 347 4 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h1039 : 1039 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 101130029 1039 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h1187 : 1187 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 101130029 1187 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h1597 : 1597 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 101130029 1597 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h1657 : 1657 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 101130029 1657 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h2543 : 2543 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 101130029 2543 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h3259 : 3259 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 101130029 3259 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h5113 : 5113 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 101130029 5113 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h6047 : 6047 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 101130029 6047 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h12433 : 12433 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 101130029 12433 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h14083 : 14083 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 101130029 14083 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have hstep1 : 1152 ∣ C := by
    have hcop : Nat.Coprime 128 9 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h128 h9
  have hstep2 : 28800 ∣ C := by
    have hcop : Nat.Coprime 1152 25 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep1 h25
  have hstep3 : 9878400 ∣ C := by
    have hcop : Nat.Coprime 28800 343 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep2 h343
  have hstep4 : 108662400 ∣ C := by
    have hcop : Nat.Coprime 9878400 11 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep3 h11
  have hstep5 : 1412611200 ∣ C := by
    have hcop : Nat.Coprime 108662400 13 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep4 h13
  have hstep6 : 24014390400 ∣ C := by
    have hcop : Nat.Coprime 1412611200 17 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep5 h17
  have hstep7 : 456273417600 ∣ C := by
    have hcop : Nat.Coprime 24014390400 19 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep6 h19
  have hstep8 : 14144475945600 ∣ C := by
    have hcop : Nat.Coprime 456273417600 31 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep7 h31
  have hstep9 : 523345609987200 ∣ C := by
    have hcop : Nat.Coprime 14144475945600 37 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep8 h37
  have hstep10 : 21457170009475200 ∣ C := by
    have hcop : Nat.Coprime 523345609987200 41 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep9 h41
  have hstep11 : 922658310407433600 ∣ C := by
    have hcop : Nat.Coprime 21457170009475200 43 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep10 h43
  have hstep12 : 76580639763816988800 ∣ C := by
    have hcop : Nat.Coprime 922658310407433600 83 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep11 h83
  have hstep13 : 8653612293311319734400 ∣ C := by
    have hcop : Nat.Coprime 76580639763816988800 113 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep12 h113
  have hstep14 : 1289388231703386640425600 ∣ C := by
    have hcop : Nat.Coprime 8653612293311319734400 149 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep13 h149
  have hstep15 : 215327834694465568951075200 ∣ C := by
    have hcop : Nat.Coprime 1289388231703386640425600 167 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep14 h167
  have hstep16 : 74718758638979552426023094400 ∣ C := by
    have hcop : Nat.Coprime 215327834694465568951075200 347 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep15 h347
  have hstep17 : 77632790225899754970637995081600 ∣ C := by
    have hcop : Nat.Coprime 74718758638979552426023094400 1039 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep16 h1039
  have hstep18 : 92150121998143009150147300161859200 ∣ C := by
    have hcop : Nat.Coprime 77632790225899754970637995081600 1187 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep17 h1187
  have hstep19 : 147163744831034385612785238358489142400 ∣ C := by
    have hcop : Nat.Coprime 92150121998143009150147300161859200 1597 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep18 h1597
  have hstep20 : 243850325185023976960385139960016508956800 ∣ C := by
    have hcop : Nat.Coprime 147163744831034385612785238358489142400 1657 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep19 h1657
  have hstep21 : 620111376945515973410259410918321982277142400 ∣ C := by
    have hcop : Nat.Coprime 243850325185023976960385139960016508956800 2543 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep20 h2543
  have hstep22 : 2020942977465436557344035420182811340241207081600 ∣ C := by
    have hcop : Nat.Coprime 620111376945515973410259410918321982277142400 3259 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep21 h3259
  have hstep23 : 10333081443780777117700053103394714382653291808220800 ∣ C := by
    have hcop : Nat.Coprime 2020942977465436557344035420182811340241207081600 5113 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep22 h5113
  have hstep24 : 62484143490542359230732221116227837871904455564311177600 ∣ C := by
    have hcop :
        Nat.Coprime 10333081443780777117700053103394714382653291808220800 6047 := by
      norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep23 h6047
  have hstep25 : 776865356017913152315693705138060708261388096031080871100800 ∣ C := by
    have hcop :
        Nat.Coprime 62484143490542359230732221116227837871904455564311177600 12433 := by
      norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep24 h12433
  have hprod : 10940594808800270924061914449459308954445128556405711907712566400 ∣ C := by
    have hcop :
        Nat.Coprime 776865356017913152315693705138060708261388096031080871100800 14083 := by
      norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep25 h14083
  norm_num [Nat.descFactorial]
  exact hprod

theorem erdos_396_k7 : ∃ n : ℕ, n.descFactorial (7 + 1) ∣ Nat.centralBinom n :=
  ⟨101130029, erdos_396_k7_witness⟩
theorem erdos_396_k8_witness :
    (339949252 : ℕ).descFactorial (8 + 1) ∣ Nat.centralBinom 339949252 := by
  let C := Nat.centralBinom 339949252
  have h4096 : 4096 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 339949252 2 30 12 12 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h243 : 243 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 339949252 3 19 5 8 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h625 : 625 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 339949252 5 13 4 5 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h7 : 7 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 339949252 7 11 1 8 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h11 : 11 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 339949252 11 9 1 6 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h169 : 169 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 339949252 13 8 2 2 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h23 : 23 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 339949252 23 7 1 2 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h29 : 29 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 339949252 29 7 1 4 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h41 : 41 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 339949252 41 6 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h73 : 73 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 339949252 73 5 1 2 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h79 : 79 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 339949252 79 5 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h191 : 191 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 339949252 191 4 1 2 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h331 : 331 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 339949252 331 4 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h491 : 491 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 339949252 491 4 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h541 : 541 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 339949252 541 4 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h701 : 701 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 339949252 701 4 1 2 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h743 : 743 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 339949252 743 4 1 2 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h859 : 859 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 339949252 859 4 1 2 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h1279 : 1279 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 339949252 1279 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h1583 : 1583 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 339949252 1583 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h2383 : 2383 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 339949252 2383 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h2539 : 2539 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 339949252 2539 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h4127 : 4127 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 339949252 4127 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h5417 : 5417 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 339949252 5417 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h6247 : 6247 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 339949252 6247 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h6997 : 6997 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 339949252 6997 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h20593 : 20593 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 339949252 20593 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have h25643 : 25643 ∣ C := by
    simpa using prime_pow_dvd_centralBinom_of_card 339949252 25643 3 1 1 (by norm_num)
      (by norm_num) (by decide) (by norm_num)
  have hstep1 : 995328 ∣ C := by
    have hcop : Nat.Coprime 4096 243 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd h4096 h243
  have hstep2 : 622080000 ∣ C := by
    have hcop : Nat.Coprime 995328 625 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep1 h625
  have hstep3 : 4354560000 ∣ C := by
    have hcop : Nat.Coprime 622080000 7 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep2 h7
  have hstep4 : 47900160000 ∣ C := by
    have hcop : Nat.Coprime 4354560000 11 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep3 h11
  have hstep5 : 8095127040000 ∣ C := by
    have hcop : Nat.Coprime 47900160000 169 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep4 h169
  have hstep6 : 186187921920000 ∣ C := by
    have hcop : Nat.Coprime 8095127040000 23 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep5 h23
  have hstep7 : 5399449735680000 ∣ C := by
    have hcop : Nat.Coprime 186187921920000 29 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep6 h29
  have hstep8 : 221377439162880000 ∣ C := by
    have hcop : Nat.Coprime 5399449735680000 41 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep7 h41
  have hstep9 : 16160553058890240000 ∣ C := by
    have hcop : Nat.Coprime 221377439162880000 73 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep8 h73
  have hstep10 : 1276683691652328960000 ∣ C := by
    have hcop : Nat.Coprime 16160553058890240000 79 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep9 h79
  have hstep11 : 243846585105594831360000 ∣ C := by
    have hcop : Nat.Coprime 1276683691652328960000 191 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep10 h191
  have hstep12 : 80713219669951889180160000 ∣ C := by
    have hcop : Nat.Coprime 243846585105594831360000 331 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep11 h331
  have hstep13 : 39630190857946377587458560000 ∣ C := by
    have hcop : Nat.Coprime 80713219669951889180160000 491 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep12 h491
  have hstep14 : 21439933254148990274815080960000 ∣ C := by
    have hcop : Nat.Coprime 39630190857946377587458560000 541 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep13 h541
  have hstep15 : 15029393211158442182645371752960000 ∣ C := by
    have hcop : Nat.Coprime 21439933254148990274815080960000 701 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep14 h701
  have hstep16 : 11166839155890722541705511212449280000 ∣ C := by
    have hcop : Nat.Coprime 15029393211158442182645371752960000 743 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep15 h743
  have hstep17 : 9592314834910130663325034131493931520000 ∣ C := by
    have hcop : Nat.Coprime 11166839155890722541705511212449280000 859 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep16 h859
  have hstep18 : 12268570673850057118392718654180738414080000 ∣ C := by
    have hcop : Nat.Coprime 9592314834910130663325034131493931520000 1279 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep17 h1279
  have hstep19 : 19421147376704640418415673629568108909488640000 ∣ C := by
    have hcop : Nat.Coprime 12268570673850057118392718654180738414080000 1583 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep18 h1583
  have hstep20 : 46280594198687158117084550259260803531311429120000 ∣ C := by
    have hcop : Nat.Coprime 19421147376704640418415673629568108909488640000 2383 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep19 h2383
  have hstep21 : 117506428670466694459277673108263180165999718535680000 ∣ C := by
    have hcop : Nat.Coprime 46280594198687158117084550259260803531311429120000 2539 := by norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep20 h2539
  have hstep22 : 484949031123016048033438956917802144545080838396751360000 ∣ C := by
    have hcop :
        Nat.Coprime 117506428670466694459277673108263180165999718535680000 4127 := by
      norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep21 h4127
  have hstep23 : 2626968901593377932197138829623734217000702901595202117120000 ∣ C := by
    have hcop :
        Nat.Coprime 484949031123016048033438956917802144545080838396751360000 5417 := by
      norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep22 h5417
  have hstep24 : 16410674728253831942435526268659467653603391026265227625648640000 ∣ C := by
    have hcop :
        Nat.Coprime 2626968901593377932197138829623734217000702901595202117120000 6247 := by
      norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep23 h6247
  have hstep25 : 114825491073592062101221377301810295172262927010777797696663534080000 ∣ C := by
    have hcop :
        Nat.Coprime 16410674728253831942435526268659467653603391026265227625648640000 6997 := by
      norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep24 h6997
  have hstep26 : 2364601337678481334850451822776179408482410455932947187967392157309440000 ∣ C := by
    have hcop :
        Nat.Coprime
          114825491073592062101221377301810295172262927010777797696663534080000
          20593 := by
      norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep25 h20593
  have hprod :
      60635472102089296869570136091449568571714451321488564741047837089885969920000 ∣ C := by
    have hcop :
        Nat.Coprime
          2364601337678481334850451822776179408482410455932947187967392157309440000
          25643 := by
      norm_num
    simpa using hcop.mul_dvd_of_dvd_of_dvd hstep26 h25643
  norm_num [Nat.descFactorial]
  exact hprod

theorem erdos_396_k8 : ∃ n : ℕ, n.descFactorial (8 + 1) ∣ Nat.centralBinom n :=
  ⟨339949252, erdos_396_k8_witness⟩
theorem erdos_396_for_k_le_three :
    ∀ k ≤ 3, ∃ n : ℕ, n.descFactorial (k + 1) ∣ Nat.centralBinom n := by
  intro k hk
  interval_cases k
  · simpa using erdos_396_k0
  · simpa using erdos_396_k1
  · simpa using erdos_396_k2
  · simpa using erdos_396_k3

theorem erdos_396_for_k_le_four :
    ∀ k ≤ 4, ∃ n : ℕ, n.descFactorial (k + 1) ∣ Nat.centralBinom n := by
  intro k hk
  interval_cases k
  · simpa using erdos_396_k0
  · simpa using erdos_396_k1
  · simpa using erdos_396_k2
  · simpa using erdos_396_k3
  · simpa using erdos_396_k4

theorem erdos_396_for_k_le_five :
    ∀ k ≤ 5, ∃ n : ℕ, n.descFactorial (k + 1) ∣ Nat.centralBinom n := by
  intro k hk
  interval_cases k
  · simpa using erdos_396_k0
  · simpa using erdos_396_k1
  · simpa using erdos_396_k2
  · simpa using erdos_396_k3
  · simpa using erdos_396_k4
  · simpa using erdos_396_k5

theorem erdos_396_for_k_le_six :
    ∀ k ≤ 6, ∃ n : ℕ, n.descFactorial (k + 1) ∣ Nat.centralBinom n := by
  intro k hk
  interval_cases k
  · simpa using erdos_396_k0
  · simpa using erdos_396_k1
  · simpa using erdos_396_k2
  · simpa using erdos_396_k3
  · simpa using erdos_396_k4
  · simpa using erdos_396_k5
  · simpa using erdos_396_k6

theorem erdos_396_for_k_le_seven :
    ∀ k ≤ 7, ∃ n : ℕ, n.descFactorial (k + 1) ∣ Nat.centralBinom n := by
  intro k hk
  interval_cases k
  · simpa using erdos_396_k0
  · simpa using erdos_396_k1
  · simpa using erdos_396_k2
  · simpa using erdos_396_k3
  · simpa using erdos_396_k4
  · simpa using erdos_396_k5
  · simpa using erdos_396_k6
  · simpa using erdos_396_k7

theorem erdos_396_for_k_le_eight :
    ∀ k ≤ 8, ∃ n : ℕ, n.descFactorial (k + 1) ∣ Nat.centralBinom n := by
  intro k hk
  interval_cases k
  · simpa using erdos_396_k0
  · simpa using erdos_396_k1
  · simpa using erdos_396_k2
  · simpa using erdos_396_k3
  · simpa using erdos_396_k4
  · simpa using erdos_396_k5
  · simpa using erdos_396_k6
  · simpa using erdos_396_k7
  · simpa using erdos_396_k8

/-- Erdős Problem 396: For every k, there exists n such that
    n(n-1)(n-2)...(n-k) divides the central binomial coefficient C(2n,n). -/
theorem erdos_396 : ∀ k : ℕ, ∃ n : ℕ, n.descFactorial (k + 1) ∣ Nat.centralBinom n := by
  intro k
  by_cases hk : k ≤ 8
  · exact erdos_396_for_k_le_eight k hk
  · sorry
