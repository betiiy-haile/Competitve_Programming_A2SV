class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        oneStep = cost[0]
        twoStep = cost[1]
        
        for i in range(2, len(cost)):
            temp = twoStep 
            twoStep = cost[i] + min(oneStep, twoStep)
            oneStep = temp
            
        return min(oneStep, twoStep)
            

        