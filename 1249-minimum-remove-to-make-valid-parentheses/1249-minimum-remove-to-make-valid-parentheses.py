class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        array = list(s)
        stack = []
        
        for i in range(len(array)):
            if array[i] == '(':
                stack.append(i)
            elif array[i] == ')' and len(stack):
                stack.pop()
            elif array[i] == ')':
                array[i] = ''
                
        while len(stack):
            index = stack.pop()
            array[index] = ''
            
        return ''.join(array)
                
            
 

        