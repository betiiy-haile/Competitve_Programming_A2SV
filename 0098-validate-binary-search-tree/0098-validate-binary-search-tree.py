# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.checkValidity(root, float("-inf"), float("inf"))
    
    def checkValidity(self, node, minValue, maxValue):
        if not node:
            return True
        if minValue >= node.val or node.val >= maxValue:
            return False
        left = self.checkValidity(node.left, minValue, node.val)
        right =self. checkValidity(node.right, node.val, maxValue)
        return left and right