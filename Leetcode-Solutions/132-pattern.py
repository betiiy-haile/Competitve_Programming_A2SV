class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        maxEle = float("-inf")
        for i in range(len(nums)-1,-1,-1):
            if stack and stack[-1] > nums[i] and nums[i] < maxEle:
                return True
            while stack and stack[-1] < nums[i]:
                maxEle = max(maxEle, stack.pop())
            stack.append(nums[i])
        return False
                           
        