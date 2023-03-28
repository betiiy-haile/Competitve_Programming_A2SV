class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        s = set()
        def backtrack(idx, path):
            x = tuple(path)
            if len(path) >= 2 and x not in s:
                ans.append(path[:])
                s.add(x)     
            if idx < len(nums):
                if (len(path) == 0 or path[-1] <= nums[idx]):
                    path.append(nums[idx]) 
                    backtrack(idx+1, path[:])
                    path.pop() 
                backtrack(idx+1, path[:])
                
        backtrack(0,[])
        return ans