class Solution:

  def distinctSubseqII(self, s: str) -> int:
    MOD = 10**9 + 7
    # dp array to store the number of distinct subsequences ending with each character 'a'-'z'
    dp = [0] * 26

    for char in s:
      idx = ord(char) - ord('a')
      # Total new subsequences formed by appending `char` to all previous distinct subsequences + the single character `char` itself
      total = sum(dp) % MOD
      dp[idx] = (total + 1) % MOD

    return sum(dp) % MOD
