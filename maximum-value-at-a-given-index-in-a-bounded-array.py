class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        maxSum -= n
        left, right = 0, maxSum
        
        while left != right:
            mid = (left + right + 1) // 2
            x = max(0, mid - index - 1)
            y = max(0, mid - n + index)

            if mid * mid <= maxSum + (x * (x + 1) + y * (y + 1)) // 2:
                left = mid
            else:
                right = mid - 1

        return right + 1