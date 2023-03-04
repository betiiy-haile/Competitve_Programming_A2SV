class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = []       
    
        def leftIndex(nums, target):
            index = -1
            left = 0
            right = len(nums)-1
            while left <= right:
                mid = left+(right-left)//2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1                
                if nums[mid] == target:
                    index = mid
            return index
        
        def rightIndex(nums, target):
            index = -1
            left = 0
            right = len(nums)-1
            while left <= right:
                mid = left+(right-left)//2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
                if nums[mid] == target:
                    index = mid
            return index
        
        ans.append(leftIndex(nums,target))
        ans.append(rightIndex(nums,target))
        return ans
                    

