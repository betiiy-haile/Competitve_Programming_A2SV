class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset = []
        nums.sort()
        def backtrack(i,path):
            if i == len(nums):
                subset.append(path[:])
                return
            path.append(nums[i])
            backtrack(i+1, path[:])
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i += 1
            path.pop()
            backtrack(i+1, path[:])

        backtrack(0,[])
        return subset