class Solution(object):
    def hammingDistance(self, x, y):
        num = x ^ y
        return self.numberOfSetBits(num)
        
    def numberOfSetBits(self, num):
        setBits = 0
        while num != 0:
            setBits += num & 1
            num = num >> 1
        return setBits