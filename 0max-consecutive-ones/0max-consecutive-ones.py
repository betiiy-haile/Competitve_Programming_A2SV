class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        oneCount = 0
        maxLen = 0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                oneCount += 1
                maxLen = max(maxLen, oneCount)               
            else:
                oneCount = 0
                
        return maxLen    
                
            
        