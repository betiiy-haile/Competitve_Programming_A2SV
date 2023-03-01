class Solution:
    def characterReplacement(self, s: str, k: int) -> int:         
        maxLen = 0
        left = 0
        d = defaultdict(int)
        maxFreq = 0
        
        for right in range(len(s)):
            d[s[right]] += 1
            maxFreq = max(maxFreq, d[s[right]])
            while (right - left + 1) - maxFreq > k:
                d[s[left]] -= 1
                left += 1
            maxLen = max(maxLen, right - left+ 1)

        return maxLen