class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        memo = defaultdict(int)

        def dfs(amount):
            if amount == 0:
                return 1
            elif amount < 0:
                return 0

            if amount in memo:
                return memo[amount]
            for i in range(len(nums)):
                memo[amount] += dfs(amount - nums[i])
            return memo[amount]

        return dfs(target)