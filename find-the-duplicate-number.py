class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0

        while i < n:
            if nums[i] != nums[nums[i]-1]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        return nums[-1]