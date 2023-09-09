class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(Sum):
            if Sum == target:
                return 1
            if Sum > target:
                return 0
            if Sum in memo:
                return memo[Sum]

            count = 0
            for num in nums:
                count += dp(Sum + num)

            memo[Sum] = count
            return count

        return dp(0)