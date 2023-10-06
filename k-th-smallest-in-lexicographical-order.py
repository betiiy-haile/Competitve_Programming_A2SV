class Solution:
    def findKthNumber(self, n: int, k: int) -> int:

        def countNodes(n, curr):  
            Next = curr + 1
            total = 0          
            while curr <= n:
                total += min(n - curr + 1 , Next - curr)
                curr *= 10
                Next *= 10   

            return total

        curr = 1
        k -= 1

        while k:
            nodeCount = countNodes(n, curr)
            if nodeCount <= k:
                curr += 1
                k -= nodeCount                
            else:
                curr *= 10
                k -= 1
                

        return curr