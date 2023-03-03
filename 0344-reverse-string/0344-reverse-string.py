class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(s, left, right):
            if left >= right:
                return s
            else:
                s[right],s[left] = s[left], s[right]
                reverse(s,left+1,right-1)
                
        return reverse(s, 0, len(s)-1)
            
        
        
            
            
             
            
