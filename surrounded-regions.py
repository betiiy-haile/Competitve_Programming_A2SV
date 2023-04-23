class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        visited = set()
        def inbound(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])

        def dfs(row, col):
            if inbound(row, col) and board[row][col] == 'O':
                if (row, col) not in visited:
                    visited.add((row, col))
                    for r,c in directions:
                        dfs(row + r, col + c)

        for row in [0,len(board)-1]:
            for col in range(len(board[0])):
                dfs(row, col)

        for col in [0, len(board[0])-1]:
            for row in range(len(board)):
                dfs(row, col)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i, j) not in visited and board[i][j] == 'O':
                    board[i][j] = 'X'