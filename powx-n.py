class Solution:
    def myPow(self, base: float, exponent: int) -> float:

        result = 1
        power = abs(exponent)

        while power > 0:
            if power & 1:
               result *= base
            base *= base
            power >>= 1
             
        return result if exponent > 0 else 1 / result