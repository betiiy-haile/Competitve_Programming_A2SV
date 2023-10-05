class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        minSum = float("inf")
        n = len(triangle[-1])
        memo = [[-1 for i in range(n)] for j in range(n)]
        
        @cache
        def dp(i, j, Sum):
            nonlocal minSum            
            if i == n - 1:
                return triangle[n - 1][j]
            if memo[i][j] != -1:
                return memo[i][j]
            
            if i == len(triangle):
                minSum = min(minSum, Sum)
                memo[i][j] = minSum
                return
            
            down = triangle[i][j] + dp(i + 1, j, Sum + triangle[i][j])
            diag = triangle[i][j] + dp(i + 1, j + 1, Sum + triangle[i][j])
            memo[i][j] = min(down, diag)
            return memo[i][j]
            
        return dp(0, 0, 0)