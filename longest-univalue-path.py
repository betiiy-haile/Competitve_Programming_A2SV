# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:   
        ans = 0     
        def uni (node, parent):
            nonlocal ans 
            if not node:
                return 0
            
            left = uni(node.left, node.val)
            right = uni(node.right, node.val)

            ans = max(left + right, ans)
            if node.val != parent:
                return 0
            else:
                return max(left, right) + 1
        
        uni(root, -2000)
        return ans