class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = 0
        def mergeSort(nums, left, right):
            if left == right:
                return [nums[left]]
            mid = left + (right -left) // 2
            left = mergeSort(nums, left, mid)
            right = mergeSort(nums, mid+1, right)
            return merge(left, right)

        def merge(left, right):
            nonlocal count
            i = 0
            j = 0
            while i < len(left):
                while j < len(right) and left[i] > 2 * right[j]:
                    j += 1
                else:
                    count += j
                    i += 1

            merged = []  
            i = 0
            j  = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            while i < len(left):
                merged.append(left[i])
                i += 1
            while j < len(right):
                merged.append(right[j])
                j += 1

            return merged
        mergeSort(nums, 0, len(nums)-1)
        return count