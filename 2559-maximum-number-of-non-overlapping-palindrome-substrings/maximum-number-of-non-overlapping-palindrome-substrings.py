class Solution:

  def maxPalindromes(self, s: str, k: int) -> int:
    n = len(s)
    dp = [0] * (n + 1)

    # Precompute palindrome checks to avoid redundant work
    # is_pal[i][j] will be True if s[i..j] is a palindrome
    is_pal = [[False] * n for _ in range(n)]
    for i in range(n):
      is_pal[i][i] = True
    for i in range(n - 1):
      is_pal[i][i + 1] = s[i] == s[i + 1]
    for length in range(3, n + 1):
      for i in range(n - length + 1):
        j = i + length - 1
        is_pal[i][j] = (s[i] == s[j]) and is_pal[i + 1][j - 1]

    # Fill 1D DP table
    for i in range(1, n + 1):
      # Case 1: Do not include character s[i-1] in a new palindrome
      dp[i] = dp[i - 1]

      # Case 2: Check if a palindrome of length k ends at s[i-1]
      if i >= k and is_pal[i - k][i - 1]:
        dp[i] = max(dp[i], dp[i - k] + 1)

      # Case 3: Check if a palindrome of length k+1 ends at s[i-1]
      if i >= k + 1 and is_pal[i - k - 1][i - 1]:
        dp[i] = max(dp[i], dp[i - k - 1] + 1)

    return dp[n]
