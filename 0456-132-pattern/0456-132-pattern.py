class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        k = float("-inf")
        
        for i in range(len(nums)-1,-1,-1):
            if stack and stack[-1] > nums[i] and nums[i] < k:
                return True
            while stack and stack[-1] < nums[i]:
                x = stack.pop()
                k = max(k, x)
            stack.append(nums[i])
                
        return False
                    
        