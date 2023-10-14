class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        total = nums[0]
        for i in range(len(nums)):
            total &= nums[i]
        print(total)
        if total != 0:
            return 1
        elif total == 0 and len(set(nums)) == 1:
            return len(nums)
        else:
            count = 0
            AND = nums[0]

            for i in range(len(nums)):
                AND &= nums[i]
                if AND == 0:
                    count += 1
                    i += 1
                    if i < len(nums):
                        AND = nums[i]
                
        return count