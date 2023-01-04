class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lst = []
        for i in range(len(nums)):
            if nums[i]==val:
                lst.append(i)
        lst.reverse()
        for i in lst:
            nums.pop(i)
        return len(nums)
                

        