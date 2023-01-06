class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans = 0
        for ice in costs:
            if ice <= coins:
                coins -= ice
                ans += 1                           
        return ans
        

        