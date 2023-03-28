class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        new = self.cyclicSort(nums)
        for i in range(len(new)):
            if new[i] == -1:
                return i
    def cyclicSort(self, nums):
        new = [-1] * (len(nums) + 1)
        for i in range(len(nums)):
            new[nums[i]] = nums[i]
        return new