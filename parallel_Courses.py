from collections import defaultdict, deque

def parallelCourses(n, prerequisites):
    # Write your code here.
    adjList = defaultdict(list)
    indegree = [0] * n

    for a, b in prerequisites:
        adjList[a - 1].append(b - 1)
        indegree[b - 1] += 1

    queue = deque()
    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)

    semisters = 0
    count = 0
    while queue:
        semisters += 1
        for i in range(len(queue)):
            curr = queue.popleft()
            count += 1
            for neighbour in adjList[curr]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour) 

    if count != n:
        return -1
    return semisters