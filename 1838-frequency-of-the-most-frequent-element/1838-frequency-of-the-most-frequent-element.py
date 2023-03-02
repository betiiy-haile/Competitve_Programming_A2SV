class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()  # O(nlogn)

        left, right = 0, 0
        freq, total = 0, 0

        while right < len(nums):
            total += nums[right]
            
            # if our window is invalid
            while nums[right]*(right-left+1) > total+k:
                total -=nums[left]
                left += 1
            freq = max(freq, right-left+1) 
            right += 1
        return freq
