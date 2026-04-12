def hello : String := "world"

theorem coprime_core_ineq (N M : Nat) (hN : 6 ≤ N) (hM : N < M) :
    N * (M / 2 + M / 3 - M / 6) ≤ 2 * M * (N / 2 + N / 3 - N / 6) := by
  have h1 : M / 2 + M / 3 - M / 6 ≤ M := by omega
  have h2 : N ≤ 2 * (N / 2 + N / 3 - N / 6) := by omega
  calc N * (M / 2 + M / 3 - M / 6)
      ≤ N * M := Nat.mul_le_mul_left N h1
      _ = M * N := Nat.mul_comm N M
      _ ≤ M * (2 * (N / 2 + N / 3 - N / 6)) := Nat.mul_le_mul_left M h2
      _ = M * 2 * (N / 2 + N / 3 - N / 6) := (Nat.mul_assoc M 2 _).symm
      _ = 2 * M * (N / 2 + N / 3 - N / 6) := by rw [Nat.mul_comm M 2]
