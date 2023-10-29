class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prev = defaultdict(int)

        for index, val in enumerate(nums):
            rem = target - val
            if rem in prev:
                return [index, prev[rem]]
            prev[val] = index


        