class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = sum(nums[:k])
        Sum = sum(nums[:k])
        
        for i in range(k,len(nums)):
            Sum += nums[i]
            Sum -= nums[i-k]
            maxSum = max(maxSum, Sum)
            
        return maxSum/k
        
        