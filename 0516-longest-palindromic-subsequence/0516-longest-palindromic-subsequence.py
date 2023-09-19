class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        R = s[::-1]
        print(R)
        n = len(s)
        
        dp =[[0 for i in range(n + 1)] for j in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == R[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    
                    
        return dp[n][n]
                    