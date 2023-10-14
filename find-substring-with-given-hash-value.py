class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        powers = [1]

        for idx in range(k - 1):
            powers.append(powers[-1] * power)

        currHash = 0
        for i in range(k):
            val = ord(s[i]) - ord('a') + 1
            currHash += (val * powers[i])  
        
        start = 0        
        for i in range(k, len(s)):
            if currHash % modulo == hashValue:
                return s[start:i]

            begin = ord(s[start]) - ord('a') + 1
            currHash = (currHash - begin) // power 
            
            end = ord(s[i]) - ord('a') + 1            
            currHash += (end * powers[-1]) 
            start += 1

        
        if currHash % modulo == hashValue:
            return s[start:i + 1]