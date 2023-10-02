class Solution:
    def minSteps(self, n: int) -> int:
        
        @cache
        def dp(length, board):
            if length == n:
                return 0
            if length > n:
                return float("inf")

            copyPaste = float("inf")
            paste = float("inf")

            copyPaste = dp(length * 2, length) + 2
            if board:
                paste = dp(length + board, board) + 1

            return min(copyPaste, paste)

        return dp(1, 0)