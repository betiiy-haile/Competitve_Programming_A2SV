class Solution:
    def maxProduct(self, words: List[str]) -> int:
        maxProduct = 0
        arrBits = []
        for i in range(len(words)):
            arrBits.append(self.getBits(words[i]))

        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if arrBits[i] & arrBits[j] == 0:
                    maxProduct = max(maxProduct, len(words[i]) * len(words[j]))
        return maxProduct

    def getBits(self, word):
        bits = 0
        for ch in word:
            shift = (ord(ch) - ord('a'))
            setBit = 1 << shift
            bits |= setBit
        return bits