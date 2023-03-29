class Solution:
    def maxLength(self, arr: List[str]) -> int:
        maxLen = 0

        def backtrack(word, idx):
            nonlocal maxLen            
            if len(word) == len(set(word)):
                maxLen = max(len(set(word)), maxLen)                
            if len(word) > len(set(word)):
                return

            for i in range(idx, len(arr)):
                word += arr[i]
                backtrack(word, i+1)
                x = len(word) - len(arr[i])
                word = word[:x]
            return

        for i in range(len(arr)):
            word = arr[i]
            if len(word) == len(set(word)):
                backtrack(word, i + 1)
        
        return maxLen