# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        def Traverse(node):
            nonlocal ans
            if not node:
                return False
            left = Traverse(node.left)
            right = Traverse(node.right)
            curr = node==p or node==q
            if (left and right) or (curr and right) or (curr and left):
                ans = node
                return True
            return left or right or curr

        Traverse(root)
        return ans