# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        nodes = []
        
        def traverse(node):
            if not node:
                return
            
            node.left = traverse(node.left)
            node.right = traverse(node.right)
            
            if node.val in to_delete:
                if node.left:
                    nodes.append(node.left)
                
                if node.right:
                    nodes.append(node.right)
                    
                return
            
            return node
        
        curr = traverse(root)
        if curr:
            nodes.append(curr)
    
        return nodes