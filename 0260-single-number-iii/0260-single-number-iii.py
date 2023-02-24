class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:        
        nums.sort()        
        ans = []
        
        for i in range(len(nums)):
            if (i and nums[i] == nums[i-1]) or (i+1 < len(nums) and nums[i] == nums[i+1]):
                continue
            else:
                ans.append(nums[i])
        return ans