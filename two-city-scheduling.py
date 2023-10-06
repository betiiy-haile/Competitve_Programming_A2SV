class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        total  = 0
        arr  = []
        for a, b in costs:
            total += a
            arr.append(b - a)
        
        arr.sort()
        for i in range(len(costs) // 2):
            total += arr[i]

        return total