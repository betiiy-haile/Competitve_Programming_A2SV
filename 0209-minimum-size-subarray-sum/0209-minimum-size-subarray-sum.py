class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float("inf")
        Sum =0
        left = 0
        for right in range(len(nums)):
            Sum += nums[right]
            while Sum >= target:
                min_len = min(right-left+1, min_len)
                Sum -= nums[left]
                left += 1
                        
        return 0 if min_len==float("inf") else min_len 
                
        