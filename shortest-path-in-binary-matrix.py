class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (0, -1), (1,0), (-1, 0), (-1,-1), (-1, 1),(1, -1), (1, 1)]
        visited = set()
        visited.add((0, 0))
        n = len(grid)
        queue = deque([(0,0)])

        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1

        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        level = 1
        while queue:
            length = len(queue)
            for i in range(length):
                row, col = queue.popleft()
                if row == col == n-1:
                    return level           
                
                for r, c in directions:
                    nr = r + row
                    nc = c + col
                    if inbound(nr, nc) and grid[nr][nc] == 0 and (nr, nc) not in visited:
                        queue.append((nr , nc))
                        visited.add((nr, nc)) 

                        
            level += 1
                           

        return -1