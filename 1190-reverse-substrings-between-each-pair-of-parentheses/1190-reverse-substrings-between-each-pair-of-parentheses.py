class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        i = 0
        while(i<len(s)):
            if s[i] != ')':
                stack.append(s[i])
            else:     
                reversed_stack = []
                while stack[-1] != '(': 
                    reversed_stack.append(stack.pop()) 
                stack.pop()
                stack.extend(reversed_stack)
            i += 1
                
        return "".join(stack)
        