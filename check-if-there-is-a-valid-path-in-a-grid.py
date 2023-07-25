class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        parent = {(i, j): (i, j) for i in range(len(grid)) for j in range(len(grid[0]))}
        size = {(i, j): 1 for i in range(len(grid)) for j in range(len(grid[0]))}

        directions = {
            1: [(0, -1), (0, 1)],
            2: [(1, 0), (-1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(-1, 0), (0, -1)],
            6: [(-1, 0), (0, 1)],
        }

        def inBound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])   

        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]

        def union(node1, node2):
            parent1 = find(node1)
            parent2 = find(node2)

            if parent1 == parent2:
                return 
            elif size[parent1] > size[parent2]:
                parent[parent2] = parent1
                size[parent1] += size[parent2]
            else:
                parent[parent1] = parent2
                size[parent2] += size[parent1]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # current cell = (i, j)
                for x, y in directions[grid[i][j]]:
                    row = i + x
                    col = j + y
                    if inBound(row, col):
                        for r, c in directions[grid[row][col]]:
                            newRow = row + r
                            newCol = col + c
                            if newRow == i and newCol == j:
                                union((i, j), (row, col))  

                           
        return find((0, 0)) == find((len(grid) - 1, len(grid[0]) - 1))