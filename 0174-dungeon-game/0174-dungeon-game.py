class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    dp[i][j] = min(0, dungeon[i][j])
                elif i == m - 1:
                    dp[i][j] = min(0, dungeon[i][j] + dp[i][j + 1])
                elif j == n - 1:
                    dp[i][j] = min(0, dungeon[i][j] + dp[i + 1][j])
                    
                else:
                    minPath = max(dp[i + 1][j] , dp[i][j + 1])
                    dp[i][j] = min(0, minPath + dungeon[i][j])

        return abs(dp[0][0]) + 1