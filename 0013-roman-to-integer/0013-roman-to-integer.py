class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        curr = 0
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        for char in reversed(s):
            num = d[char]
            
            if curr > num:
                ans -= num
            else:
                ans += num

            curr = num
            
        return ans