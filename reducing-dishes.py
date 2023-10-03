class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        satisfaction.sort()
        memo = defaultdict(int)

        def dp(index, time):
            if (index, time) in memo:
                return memo[(index, time)] 
            
            if index == len(satisfaction):
                return 0
            
            take = dp(index + 1, time + 1) + (satisfaction[index] * time)
            notTake = dp(index + 1, time)
            memo[(index, time)] = max(take, notTake)
            return memo[(index, time)]

        return dp(0, 1)