class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                nums[i-1] = 2 * nums[i]
                nums[i] = 0

        left = 0
        while left < len(nums) and nums[left] != 0:
            left += 1
        if left < len(nums):
            for right in range(left+1, len(nums)):
                if nums[right] != 0:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1

        return nums