class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        
        for i in nums1:
            if i in nums2 and i not in ans:
                ans = ans + [i]*min(nums1.count(i), nums2.count(i))
                
        return ans

		
        