# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        prevSum = 0
        totalSum = 0
        def getSum(node):
            nonlocal totalSum 
            if node:
                getSum(node.left)
                totalSum += node.val
                getSum(node.right)
            return totalSum
        
        getSum(root) 
        
        def modify(node):
            nonlocal prevSum
            nonlocal totalSum
            if node:
                modify(node.left)
                temp = node.val               
                node.val = totalSum - prevSum               
                prevSum += temp
                modify(node.right)
            return prevSum
        modify(root)
        return root
                

                
                
            