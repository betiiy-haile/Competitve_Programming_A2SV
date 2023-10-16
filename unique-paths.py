class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def factorial(n):
            ans = 1
            while n > 1:
                ans *= n
                n -= 1
            return ans
            
        val = factorial(n + m - 2) 
        val2 = factorial(m - 1) * factorial(n - 1)
        return val // val2