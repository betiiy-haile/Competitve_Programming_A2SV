class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if nums[n-1]<target:
            return n
        
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
            
                