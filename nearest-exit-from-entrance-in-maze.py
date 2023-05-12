class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
        visited = set(entrance)
        queue = deque([entrance])

        destinations = set()
        for row in [0, len(maze) -1]:
            for col in range(len(maze[0])):
                if maze[row][col] != '+' and [row, col] != entrance:
                    destinations.add((row, col))

        for col in [0, len(maze[0]) - 1]:
            for row in range(len(maze)):
                if maze[row][col] != '+' and [row, col] != entrance:
                    destinations.add((row, col))

        def inBound(row, col):
            return 0 <= row < len(maze) and 0 <= col < len(maze[0])

        level = 0
        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()

                if (row, col) in destinations:
                    return level

                for r, c in directions:
                    nr = row + r
                    nc = col + c
                    if inBound(nr, nc) and maze[nr][nc] == '.' and (nr, nc) not in visited:
                        queue.append((nr, nc))
                        visited.add((nr, nc))
            level += 1

        return -1