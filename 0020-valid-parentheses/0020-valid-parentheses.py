class Solution:
    def isValid(self, s: str) -> bool:
        ans = []
        d = {')':'(', '}':'{', ']':'['}
        for i in s:
            if i in d.values():
                ans.append(i)
            elif ans and (d[i] == ans[-1]):
                ans.pop()
            else:
                return False
                    
        if ans == []:
            return True
       
            
        