class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = Counter(s)
        tCount = Counter(t)
        return tCount==sCount