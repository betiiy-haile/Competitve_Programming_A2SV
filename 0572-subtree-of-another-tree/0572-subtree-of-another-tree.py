# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        ans = False
        def searchNode(node, subRoot):
            nonlocal ans
            if not node:
                return None
            if node.val == subRoot.val:
                if compare(node, subRoot):
                    ans = True
                    return ans
            left = searchNode(node.left, subRoot)
            right = searchNode(node.right, subRoot)         
        
        def compare(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2 or node1.val != node2.val:
                return False
            left = compare(node1.left, node2.left)
            right = compare(node1.right, node2.right)
            return left and right
         
        searchNode(root, subRoot)
        return ans