class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        target = 0
        n = len(needle)
        power = n - 1

        if len(haystack) < len(needle):
            return -1

        current = 0
        for i in range(n):
            val = ord(needle[i]) - ord('a') + 1
            curr =  ord(haystack[i]) - ord('a') + 1
            target += val * (26 ** power)
            current += curr * (26 ** power)
            power -= 1

        start = 0
        for i in range(n, len(haystack)):

            if current == target:
                return start

            push = ord(haystack[i]) - ord('a') + 1 
            pop = ord(haystack[start]) - ord('a') + 1 
            current -= pop * (26 ** (n - 1))  
            current *= 26
            current += push
            start += 1
    
        if current == target:
            return start
            
        return -1