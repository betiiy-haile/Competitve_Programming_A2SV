class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        d = defaultdict(int)
        for key in words[0]:
            d[key] += 1
        
        for key in d:
            for word in words[1:]:
                if key not in word:
                    d[key] = 0
                else:
                    d[key] = min(d[key], word.count(key))
        ans = []
        for key in d:
            if d[key] > 0:
                for i in range(d[key]):
                    ans.append(key)

        return ans