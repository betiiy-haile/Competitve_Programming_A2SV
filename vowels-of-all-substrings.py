class Solution:
    def countVowels(self, word: str) -> int:
        vowels = set(list("aeiou"))
        n = len(word)

        ans = 0
        for i in range(n):
            if word[i] in vowels:
                val = (i + 1) * (n - i)
                ans += val
        
        return ans