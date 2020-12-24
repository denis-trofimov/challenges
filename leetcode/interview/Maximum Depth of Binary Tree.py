# You are here!
# Your runtime beats 72.46 % of python3 submissions.
# You are here!
# Your memory usage beats 12.09 % of python3 submissions.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        def traversal(node, max_depth, depth = 0):
            max_depth = max(depth, max_depth)
            if node.left:
                max_depth = traversal(node.left, max_depth, depth + 1)
            if node.right:    
                max_depth = traversal(node.right, max_depth, depth + 1)
            return max_depth
        
        if not root:
            return 0
        return traversal(root, 0)
    