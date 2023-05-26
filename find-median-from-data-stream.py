class MedianFinder:

    def __init__(self):
        self.maxHeap = []     # smaller numbers
        self.minHeap = []     # larger numbers
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)
        heapq.heappush(self.minHeap, -heappop(self.maxHeap))

        if len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))        

    def findMedian(self) -> float:
        if len(self.maxHeap) != len(self.minHeap):
            return -self.maxHeap[0]
        return (-self.maxHeap[0] + self.minHeap[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()