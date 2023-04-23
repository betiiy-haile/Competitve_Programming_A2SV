class Solution:
    def minSteps(self, n: int) -> int:
        # finding sum of its prime factors
        ans = 0
        d = 2

        while d * d <= n:
            while n % d == 0:
                ans += d
                n /= d
            d += 1

        if n > 1:
            ans += n

        return int(ans)