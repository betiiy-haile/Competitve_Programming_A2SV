class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        parent = {(x,y):(x,y) for x in range(row) for y in range(col)}
        size = {(x,y):1 for x in range(row) for y in range(col)}
        dxns = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,-1), (-1,1), (1,-1)]
        visited = set()
        
        def find(x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parentx = find(x)
            parenty = find(y)
            
            if parentx == parenty:
                return
            if size[parentx] > size[parenty]:
                parent[parenty] = parentx
                size[parentx] += size[parenty]
            else:
                parent[parentx] = parenty
                size[parenty] += size[parentx]

        parent[0], parent[-1] = 0, -1
        size[0], size[-1] = 1, 1
        
        count = 0
        for r, c in cells:
            r -= 1
            c -= 1
            for x, y in dxns:
                newRow = r + x
                newCol = c + y

                if 0 <= newRow < row:
                    if 0 <= newCol < col:
                        if (newRow, newCol) in visited:
                            union((newRow, newCol), (r, c))
                    else:
                        if newCol == -1:
                            union((r, c), 0)
                        elif newCol == col:
                            union((r, c), -1)

                if find(0) == find(-1):
                    return count
                visited.add((r, c))
            count += 1

        return col