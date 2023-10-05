class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit = 0
        money = -prices[0]

        for i in range(1, len(prices)):
            money = max(money, profit - prices[i])
            # if i sell the stock
            profit = max(profit, money + prices[i] - fee)

        return profit