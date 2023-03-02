class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0 
        
        for left in range(len(nums)):
            if left > 0 and nums[left] == nums[left-1]:
                continue
            right = left + 1
            while right < len(nums) and (nums[right] - nums[left]) < k:
                right += 1
                
            if right == len(nums):
                break;
            if (nums[right]-nums[left] == k):
                count += 1

        return count