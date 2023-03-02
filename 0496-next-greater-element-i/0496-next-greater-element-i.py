class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapp = {}
        stack = []
        ans = []	
        stack.append(nums2[0])
	            
        # using stack

        for i in range(1, len(nums2)):
            while stack and nums2[i] > stack[-1]:       
                mapp[stack[-1]] = nums2[i]           
                stack.pop()                             
            stack.append(nums2[i])                      

        for element in stack:                           
            mapp[element] = -1

        for i in range(len(nums1)):
            ans.append(mapp[nums1[i]])
        return ans
    
        # ans = []
        # for i in nums1:
        #     val = -1
        #     index = nums2.index(i)
        #     temp = nums2[index+1:]
        #     for j in temp:                
        #         if j>i:
        #             val = j
        #             break
        #     ans.append(val)       
        # return ans
        
        
    
    
    
    
    
    