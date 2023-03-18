# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = defaultdict(list)
        def Traverse(root,level , n):
            nonlocal d
            if not root:
                return 
            d[level].append(n)
            Traverse(root.left , level + 1,2*n + 1)
            Traverse(root.right , level + 1 , 2*n + 2)        
        
        Traverse(root , 0 , 0)
        maxWidth = 0
        for distance in d.values():
            left = distance[0]
            right = distance[-1]
            maxWidth = max(right - left + 1 , maxWidth)
        return maxWidth