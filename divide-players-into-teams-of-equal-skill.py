class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        teamSkill = []
        left = 0
        right = len(skill) - 1
        while left < right:
            teamSkill.append(skill[left] + skill[right])
            left += 1
            right -= 1
        if len(set(teamSkill)) != 1:
            return -1
        totalSum = 0
        left = 0
        right = len(skill) - 1
        while left < right:
            totalSum += skill[left] * skill[right]
            left += 1
            right -= 1

        return totalSum