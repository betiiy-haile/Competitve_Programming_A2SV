"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        d = defaultdict(list)
        for i in range(len(employees)):
            d[employees[i].id].append(employees[i].importance)
            d[employees[i].id].append(employees[i].subordinates)            

        def dfs(empID):
            importance = d[empID][0]
            for id in d[empID][1]:
                importance += dfs(id)  
                              
            return importance

        return dfs(id)