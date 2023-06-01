class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(amount):
            if amount == 0:
                memo[amount] = 0
                return memo[amount]
            elif amount < 0:
                return float("inf")

            if amount in memo:
                return memo[amount]

            minPath  = float("inf")
            for coin in coins:
                minPath = min(minPath, dp(amount - coin))
            memo[amount] = minPath + 1
            return memo[amount]

        return dp(amount) if dp(amount) != float("inf") else -1