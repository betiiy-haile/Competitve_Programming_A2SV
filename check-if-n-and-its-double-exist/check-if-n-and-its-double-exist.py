class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        i = 0
        while i<len(arr):
            for j in range(len(arr)):
                if i != j and arr[i] == 2*arr[j]: 
                        return True
            i += 1
     
        