class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = ((10 ** 9) + 7)

        def power(base, exponent):
            result = 1
            power = abs(exponent)

            while power > 0:
                if power & 1:
                    result = (result * base) % mod
                base = (base * base) % mod
                power >>= 1
                
            return int(result) if exponent > 0 else int(1 / result)

        if n % 2 == 0:
            n //= 2 
            ans = power(5, n) * power(4 , n)
        else:
            n //= 2
            ans = power(5, n + 1) * power(4, n)

        return ans % mod