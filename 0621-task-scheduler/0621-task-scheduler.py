class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq ={}
        for task in tasks:
            if task not in freq:
                freq[task] = 1
            else:
                freq[task] += 1
                
        freq = [value for key,value in freq.items()]
        maxFreq = max(freq)
        maxFreqCount = freq.count(maxFreq)
        
        return max(len(tasks),(maxFreq-1)*(n+1)+maxFreqCount)
