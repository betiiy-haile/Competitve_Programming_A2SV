# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        memo = defaultdict(int)
        def dp(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return node.val
            if node in memo:
                return memo[node]
            take = node.val
            notTake = 0
            if node.left:
                take += dp(node.left.left) + dp(node.left.right)
                notTake += dp(node.left)
            if node.right:
                take += dp(node.right.left) + dp(node.right.right)
                notTake += dp(node.right) 

            memo[node] = max(take, notTake)
            return memo[node]

        return dp(root)