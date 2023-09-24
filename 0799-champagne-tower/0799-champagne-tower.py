class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0.0] * (query_row + 1) for _ in range(query_row + 1)]
        dp[0][0] = poured

        for glassRow in range(query_row):
            for glassCol in range(glassRow + 1):
                excess = (dp[glassRow][glassCol] - 1.0) / 2.0
                if excess > 0:
                    dp[glassRow + 1][glassCol] += excess
                    dp[glassRow + 1][glassCol + 1] += excess

        return min(1, dp[query_row][query_glass])
        