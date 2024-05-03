class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        
        for i in range(len(nums) - 2, -1,  -1):
            if i + nums[i] >= target:
            #   this means i can reach target from the position i so my next terget will be i itself
                target = i
                
        return True if target == 0 else False
            