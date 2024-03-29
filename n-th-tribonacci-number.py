class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {0 : 0, 1: 1, 2: 1}
        def dp(n):
            if n == 0 or n == 1:
                return n
            elif n in memo:
                return memo[n]
            else:
                memo[n] = dp(n - 1) + dp(n - 2) + dp( n - 3)
                return memo[n]
        return dp(n)