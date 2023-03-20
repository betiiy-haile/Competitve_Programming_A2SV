class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        current = []
        def backtrack(idx):
            if idx == len(num) and len(current) >= 3:
                return True           
            for i in range(idx, len(num)):

                temp = num[idx:i+1]
                if len(temp) > 1 and temp[0] == '0':
                    return False
                temp = int(temp)    
                if len(current) < 2 or (current[-1] + current[-2] == temp):
                    current.append(temp)
                    if backtrack(i+1):
                        return True
                    current.pop()
            return False

        return backtrack(0)