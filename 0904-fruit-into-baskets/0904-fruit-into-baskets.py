class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d = defaultdict(int)
        maxLen = 0
        left = 0
        for right in range(len(fruits)):
            d[fruits[right]] += 1            
            while len(d) > 2:
                d[fruits[left]] -= 1
                if d[fruits[left]] == 0:
                    d.pop(fruits[left])
                left += 1
            maxLen = max(maxLen , right-left+1)
                
        return maxLen
    
    