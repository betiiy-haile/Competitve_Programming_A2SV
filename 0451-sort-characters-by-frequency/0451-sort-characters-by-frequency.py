class Solution:
    def frequencySort(self, s: str) -> str:
        ctr = Counter(s)                        
        d = list(ctr.items())                
        d.sort(key = lambda x: (-x[1], x[0]))   
        words = [ch*n for ch, n in d]           
                            
        return ''.join(words)