class Solution:
    def jump(self, nums: List[int]) -> int:
        
        jumps = 0
        left, right = 0, 0  # to keep track of reachable window size        
        #    e.g for the first example our windows will be [0, 0], [1,  2], [3, 4]      ans = number of windows 
        
        while right < len(nums) - 1:
            farthest = 0
            
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])
                
            left = right + 1
            right = farthest
            jumps += 1
            
        return jumps