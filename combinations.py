class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
       combinations = []

       def backtrack(curr, path, k):
            if len(path) == k:
               combinations.append(path[:])
               return 
            if curr <= n:
                path.append(curr)
                backtrack(curr+1, path[:], k)
                path.pop()
                backtrack(curr+1, path[:], k)
        
       backtrack(1, [], k)
       return combinations