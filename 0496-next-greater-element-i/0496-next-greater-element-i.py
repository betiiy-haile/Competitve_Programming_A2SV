class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in nums1:
            val = -1
            index = nums2.index(i)
            temp = nums2[index+1:]
            for j in temp:                
                if j>i:
                    val = j
                    break
            ans.append(val)       
        return ans
    
    
    
    