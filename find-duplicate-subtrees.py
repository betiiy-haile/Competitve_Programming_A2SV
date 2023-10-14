# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        levels = defaultdict(int)
        ans = []

        def Traverse(node):
            if not node:
                return '*'

            key = str(node.val) + "-" + Traverse(node.left) + "-" + Traverse(node.right)
            if levels[key] == 1:
                ans.append(node)

            levels[key] += 1
            return key

        Traverse(root)
        return ans