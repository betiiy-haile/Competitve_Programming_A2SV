class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        for a in zip(*strs):
            if len(set(a)) == 1: 
                ans += a[0]
            else: 
                return ans
        return ans