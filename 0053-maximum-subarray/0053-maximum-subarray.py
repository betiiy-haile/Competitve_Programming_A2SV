class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curr = 0
        for i in range(len(nums)):  
            if curr < 0:
                curr = 0
            curr += nums[i]
            maxSum = max(maxSum,curr)
            
        return maxSum