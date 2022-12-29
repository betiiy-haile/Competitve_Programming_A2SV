class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left, right = 0, len(tokens)-1
        score, maxScore = 0, 0
        
        while(left<=right):
            if power >= tokens[left]:
                power -= tokens[left]
                left += 1
                score += 1
                maxScore = max(score, maxScore)
            elif score > 0:
                power += tokens[right]
                right -= 1
                score -= 1
            else:
                break;
                
        return maxScore        
                
                
        