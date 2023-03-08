# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def getVal(node,val):
            nonlocal ans
            if node:
                if not node.left and not node.right:
                    ans.append(val + str(node.val))
                    return 
                val += str(node.val) + "->"
                getVal(node.left, val)
                getVal(node.right, val)
                      
        getVal(root, "")
        return ans