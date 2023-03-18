# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]: 
        d = defaultdict(int)
        def Inorder(node):
            nonlocal d
            if node:
                Inorder(node.left)
                d[node.val] += 1
                Inorder(node.right)

        Inorder(root)        
        ans = []
        for k,v in d.items():
            if v == max(d.values()):
                ans.append(k)

        return ans