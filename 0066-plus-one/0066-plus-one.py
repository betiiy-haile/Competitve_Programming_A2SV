class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for d in digits:
            num += str(d)
            
        num = str(int(num) + 1)        
        arr = []
        for i in num:
            arr.append(int(i))            
        return arr
        
        