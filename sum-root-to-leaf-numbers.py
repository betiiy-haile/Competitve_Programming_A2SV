# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def Traverse(curr, num):
            nonlocal ans
            if curr:
                if not curr.left and not curr.right:
                    ans += num*10 + curr.val
                    return
                num = num*10 + curr.val
                Traverse(curr.left, num)
                Traverse(curr.right, num)

        Traverse(root, 0)
        return ans