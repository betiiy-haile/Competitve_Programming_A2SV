class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
#         count = Counter(nums) 
#         for num,c in count.items():
#             if c >= n/2:
#                 return num
            
        nums.sort()
        return nums[int(n/2)]
        