class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque()
        ans = [[0]* len(mat[0]) for _ in range(len(mat))]
        
        def inBound(row, col):
            return 0 <= row < len(mat) and 0 <= col < len(mat[0]) 

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i,j))

        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()
                for i,j in directions:
                    r = row + i
                    c = col + j
                    if not inBound(r, c) or mat[r][c] == 0:
                        continue
                    ans[r][c] = ans[row][col] + 1
                    mat[r][c] = 0
                    queue.append((r, c))  

        return ans