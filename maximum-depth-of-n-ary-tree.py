"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        return self.dfs(root)

    def dfs(self, root):
        if not root:
            return 0
        depth = 0
        if root.children:
            for child in root.children:
                depth = max(depth, self.dfs(child))
        return depth + 1