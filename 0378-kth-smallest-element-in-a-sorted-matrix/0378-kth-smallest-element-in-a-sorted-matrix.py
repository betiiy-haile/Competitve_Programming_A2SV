class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr = []
        for i in range(len(matrix)):
            arr.extend(matrix[i])
            
        arr.sort()
        return arr[k-1]