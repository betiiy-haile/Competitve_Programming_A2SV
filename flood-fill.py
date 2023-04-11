class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(0,1), (0, -1), (1,0), (-1, 0)]
        visited = set() 
        oldColor = image[sr][sc]
        def inbound(row, col):
            return 0 <= row < len(image) and 0 <= col < len(image[0])

        def dfs(row, col):
            visited.add((row,col))
            image[row][col] = color
            for r,c in directions:
                newRow = row + r
                newCol = col + c
                if inbound(newRow, newCol) and (newRow, newCol) not in visited and image[newRow][newCol] == oldColor:
                    dfs(newRow, newCol)

        dfs(sr, sc)
        return image