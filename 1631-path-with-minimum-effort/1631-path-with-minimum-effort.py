class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = set()
        
        def dfs(row, col, effort):
            visited.add((row, col))
            
            if row == m - 1 and col == n - 1:
                return True
            
            for i, j in directions:
                newRow, newCol = row + i, col + j
                if (newRow, newCol) not in visited and 0 <= newRow < m and 0 <= newCol < n:
                    if abs(heights[newRow][newCol] - heights[row][col]) <= effort:
                        if dfs(newRow, newCol, effort):
                            return True
            return False
        
        beg, end = 0, 10 ** 6
        while beg < end:
            mid = (beg + end) // 2
            visited = set()
            if dfs(0, 0, mid):
                end = mid
            else:
                beg = mid + 1
                
        return beg