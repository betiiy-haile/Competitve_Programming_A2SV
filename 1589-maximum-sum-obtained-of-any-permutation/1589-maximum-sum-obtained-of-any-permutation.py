class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        preSum = [0]*len(nums)
        for start, end in requests:
            preSum[start] += 1
            if end<len(nums)-1:
                preSum[end+1] -= 1
            
        for i in range(1,len(nums)):
            preSum[i] += preSum[i-1]
            
        preSum.sort()
        nums.sort()
        ans = 0
        
        for i in range(len(nums)):
            ans += (nums[i]*preSum[i])
            
        return ans%((10**9)+7)