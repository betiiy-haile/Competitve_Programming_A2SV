class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        Sum = sum(stones)
        target = ceil(Sum // 2)

        def dp(index, total):
            if total >= target or index == len(stones):
                return abs(total - (Sum - total))

            if (index, total) in memo:
                return memo[(index, total)]

            memo[(index, total)] = min(dp(index + 1, total), dp(index + 1, total + stones[index]))
            return memo[(index, total)]

        memo = {}
        return dp(0, 0)