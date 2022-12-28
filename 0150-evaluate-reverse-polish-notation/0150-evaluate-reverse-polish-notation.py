class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = []
        for i in tokens:
            if i == '+':
                result.append(result.pop() + result.pop())
            elif i == '-':
                x,y = result.pop(), result.pop()
                result.append(y-x)
            elif i == '*':
                result.append(result.pop() * result.pop())
            elif i == '/':
                x,y = result.pop(), result.pop()
                result.append(int(y/x))
            else:
                result.append(int(i))
                
        return result[0]        
        