class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        
        dp = grid

        for i in range(len(grid) - 2, -1, -1):
            for k in range(len(grid[0])):
                curr = grid[i][k]
                temp = moveCost[curr][0] + dp[i + 1][0]
                for j in range(len(grid[0])):
                    temp = min(temp, moveCost[curr][j] + dp[i + 1][j])
                dp[i][k] += temp
                
        return min(dp[0])