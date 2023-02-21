class Solution:
    def addDigits(self, num: int) -> int:
        while num != num%10:
            digits = (int(x) for x in str(num))
            Sum = 0
            for d in digits:
                Sum += d
            num = Sum
            
        return num
        