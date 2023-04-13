# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.Sum = 0
        self.dfs(root, -1, -1)
        return self.Sum

    def dfs(self, child, parent, grandparent):
        if not child:
            return
        if grandparent % 2 == 0:
            self.Sum += child.val
            
        self.dfs(child.left, child.val, parent)
        self.dfs(child.right, child.val, parent)