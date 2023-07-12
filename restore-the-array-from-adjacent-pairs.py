class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)

        for a, b in adjacentPairs:
            adjList[a].append(b)
            adjList[b].append(a)

        def dfs(node, nums):
            nums.append(node)
            for neighbour in adjList[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    dfs(neighbour, nums)
            return nums

        visited = set()
        for num in adjList.keys():
            if len(adjList[num]) == 1:
                visited.add(num)
                return dfs(num, [])