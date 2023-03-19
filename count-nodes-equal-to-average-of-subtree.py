# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def Average(node):
            nonlocal ans
            if not node:
                return [0, 0]
            
            left, leftNodes = Average(node.left)
            right, rightNodes = Average(node.right)
            
            Sum = left + right + node.val
            count = leftNodes + rightNodes + 1
            
            if (Sum)//count == node.val:
                ans += 1
            
            return [Sum, count]
        Average(root)
        return ans