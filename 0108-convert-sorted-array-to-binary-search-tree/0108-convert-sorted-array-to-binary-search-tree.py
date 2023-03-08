# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]: 
        return self.help(nums, 0, len(nums)-1)
        
    def help(self,arr, start, end):
        if start > end:
            return 
        if start == end:
            return TreeNode(arr[start])
        
        mid = start + (end-start)//2 
        newNode = TreeNode(arr[mid])
        newNode.left = self.help(arr,start,mid-1)
        newNode.right = self.help(arr,mid+1,end)
        return newNode
            

            