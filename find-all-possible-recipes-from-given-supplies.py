class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adjList = defaultdict(list)
        incoming = defaultdict(int)

        for i, arr in enumerate(ingredients):
            incoming[recipes[i]] = len(arr)
            for x in arr:
                adjList[x].append(recipes[i])

        ans = []
        queue = deque(supplies)
        while queue:
            curr = queue.popleft()
            for recipe in adjList[curr]:
                incoming[recipe] -= 1
                if incoming[recipe] == 0:
                    ans.append(recipe)
                    queue.append(recipe)
                
        return ans