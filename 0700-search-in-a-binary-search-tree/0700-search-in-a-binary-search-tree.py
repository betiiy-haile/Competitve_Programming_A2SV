# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def findNode(root, val):            
            if root:
                if root.val == val:
                    return root
                elif root.val < val:
                    return findNode(root.right, val)
                else:
                    return findNode(root.left, val)
            else:
                return None
        return findNode(root, val)
        