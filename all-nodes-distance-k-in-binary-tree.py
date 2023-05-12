# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        adjList = defaultdict(list)
        ans = []

        visited = set()
        visited.add(target.val)

        def buildList(node):
            nonlocal adjList
            if node:
                if node.left:
                    adjList[node.left.val].append(node.val)
                    adjList[node.val].append(node.left.val)                    
                if node.right:
                    adjList[node.right.val].append(node.val)
                    adjList[node.val].append(node.right.val)                    
                buildList(node.left)
                buildList(node.right)
                
        buildList(root)
       
        def getNodes(arr, k):
            nonlocal ans
            
            if k == 1:
                for i in range(len(arr)):
                    if arr[i] not in visited:
                        ans.append(arr[i])
            else:
                for i in arr:
                    if i not in visited:
                        visited.add(i)
                        getNodes(adjList[i], k-1)

        if k == 0:
            ans.append(target.val)
        else:
            getNodes(adjList[target.val], k)
        return ans