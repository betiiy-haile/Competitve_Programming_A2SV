class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        Sum = 0
        costs.sort()
        ans = 0
        for i in costs:
            if Sum+i > coins:
                break
            ans += 1
            Sum += i
                
        return ans
        

        