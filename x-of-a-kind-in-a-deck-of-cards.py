class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)
        gcd = 0
        for val in count.values():
            gcd = self.gcd(gcd, val)
            if gcd == 1:
                return False 
        return True

    def gcd(self, a ,b):
        if b == 0:
            return a
        return self.gcd(b, a % b)