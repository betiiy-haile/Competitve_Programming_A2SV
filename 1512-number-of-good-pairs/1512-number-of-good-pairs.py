class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = len(nums)
        ans = []
        for i in range(n):
            for j in range(i,n):
                if nums[i] == nums[j] and i < j:
                    ans.append([i,j])

        return len(ans)            