class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # return set(range(1, len(nums) + 1)) - set(nums)
        self.cyclicSort(nums)
        ans = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                ans.append(i+1)
        return ans

    def cyclicSort(self, nums):
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1