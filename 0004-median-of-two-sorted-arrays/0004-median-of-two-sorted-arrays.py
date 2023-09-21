class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        totalLength = n + m

        mid1, mid2 = None, None

        i, j = 0, 0

        for _ in range(totalLength // 2 + 1):
            mid2 = mid1
            if i < n and (j >= m or nums1[i] < nums2[j]):
                mid1 = nums1[i]
                i += 1
            else:
                mid1 = nums2[j]
                j += 1

        if totalLength % 2 == 0:
            return (mid1 + mid2) / 2
        else:
            return mid1 

