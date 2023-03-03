class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        c = Counter(s)
        stack = []
        for i in s:
            if i not in stack:            
                while len(stack) != 0 and ord(i) < ord(stack[-1]) and c[stack[-1]] > 1 :
                    x = stack.pop()
                    c[x] -= 1
                stack.append(i)
            else:
                c[i] -= 1

        return "".join(stack)
                
            
                
            