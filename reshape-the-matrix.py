class Solution(object):
    def matrixReshape(self, mat, r, c):
        ans = [[] for i in range(r)]
        col = 0
        row = 0
        if r*c != len(mat)*len(mat[0]):
           return mat
           
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                ans[row].append(mat[i][j])
                col += 1
                if col == c:
                    col = 0
                    row += 1
        return ans