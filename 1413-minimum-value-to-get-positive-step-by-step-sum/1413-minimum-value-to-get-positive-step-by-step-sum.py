class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        Sum = 0
        ans = 0
        for n in nums:
            Sum = Sum + n
            ans = min(ans, Sum)
        return -ans + 1