class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        maxCount = 0

        for r,x in enumerate(s):
            if x in "aeiou":
                count += 1
            if r >= k and s[r-k] in "aeiou":
                count -= 1
            maxCount = max(maxCount, count) 

        return maxCount    
 
                