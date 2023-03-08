# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balanced(node):
            if not node:
                return [True, 0]
            bolLeft,left = balanced(node.left)
            bolRight,right = balanced(node.right)
            if abs(left-right) > 1:
                return [False, max(left, right)+1]
            return [bolLeft and bolRight, max(left, right)+1]
                
        return balanced(root)[0]