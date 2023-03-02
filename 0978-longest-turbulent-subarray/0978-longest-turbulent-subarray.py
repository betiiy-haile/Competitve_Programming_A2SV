class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        i = j = 0
        ans = 0 
        if len(arr) == 1:
            return 1
        while j < len(arr):
            while j <len(arr)-1 and (arr[j-1]>arr[j]<arr[j+1] or arr[j-1]<arr[j]>arr[j+1]):
                j += 1
            while i < j and arr[i]==arr[i+1]:
                i += 1
            ans = max(ans, j-i+1)
            
            i = j
            j += 1
            
        return ans
        	
	

        