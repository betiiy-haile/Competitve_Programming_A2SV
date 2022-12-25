class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = []
        
        for i in range(n):
            MAX = max(arr[:n-i])
            max_index = arr.index(MAX)+1
            arr[:max_index] = reversed(arr[:max_index])
            ans.append(max_index)
            
            arr[:n-i] = reversed(arr[:n-i])
            ans.append(n-i)
            
        return ans    
            

        