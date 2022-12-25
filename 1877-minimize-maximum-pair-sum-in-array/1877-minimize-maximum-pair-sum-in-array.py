class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        
        i, j = 0, len(nums)-1
        while(i<j):
            ans = max(ans, nums[i]+nums[j])
            j -= 1
            i += 1
            
        return ans    
        