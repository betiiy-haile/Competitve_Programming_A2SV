class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        target = threshold*k
        s = 0
        
        for i in range(len(arr)):
            s += arr[i]
            if i<k-1:
                continue
            if i>k-1:
                s -= arr[i-k]
            if s >= target:
                count += 1
                
        return count        
            
        