class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for i, eq in enumerate(equations):
            a, b = eq
            graph[a].append((b, values[i]))
            graph[b].append((a, 1 / values[i]))

        def bfs(start, target):
            if start not in graph or target not in graph:
                return -1

            visited = set()
            queue = deque()
            queue.append([start, 1])

            while queue:
                node, weight = queue.popleft()

                if node == target:
                    return weight

                for neigh, w in graph[node]:
                    if neigh not in visited:
                        queue.append((neigh, weight * w))
                        visited.add(neigh)

            return -1


        ans = []
        for start, end in queries:
            ans.append(bfs(start, end))

        return ans

