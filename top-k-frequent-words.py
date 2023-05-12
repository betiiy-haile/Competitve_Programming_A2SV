class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if not words or k == 0:
            return []

        wordsCount = defaultdict(int)
        for word in words:
            wordsCount[word] += 1

        heap = []
        for word, freq in wordsCount.items():
            heap.append((-freq, word))
        heapq.heapify(heap)

        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])  
        return ans