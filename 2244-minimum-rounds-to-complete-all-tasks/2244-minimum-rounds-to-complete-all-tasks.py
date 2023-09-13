class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freq = Counter(tasks)
        
        count = 0
        
        for key, val in freq.items():
            if val < 2:
                return -1
            if val >= 3:
                count += ceil(val / 3)
            else:
                count += val // 2
                
        return count
            
            
            
        