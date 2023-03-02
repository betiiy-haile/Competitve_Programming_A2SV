class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        left = 0

        for right in range(len(prices)):            
            if prices[right] <= prices[left]:
                left = right
            maxProfit = max(maxProfit, prices[right] - prices[left])
        
        return maxProfit