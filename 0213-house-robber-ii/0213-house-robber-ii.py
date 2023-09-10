class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def robHouse(nums):
            rob1, rob2 = 0,0
            # [rob1, rob2, num, num + 1, ...]            
            for num in nums:
                temp = max(rob1 + num, rob2)
                rob1 = rob2
                rob2 = temp
                
            return rob2
        
        return max(nums[0], robHouse(nums[1:]), robHouse(nums[:-1]))
                
        