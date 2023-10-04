class Trie:
    def __init__(self, bitLength):
        self.root = {}
        self.bitLength = bitLength 

    def insert(self, num) -> None:
        node = self.root

        for i in range(self.bitLength, -1, -1):
            bit = (num >> i) & 1
            if bit not in node:
                node[bit] = {}
            
            node = node[bit]
    
    def getMaxXOR(self, num):
        node = self.root
        xor = 0

        for i in range(self.bitLength, -1, -1):
            bit = (num >> i) & 1

            if (1 - bit) in node:
                xor += 2 ** i
                node = node[1 - bit]
            else:
                node = node[bit]    

        return xor

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        bitLength = int.bit_length(max(nums))
        trie = Trie(bitLength)

        for num in nums:
            trie.insert(num)

        ans = 0
        for num in nums:
            xor = trie.getMaxXOR(num)
            ans = max(ans, xor)
        
        return ans