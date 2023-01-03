class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # wealth = []
        customerWealth = 0
        maxWealth = 0
        for i in range(len(accounts)):
            customerWealth = sum(accounts[i])
            maxWealth = max(maxWealth, customerWealth)
            
        return maxWealth

        