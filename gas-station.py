class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        curr = 0
        index = -1
        neg = 0


        for i in range(len(gas)):
            curr += gas[i] - cost[i]

            if curr < 0:
                neg += curr
                curr = 0
                index = -1
            elif index == -1 and curr >= 0:
                index = i

        if curr >= abs(neg):
            return index

        return -1