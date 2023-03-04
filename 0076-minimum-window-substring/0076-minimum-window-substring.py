class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount = Counter(t)
        minLen = float("inf")
        count = len(tCount)
        ans = ""
        left, right = 0,0
        
        while right < len(s):
            while right < len(s) and count != 0:
                if s[right] in tCount:
                    tCount[s[right]] -= 1
                    if tCount[s[right]] == 0:
                        count -= 1
                right += 1
                
            while left < right and count == 0:
                if right-left < minLen:
                    minLen = right-left
                    ans = s[left:right]
                if s[left] in tCount:
                    tCount[s[left]] += 1
                    if tCount[s[left]] > 0:
                        count += 1
                left += 1
                
        return ans   

            