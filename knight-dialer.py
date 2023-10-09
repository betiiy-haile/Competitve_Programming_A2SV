class Solution:
    def knightDialer(self, n: int) -> int:
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0,'#' ]]
        dir = [(2, 1), (-2, 1), (1, -2), (1, 2), (-2, -1), (-1, 2), (-1, -2), (2, -1)]

        inbound = lambda x, y : 0 <= x < len(matrix) and 0 <= y < len(matrix[0])

        @cache
        def dfs(row, col, rem):      
            if rem == 0:
                return 1             
            count = 0  
            
            for i , j in dir:
                newRow = i + row
                newCol = j + col
                if inbound(newRow, newCol) and (matrix[newRow][newCol] != '#' and  matrix[newRow][newCol] != '*'):
                    count += dfs(newRow, newCol, rem - 1)
            return count
            
        ans = 0            
        for i in range(len(matrix)):
            print(i)
            for j in range(len(matrix[0])):
                if matrix[i][j] != '*' and  matrix[i][j] != '#':
                    ans += dfs(i, j, n - 1)
        
        return ans % ((10 ** 9) + 7)