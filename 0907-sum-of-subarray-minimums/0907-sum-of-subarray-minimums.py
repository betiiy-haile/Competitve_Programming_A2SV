class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        ans = 0
        for right in range(len(arr)+1):                 
            while stack and (right == len(arr) or arr[right] <= arr[stack[-1]]):
                deleted = stack.pop()
                left = -1 if not stack else stack[-1]
                ans += (deleted-left) * (right-deleted) * arr[deleted]
            stack.append(right)    
        return ans %(10 ** 9 + 7)
                
                
                
            
        