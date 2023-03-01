class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        Sum = 0
        d = {0:1}
        for i in range(len(nums)):
            Sum += nums[i]
            
            if d.get(Sum-k):
                count += d[Sum-k]
                
            if d.get(Sum):
                d[Sum] += 1
            else:
                d[Sum] = 1
                
        return count