class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:   
        
        #  return len(set(nums)) != len(nums)
        
        nums.sort()
        if len(nums)==1:
            return False
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                return True
            continue
        return False
        