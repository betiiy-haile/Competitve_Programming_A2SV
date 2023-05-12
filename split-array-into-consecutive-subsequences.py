class Solution:
    def isPossible(self, nums: List[int]) -> bool:

        heap = []
        for num in nums:
            
            while heap and num > heap[0][0] + 1:
                length = heapq.heappop(heap)
                if length[1] < 3:
                    return False

            if heap and num == heap[0][0] + 1:
                length = heapq.heappop(heap)
                heapq.heappush(heap, (num, length[1] + 1))
            else:
                heapq.heappush(heap, (num, 1))
                
        while heap:
            if heapq.heappop(heap)[1]<3:
                return False
        
        return True