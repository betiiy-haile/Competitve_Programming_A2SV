class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums2)
        m = len(nums1)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        # print(dp)
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):

                if nums2[i] == nums1[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1                    
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]