class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        area = 0
        for i,h in enumerate(height):
            while stack and stack[-1][1] <= h:
                top = stack.pop()
                if stack:
                    H =min(stack[-1][1], h) - top[1]
                    W = i - stack[-1][0] - 1
                    area += H*W
            stack.append([i,h])
        return area