# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def backtrack(root, arr):
            nonlocal ans
            if root:
                arr.append(root.val)

                if not root.left and not root.right:
                    if sum(arr) == targetSum:
                        ans.append(arr)
              
                    # arr.pop()
                backtrack(root.left, arr[:])                
                
                
                backtrack(root.right, arr[:])

        backtrack(root, [])
        return ans