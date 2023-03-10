class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        mid = (2**(n-1))//2
        if k <= mid:
            val = self.kthGrammar(n-1,k)
            return val
        else:
            val = self.kthGrammar(n-1,k-mid)
            if val == 1:
                return 0
            else:
                return 1