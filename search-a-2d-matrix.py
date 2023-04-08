class Solution(object):
    def searchMatrix(self, matrix, target):
        row = 0
        for i in range(1,len(matrix)):
            if target < matrix[i][0]:
                row = i-1
                break
            elif target >= matrix[i][0]:
                row = i
        for i in range(len(matrix[row])):
            if target == matrix[row][i]:
                return True
                break
        return False