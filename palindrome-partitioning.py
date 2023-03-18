class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        part = []
        def backtrack(i, ans, part):
            if i == len(s):
                ans.append(part[:]) 
                return
            for j in range(i+1,len(s) + 1):
                temp = s[i:j]
                if temp == temp[::-1]:
                    part.append(temp)
                    backtrack(j,ans,part) 
                    part.pop()
        backtrack(0,ans,part)
        return ans