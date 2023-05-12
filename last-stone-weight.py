class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        heap = []
        for i in range(len(stones)):
            heapq.heappush(heap, -stones[i])

        if len(stones) == 1:
            return stones[0]

        while len(heap) > 1:
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)
            heapq.heappush(heap, y - x)
            
        if heap:
            return -heap[0]            
        return 0