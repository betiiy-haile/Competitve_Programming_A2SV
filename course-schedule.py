class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        incomingEdges = defaultdict(int)
        queue = deque()
        ans = []

        for course, pre in prerequisites:
            adjList[pre].append(course)
            incomingEdges[course] += 1

        for course in range(numCourses):
            if incomingEdges[course] == 0:
                queue.append(course)

        while queue:
            curr = queue.popleft()
            ans.append(curr)
            for child in adjList[curr]:
                incomingEdges[child] -= 1
                if incomingEdges[child] == 0:
                    queue.append(child)

        if len(ans) != numCourses:
            return False
        return True