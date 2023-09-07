class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        
        if mat == target:
            return True
        
        for _ in range(3):
            for i in range(n // 2):
                for j in range(i, n - 1 - i):
                    temp = mat[i][j]
                    mat[i][j] = mat[n - 1 - j][i]
                    mat[n - 1 - j][i] = mat[n - 1 - i][n - 1 - j]
                    mat[n - 1 - i][n - 1 - j] = mat[j][n - 1 - i]
                    mat[j][n - 1 - i] = temp
                    
                    if mat == target:
                        return True

                    

        return False
                
        