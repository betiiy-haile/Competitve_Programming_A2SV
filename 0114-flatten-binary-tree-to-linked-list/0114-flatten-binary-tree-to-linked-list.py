# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def preOrder(root):
            if not root:
                return
            left = root.left
            right = root.right
            
            preOrder(left)
            root.right = left
            root.left = None
            
            preOrder(right)
            while root.right:
                root = root.right
                
            root.right = right
            return root
        
        preOrder(root)
                
        