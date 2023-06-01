class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def inBound(row, col):
            return 0 <= row < m and 0 <= col < n

        def dp(row, col):
            if row == m - 1 and col == n -1:
                return 1
            ans = 0
            if (row, col) not in memo:
                for (r, c) in [(0,1), (1,0)]:
                    if inBound(row + r, col + c):
                        ans += dp(row + r, col + c)   
                memo[(row, col)] = ans
            return memo[(row, col)]

        return dp(0, 0)