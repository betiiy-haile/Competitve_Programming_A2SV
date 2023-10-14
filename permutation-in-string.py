class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1Count = defaultdict(int)
        s2Count = defaultdict(int)
        
        if len(s1) > len(s2):
            return False
        
        for i in range(len(s1)):
            s1Count[s1[i]] += 1
            s2Count[s2[i]] += 1
            
        if s1Count == s2Count:
            return True
        
        i = 0
        for j in range(len(s1), len(s2)):
            s2Count[s2[j]] += 1
            s2Count[s2[i]] -= 1
            
            if s2Count[s2[i]] == 0:
                s2Count.pop(s2[i])
            i += 1
            if s1Count == s2Count:
                return True
            
        return False