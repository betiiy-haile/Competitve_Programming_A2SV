class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        heap = []
        for x in nums1:
            for y in nums2:
                if len(heap) < k:
                    heapq.heappush(heap, (-(x + y), x, y))
                elif heap[0][0] < -(x + y):
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-(x + y), x, y))
                else:
                    break

        ans = []
        for x, y, z in heap:
            ans.append([y, z])

        return ans