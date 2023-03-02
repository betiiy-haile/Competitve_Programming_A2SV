class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()   
        
        Sum = 0
        for i in range(0,len(nums),2):
            Sum += min(nums[i],nums[i+1])
        return Sum