class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        S = set()
        left = 0
        ans = 0
        
        for right in range(len(s)):
            while s[right] in S:
                S.remove(s[left])
                left += 1
                
            S.add(s[right])
            ans = max(ans, right-left+1)
            
        return ans