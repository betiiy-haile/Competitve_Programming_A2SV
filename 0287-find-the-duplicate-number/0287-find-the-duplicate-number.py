class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = Counter(nums)
        for v,c in count.items():
            if c >= 2:
                return v
