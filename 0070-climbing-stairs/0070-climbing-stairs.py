class Solution:
    def climbStairs(self, n: int) -> int:
        
        @cache
        def dp(index):
            if index > n:
                return 0
            if index == n:
                return 1
            one = dp(index + 1)
            two = dp(index + 2)
            return one + two
        
        return dp(0)
            
            