class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        self.cyclicSort(nums)
        print(nums)
        ans = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                ans.append(nums[i])
        return ans

    def cyclicSort(self, nums):
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1