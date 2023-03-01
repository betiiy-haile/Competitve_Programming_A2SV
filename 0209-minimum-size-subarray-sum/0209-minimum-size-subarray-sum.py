class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = float("inf")
        Sum = 0
        left = 0
        for right in range(len(nums)):
            Sum += nums[right]            
            while Sum >= target:
                minLen = min(minLen, right-left+1)
                Sum -= nums[left]
                left += 1                
                
        return minLen if minLen != float("inf") else 0 
                
        