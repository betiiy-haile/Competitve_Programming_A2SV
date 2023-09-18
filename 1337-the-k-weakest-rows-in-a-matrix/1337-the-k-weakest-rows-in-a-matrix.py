class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        RowSum = []
        for i in range(len(mat)):
            Sum = sum(mat[i])
            RowSum.append([i, Sum])
            
        RowSum.sort(key=lambda x: x[1])
        ans = []
        for index, Sum in RowSum:
            ans.append(index)
        return ans[:k]
            