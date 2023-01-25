class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        s += '+'
        stack = []
        num = 0
        op = '+'
        
        for i in s:
            if i.isdigit():
                num = (num*10)+int(i)
                
            else:
                num = int(num)
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop()*num)
                elif op == '/':
                    stack.append(int(stack.pop()/num))
                
                num = 0
                op = i
        return sum(stack)