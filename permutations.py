class Solution(object):
    def permute(self, nums):
        self.unique = 0
        result = []
        def helper( path):
            if len(path) == len(nums):
                result.append(path[:])

            for index in range(len(nums)):
                if self.unique & (1 << index) == 0:
                    path.append(nums[index])
                    self.unique |= 1 << index
                    helper(path[:])
                    path.pop()
                    self.unique ^= 1 << index

        
        helper([])
        return result