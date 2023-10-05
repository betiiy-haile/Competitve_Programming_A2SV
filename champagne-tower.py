class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:

        dp = [0.0] * 100
        dp[0] = poured

        for row in range(query_row):
            Next = [0.0] * 100

            for glass in range(row + 1):
                overflow = max(0, (dp[glass] - 1.0) / 2.0)
                Next[glass] += overflow
                Next[glass + 1] += overflow
            
            dp = Next
        
        return min(1.0, dp[query_glass])