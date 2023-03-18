class Solution:
    def splitString(self, s: str) -> bool:
        current = []

        def backtrack(idx):
            if idx == len(s):
                return len(current) >= 2
            for i in range(idx, len(s)):
                num = int(s[idx:i+1])
                if len(current) == 0 or current[-1] - num == 1:
                    current.append(num)
                    if backtrack(i+1):
                        return True
                    current.pop()
            return False
            
        return backtrack(0)