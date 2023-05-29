class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        memo ={ 0: 0, 1: 1, 2: 1}
        def dp(n):
            if n == 0 or n == 1:
                return n
            if n == 2:
                return 1
            if n in memo:
                return memo[n]
            if n % 2 == 0:
                memo[n] = dp(n / 2)
                return memo[n]
            else:
                memo[n] = dp(n // 2) + dp((n // 2) + 1)
                return memo[n]

        ans = 0
        for i in range(n + 1):
            ans = max(ans, dp(i))
        return ans