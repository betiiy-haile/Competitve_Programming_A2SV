class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for p in s:
            if p == ')':
                if stack[-1] == '(':
                    stack.pop()
                    stack.append(1)
                else:
                    val = 0
                    while stack[-1] != '(':
                        val += stack.pop()
                    stack.pop()
                    stack.append(2*val)                
            else:
                stack.append(p)
                
          
        return sum(stack)
                    