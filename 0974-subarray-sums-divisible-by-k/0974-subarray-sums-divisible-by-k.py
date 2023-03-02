class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        d = defaultdict(int, {0:1})
        Sum = 0
        
        for n in nums:
            Sum += n
            mod = Sum % k
            ans += d[mod]
            d[mod] += 1
        return ans