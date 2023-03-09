class Solution:
    def balancedString(self, s: str) -> int:
        C = Counter(s)
        minLen = len(s)
        x = len(s)//4
        left, right = 0, 0
        
        for right in range(len(s)):
            C[s[right]] -= 1
            while left < len(s) and C['Q'] <= x and C['W'] <= x and C['E'] <= x and C['R'] <= x:          
                minLen = min(minLen, right-left+1) 
                C[s[left]] += 1
                left += 1
                
        return minLen