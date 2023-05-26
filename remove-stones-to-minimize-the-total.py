class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []

        for pile in piles:
            heapq.heappush(heap, -pile)

        while k > 0:
            curr = heapq.heappop(heap)
            heapq.heappush(heap, curr // 2)
            k -= 1

        return -sum(heap)