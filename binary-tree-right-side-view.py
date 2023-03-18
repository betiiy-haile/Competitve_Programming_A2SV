# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        d = defaultdict(list)
        def Traverse(node, depth):
            if node:
                d[depth] = node.val    
                Traverse(node.left, depth+1) 
                Traverse(node.right, depth+1)   
        Traverse(root, 0)
        return d.values()