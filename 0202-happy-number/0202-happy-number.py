class Solution:
    def isHappy(self, n: int) -> bool:   
        nums = set()
        while n not in nums and n != 1:
            nums.add(n)
            Sum = 0
            digits = (int(char) for char in str(n))
            for d in digits:
                Sum += d*d
            n = Sum 
        return n == 1