class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # non recursive approach
        # while n > 1:
        #     n /= 3            
        # return True if n == 1 else False
               

        # recursive approach
        if n <= 0:
            return False
        if n == 1:
            return True 
        if n % 3 != 0:
            return False
        return self.isPowerOfThree(n//3)
            
        