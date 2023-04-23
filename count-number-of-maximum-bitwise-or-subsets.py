class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        count = 0
        maxOr = 0
        for num in nums:
            maxOr |= num

        n = 2 ** len(nums)
        for i in range(n):
            subset = []
            index = 0
            while(i):
                if i & 1 == 1:
                    subset.append(nums[index])
                i >>= 1
                index += 1
            Or =0
            for num in subset:
                Or |= num
            if Or == maxOr:
                count += 1

        return count