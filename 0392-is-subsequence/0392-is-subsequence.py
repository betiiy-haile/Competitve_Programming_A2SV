class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def sub(i, j):
            if i == len(s):
                return True
            if j == len(t):
                return False

            if s[i] == t[j]:
                return sub(i + 1, j + 1)
            else:
                return sub(i, j + 1)

        return sub(0, 0)
    
        