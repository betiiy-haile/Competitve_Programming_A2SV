class Solution:
    def rob(self, nums: List[int]) -> int:
        # Bottom - up Approach        

        def robHouse(nums):
            money = [0] * len(nums)
            money[0] = nums[0]
            money[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                money[i] = max(money[i - 1], money[i - 2] + nums[i])
            
            return money[-1]

        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
            
        return max(robHouse(nums[1:]), robHouse(nums[:-1]))