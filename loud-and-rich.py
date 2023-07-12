class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        ans = [i for i in range(len(quiet))]
        adjList = defaultdict(list)
        indegree = [0] * len(quiet)

        for x, y in richer:
            adjList[x].append(y)
            indegree[y] += 1

        queue = deque()
        for i in range(len(quiet)):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            curr = queue.popleft()
            for child in adjList[curr]:
                if quiet[ans[curr]] < quiet[ans[child]] :
                    ans[child] = ans[curr]

                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)

        return ans