class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for char in s:
            if stack and stack[-1][0] == char:
                last = stack[-1]
                stack.pop()
                stack.append((last[0], last[1] + 1)) 
            else:
                stack.append((char, 1))

            if stack and stack[-1][1] == k:
                stack.pop()

        ans = ""
        for char, count in stack:
            ans += (char * count)

            
        return ans