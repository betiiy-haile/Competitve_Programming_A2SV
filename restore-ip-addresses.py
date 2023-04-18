class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        if len(s) > 12:
            return

        def backtrack(idx, dots, currIP):
            if dots == 4 and idx == len(s):
                ans.append(currIP[:-1])
                return

            for i in range(idx, min(idx + 3,len(s))):
                if int(s[idx:i+1]) < 256 and ( idx == i or int(s[idx]) != 0):
                    backtrack(i + 1, dots + 1, currIP + s[idx:i+1] + ".")

        backtrack(0, 0, "")
        return ans