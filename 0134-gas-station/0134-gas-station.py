class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        curr = 0    # current gas 
        index = -1    # starting index
        neg = 0     # cost before reaching starting index  

        for i in range(len(gas)):
            curr += gas[i] - cost[i]

            if curr < 0:
                neg += curr
                index = -1
                curr = 0
            elif index == -1 and curr >= 0:
                index = i

        if curr >= abs(neg):   # if the amount of gas that i have is greater than the amount of gas that i need to reach that starting node
            return index

        return -1

        