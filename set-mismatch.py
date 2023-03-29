class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result = []
        nums = self.cyclicSort(nums)
        for i in range(len(nums)):
            if nums[i]-1 != i:
                result.append(nums[i])
                result.append(i+1)
        return result

    def cyclicSort(self, nums):
        i = 0
        while i < len(nums):
            num = nums[i]-1
            if i != num and nums[num] != nums[i]:
                nums[i],nums[num] = nums[num],nums[i]
            else:
                i += 1
        return nums