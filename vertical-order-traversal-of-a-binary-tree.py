# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        vertical = defaultdict(list)
        def Traverse(node, row, col):
            if not node:
                return     
            
            Traverse(node.left, row + 1, col - 1)
            vertical[col].append((row, node.val))
            Traverse(node.right, row + 1, col + 1)
        
        SortByLevel = defaultdict(list)
        Traverse(root, 0, 0)

        for c, v in vertical.items():
            for x in sorted(v):
                SortByLevel[c].append(x[1])
        
        t = list(SortByLevel.keys())
        t.sort()
        output =[ SortByLevel[i] for i in t]
        return output