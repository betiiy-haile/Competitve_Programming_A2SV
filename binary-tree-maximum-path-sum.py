# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
                
            leftSum = max(dfs(node.left), 0)
            rightSum = max(dfs(node.right), 0)

            self.maxSum = max(self.maxSum, (node.val + leftSum + rightSum))
            return node.val + max(leftSum, rightSum)
            
        self.maxSum = float("-inf")
        dfs(root)
        return self.maxSum