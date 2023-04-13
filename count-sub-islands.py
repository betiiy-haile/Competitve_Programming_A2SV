class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visited = set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(row, col):
            if row < 0 or col < 0 or row == len(grid1) or col == len(grid1[0]) or grid2[row][col] == 0 or (row, col) in visited:
                return True        

            visited.add((row, col))
            res = True
            if grid1[row][col] == 0:
                res = False

            for r,c in directions:
                res = dfs(row + r, col + c) and res 
            return res

        count = 0
        for r in range(len(grid1)):
            for c in range(len(grid1[0])):
                if grid2[r][c] == 1 and (r,c) not in visited and dfs(r,c):
                    count += 1

        return count