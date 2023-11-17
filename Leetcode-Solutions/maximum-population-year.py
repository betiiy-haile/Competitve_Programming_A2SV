class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = [0] * 101
        for birth, death in logs:            
            years[birth - 1950] += 1
            years[death - 1950] -= 1

        maxPopulation = years[0]
        maxYear = 1950
        for i in range(1, 101):
            years[i] += years[i - 1]
            if years[i] > maxPopulation:
                maxPopulation = years[i]
                maxYear = 1950 + i

        return maxYear