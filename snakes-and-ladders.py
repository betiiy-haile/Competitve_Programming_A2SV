class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        board.reverse()

        def intToPos(position):
            row = (position - 1) // n
            col = (position - 1) % n
            if row % 2:
                col = n - 1 - col
            return [row, col]

        queue = deque()
        queue.append([1, 0])
        visited = set()

        while queue:
            pos, moves = queue.popleft()

            for i in range(1, 7):
                nextPos = pos + i
                r , c = intToPos(nextPos)
                if board[r][c] != -1:
                    nextPos = board[r][c]
                if nextPos == n * n:
                    return moves + 1
                if nextPos not in visited:
                    visited.add(nextPos)
                    queue.append((nextPos, moves + 1))

        return -1