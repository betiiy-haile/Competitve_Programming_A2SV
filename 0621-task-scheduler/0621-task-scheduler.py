class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxFreq = max(freq.values())
                
        freq = [value for key,value in freq.items()]
        maxFreqCount = freq.count(maxFreq)
        
        return max(len(tasks),(maxFreq-1)*(n+1)+maxFreqCount)
    
    
