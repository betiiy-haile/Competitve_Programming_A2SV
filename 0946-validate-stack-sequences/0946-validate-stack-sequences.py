class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        count = 0
        for i in pushed:
            stack.append(i)
            while stack and count<len(popped) and stack[-1] == popped[count]:            
                stack.pop()
                count += 1
                
        return count == len(popped)        
        