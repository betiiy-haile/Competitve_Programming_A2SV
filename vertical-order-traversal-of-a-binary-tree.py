# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        vertical = defaultdict(list)

        def frustrating(node, row, col) :
            if not node:
                return        
            
            frustrating(node.left, row + 1, col - 1)
            vertical[col].append((row, node.val))
            # vertical[col].sort()
            frustrating(node.right, row + 1, col + 1)
        
        tired = defaultdict(list)

        frustrating(root, 0, 0)

        for c, v in vertical.items():
            for x in sorted(v):
                tired[c].append(x[1])
        
        t = list(tired.keys())
        t.sort()
        output =   [ tired[i] for i in t]



        # print(vertical)
        return output