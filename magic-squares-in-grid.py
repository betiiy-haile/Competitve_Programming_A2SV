class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                subgrid = [grid[i][j:j+3], grid[i+1][j:j+3], grid[i+2][j:j+3]]
                if self.isMagicSquare(subgrid):
                    count += 1
        return count
        
    def isMagicSquare(self, subGrid):
        subgridList = [num for row in subGrid for num in row]
        if sorted(subgridList) != [x for x in range(1, 10)]:
            return False

        rowSum = sum(subGrid[0])
        for row in subGrid:
            if sum(row) != rowSum:
                return False

        col1 = [row[0] for row in subGrid]
        col2 = [row[1] for row in subGrid]
        col3 = [row[2] for row in subGrid]
        if sum(col1) != rowSum or sum(col2) != rowSum or sum(col2) != rowSum:
            return False
        
        diagonal1 = [subGrid[i][i] for i in range(3)]
        diagonal2 = [subGrid[i][2-i] for i in range(3)]
        if sum(diagonal1) != rowSum or sum(diagonal2) != rowSum:
            return False

        return True