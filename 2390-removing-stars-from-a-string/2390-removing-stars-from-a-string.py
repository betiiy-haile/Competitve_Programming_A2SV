class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in s:
            if stack and i == "*":
                stack.pop()
            elif i != "*":
                stack.append(i)
        
        return str("".join(stack))
            
        