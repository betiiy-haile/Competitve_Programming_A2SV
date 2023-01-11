class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        arr = dict(sorted(c.items(), key = lambda x: x[1], reverse=True))
        ans = list(arr.keys())
        
        
        return ans[:k]
        