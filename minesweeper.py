class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        self.directions = [(-1,-1), (-1,0), (-1,1),(0, -1), (0, 1),(1,-1),(1,0),(1,1)]
        self.board = board
        x,y = click        
        if board[x][y] == 'M':
            board[x][y] = 'X'
        else:
            numMines = self.getAdjacentMines(board, x, y)
            if numMines:
                board[x][y] = str(numMines)
            else:
                board[x][y] = "B"
                for r,c in self.directions:
                    row = x + r
                    col = y + c
                    if self.inbound(row, col) and board[row][col] != "B":
                        self.updateBoard(board, [row, col])

        return self.board

    def inbound(self, row, col):
            return 0 <= row < len(self.board) and 0 <= col < len(self.board[0])

    def getAdjacentMines(self, board, x, y):

        numMines = 0
        for r,c in self.directions:
            row = x + r
            col = y + c
            if self.inbound(row, col) and board[row][col] == "M":
                numMines += 1

        return numMines