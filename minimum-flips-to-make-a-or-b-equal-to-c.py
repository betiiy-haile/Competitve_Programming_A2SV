class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        while a > 0 or b > 0 or c > 0:
            bitA = a & 1 
            bitB = b & 1
            bitC = c & 1

            if bitC == 0:
                ans += (bitA + bitB)
            else:
                if bitA == 0 and bitB == 0:
                    ans += 1


            a >>= 1
            b >>= 1
            c >>= 1

        return ans