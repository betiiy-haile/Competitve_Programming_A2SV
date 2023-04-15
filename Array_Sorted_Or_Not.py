class Solution:
    def arraySortedOrNot(self, arr, n):
        
        left = 0
        right =1
        while right < len(arr):
            if arr[left] > arr[right]:
                return 0
            left+=1
            right+=1
        return 1