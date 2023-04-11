class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        area = 0
        def dfs(row, col):
            visited.add((row, col))
            nonlocal area
            area += 1
            for r,c in directions:
                newRow = row + r
                newCol = col + c
                if inbound(newRow, newCol) and grid[newRow][newCol] == 1 and (newRow, newCol) not in visited:
                    
                    dfs(newRow, newCol)
            return area

        maxArea = 0        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    maxArea = max(maxArea, dfs(i, j))
                    area = 0

        return maxArea