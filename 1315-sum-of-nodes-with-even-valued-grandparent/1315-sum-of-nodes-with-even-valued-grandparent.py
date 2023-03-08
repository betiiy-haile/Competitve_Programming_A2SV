# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:        
        Sum = 0
        def dfs(node, parent, gParent):
            nonlocal Sum 
            if not node:
                return            
            if gParent != -1 and gParent.val %2 == 0:
                Sum += node.val
            dfs(node.left,node, parent)
            dfs(node.right, node, parent)
       
        dfs(root, -1,-1)
        return Sum    
                
                