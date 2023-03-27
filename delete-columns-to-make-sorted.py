class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows = len(strs)
        cols = len(strs[0])
        res = 0
        for j in range(cols):
            colSorted = True
            for i in range(1,rows):
                if strs[i-1][j] > strs[i][j]:
                    print(strs[i][j])
                    colSorted = False
                    break
            if not colSorted:
                res += 1

        return res