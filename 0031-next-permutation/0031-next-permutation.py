class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 2:
            return nums.reverse()
        right = n-2
        while right >= 0 and nums[right] >= nums[right+1]:
            right -= 1
            
        if right == -1:
            return nums.reverse()
        
        for i in range(n-1, right, -1):
            if nums[right] < nums[i]:
                nums[i], nums[right] = nums[right], nums[i]
                break
                
        nums[right+1:] = reversed(nums[right+1:])    