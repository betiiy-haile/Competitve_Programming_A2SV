class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c = Counter(arr)
        n = len(arr)
        x = 0
        ans = 0
        
        for i,j in sorted(c.items(), key = lambda x: -x[1]):
            x += j
            ans += 1
            if x >= n//2:
                break
                
        return ans        
        
        
        