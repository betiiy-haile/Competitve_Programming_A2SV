class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = {}
        count = 0
        
        for num in nums:
            x = k-num
            if x in counter and counter[x]>0:
                count += 1
                counter[x] -= 1
            else:
                if num not in counter:
                    counter[num] = 0
                counter[num] += 1

        
        return count           
        