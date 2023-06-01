class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(arr, target):
            if len(arr) == 0:
                return 1 if target == 0 else 0
            if (tuple(arr), target) in memo: 
                return memo[(tuple(arr), target)]
            memo[(tuple(arr), target)] = dp(arr[1:], target - arr[0]) + dp(arr[1:], target + arr[0])
            return memo[(tuple(arr), target)]
                      
        return dp(nums, target)