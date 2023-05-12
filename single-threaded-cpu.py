class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        for idx, task in enumerate(tasks):
            task.append(idx)

        tasks.sort()
        ans= []
        heap = []
        i = 0
        time = tasks[0][0]

        while heap or i < len(tasks):
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(heap, [tasks[i][1], tasks[i][2]])
                i += 1
            
            if not heap:
                time = tasks[i][0]
            else:
                procTime, index = heapq.heappop(heap)
                time += procTime
                ans.append(index)

        return ans