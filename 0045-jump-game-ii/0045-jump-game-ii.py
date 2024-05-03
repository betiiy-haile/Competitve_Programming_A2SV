class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        curr = 0
        end = 0
        jumps = 0

        for i in range(n - 1):
            end = max(end, i + nums[i])

            if i == curr:
                jumps += 1
                curr = end

                if curr >= n - 1:
                    return jumps

        return jumps