class Solution:
    def findComplement(self, num: int) -> int:
        bits = len(bin(num)) - 2
        toggler = 1
        for _ in range(bits):
            num = num ^ toggler
            toggler <<= 1
        return num