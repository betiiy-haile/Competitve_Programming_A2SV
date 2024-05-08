class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ranks = sorted(score, reverse=True)

        for i in range(len(score)):
            if score[i] == ranks[0]:
                score[i] = "Gold Medal"
            elif len(score) >= 2 and score[i] == ranks[1]:
                score[i] = "Silver Medal"
            elif len(score) >= 3 and score[i] == ranks[2]:
                score[i] = "Bronze Medal"
            else:
                score[i] = str(ranks.index(score[i]) + 1)
        print(ranks)
        return score