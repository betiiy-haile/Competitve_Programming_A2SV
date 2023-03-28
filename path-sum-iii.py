# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        d = defaultdict(int, {0:1})
        count = 0

        def Traverse(root, total):
            nonlocal d
            nonlocal count

            if root:
                total += root.val        
                if d.get(total - targetSum):
                    count += d[total - targetSum]

                d[total] += 1
                Traverse(root.left, total)
                Traverse(root.right, total)
                d[total] -= 1

        Traverse(root, 0)
        return count