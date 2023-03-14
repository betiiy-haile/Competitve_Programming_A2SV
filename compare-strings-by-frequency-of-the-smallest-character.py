class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:           
        wordFreq = []
        queryFreq = []
        for word in words:
            C = Counter(word)
            C = sorted(C.items())
            wordFreq.append(C[0][1])

        ans = []    
        wordFreq.sort()
        n = len(words)
        for query in queries:
            C = Counter(query)
            C = sorted(C.items())
            queryFreq.append(C[0][1])
        
        for freq in queryFreq:
            left,right = 0, n-1            
            while left <= right:
                mid = (left + right) // 2
                if wordFreq[mid] <= freq:
                    left = mid + 1
                else:
                    right = mid - 1
            ans.append(n - left)
        
        return ans