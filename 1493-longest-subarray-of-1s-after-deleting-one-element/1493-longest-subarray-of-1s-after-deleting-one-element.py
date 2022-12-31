class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        ans = 0
        zeroCount = 0
        while left <= right and right < len(nums):
            if nums[right] == 0:
                zeroCount +=1
            if zeroCount > 1:
                if nums[left]==0:
                    zeroCount -=1
                left +=1
            ans = max(ans,right-left )
            right +=1
        
        return ans