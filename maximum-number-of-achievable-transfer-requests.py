class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        ans =  0   
        buildings = [0] * n

        def backtrack(idx, curr, buildings):
            nonlocal ans
            
            if idx >= len(requests):
                return
            
            for i in range(idx, len(requests)):
                curr.append(requests[i])
                src, dest = requests[i]
                buildings[src] -= 1
                buildings[dest] += 1
                
                if all(net == 0 for net in buildings):
                    ans = max(ans, len(curr))
                
                backtrack(i + 1, curr, buildings)
                
                request = curr.pop()
                src, dest = request
                buildings[src] += 1
                buildings[dest] -= 1
            
            return
        
        backtrack(0, [], buildings)
        
        return ans