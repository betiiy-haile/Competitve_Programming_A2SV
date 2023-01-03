class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        Sum = 0
        for i in range(len(nums)):
            Sum += nums[i]
            nums[i] = Sum
            
        return nums    
            