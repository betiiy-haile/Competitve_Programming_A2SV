class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        maxLen = 0
        Sum = 0
        d = defaultdict(int, {0:-1})
        if target == 0:
            return len(nums)
        for i in range(len(nums)):
            Sum += nums[i]
            if Sum-target in d:                
                maxLen = max(maxLen, i-d[Sum-target])
            if Sum not in d:
                d[Sum] = i
                
        return len(nums)-maxLen if maxLen != 0 else -1