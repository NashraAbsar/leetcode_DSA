class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        # dp[j] will store the number of ways to form t[0...j-1]
        dp = [0] * (n + 1)
        
        # Base case: There is 1 way to form an empty t
        dp[0] = 1 
        
        # Iterate through each character of s
        for i in range(1, m + 1):
            # Traverse t backwards to use the current row's previous states correctly
            for j in range(n, 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] = dp[j] + dp[j - 1]
                # If they don't match, dp[j] remains dp[j] (inheriting from the previous i step)
                
        return dp[n]
