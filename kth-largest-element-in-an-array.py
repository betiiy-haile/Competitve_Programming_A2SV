class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        k = len(nums) - k

        def quickSort(left, right):
            pivot = nums[right]
            p = left

            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1

            nums[p], nums[right] = nums[right], nums[p]

            if p > k:
                return quickSort(left, p - 1)
            elif p < k:
                return quickSort(p + 1, right)
            else:
                return nums[p]

        return quickSort(0, len(nums)-1)