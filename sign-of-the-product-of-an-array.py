class Solution:
    def arraySign(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = -1
            elif nums[i] > 0:
                nums[i] = 1
            else:
                nums[i] = 0

        product = 1
        for i in range(len(nums)):
            product *= nums[i]
            
        return product