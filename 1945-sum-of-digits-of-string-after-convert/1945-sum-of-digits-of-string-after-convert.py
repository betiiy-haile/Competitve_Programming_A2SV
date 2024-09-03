class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = ""
        
        for ch in s:
            num += str(ord(ch) - ord("a") + 1)
            
            
        while k > 0:
            Sum = 0
            for ch in num:
                Sum += int(ch)
            num = str(Sum)
            k -= 1
        
        return int(num)
            
            
        
        