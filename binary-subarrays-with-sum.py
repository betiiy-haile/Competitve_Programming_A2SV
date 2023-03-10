class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int: 
        count = 0
        Sum = 0
        d = defaultdict(int, {0:1})

        for i in range(len(nums)):
            Sum += nums[i]
            if d.get(Sum-goal):
                count += d[Sum-goal]
            d[Sum] += 1 

        return count