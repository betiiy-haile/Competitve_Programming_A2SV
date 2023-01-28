class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        S = str(num)
        count = 0
        for i in range(k,len(S)+1):
            x = int(S[i-k:i])
            if x != 0 and num % x == 0:
                count += 1
        return count