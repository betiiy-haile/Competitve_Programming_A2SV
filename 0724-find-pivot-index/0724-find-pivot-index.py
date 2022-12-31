class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        rightSum = sum(nums)
        
        for i,num in enumerate(nums):
            rightSum -= num
            if leftSum == rightSum:
                return i
            leftSum += num
        
        return -1