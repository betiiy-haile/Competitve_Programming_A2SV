class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # Bottom - UP Approach
        dp = defaultdict(int)

        for i in range(len(arr)):
            dp[arr[i]] = dp[arr[i] - difference] + 1

        return max(dp.values())