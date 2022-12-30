class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_len = 0
        left = 0
        unique = 0
        counter = Counter()
        
        for right in range(len(fruits)):
            counter[fruits[right]] += 1
            
            if counter[fruits[right]] == 1:
                unique += 1
                
            while unique > 2:
                counter[fruits[left]] -= 1                
                if counter[fruits[left]] == 0:
                    unique -= 1
                left += 1
            curr_len = right - left + 1
            max_len = max(max_len,curr_len)
            
        return max_len    