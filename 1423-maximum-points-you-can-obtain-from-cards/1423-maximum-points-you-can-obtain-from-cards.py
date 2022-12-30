class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        m = n-k
        total = sum(cardPoints)
        min_sum = s = sum(cardPoints[:m])
        
        for i in range(k):
            s += cardPoints[m+i]
            s -= cardPoints[i]
            min_sum = min(min_sum, s)
            
        return total-min_sum     
            
            
        