# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0       
        
        def helper(curr):
            nonlocal ans
            if not curr:
                return 0
            left = helper(curr.left)
            right = helper(curr.right)
            ans = max(ans, right + left) 
            return max(left, right)+1 
        
        helper(root)
        return ans