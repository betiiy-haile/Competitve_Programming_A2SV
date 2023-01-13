class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n > 1:
            n /= 3
            
        return True if n == 1 else False
            
        