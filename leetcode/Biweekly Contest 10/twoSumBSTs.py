# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        def search(root: TreeNode, val):
            d = deque((root, ))
            while d:
                node = d.popleft()
                if node is None:
                    continue
                elif node.val > val:
                    d.append(node.left)
                elif node.val < val:
                    d.append(node.right)
                else:
                    return val
            
        d = deque((root1, ))
        while d:
            node = d.popleft()
            if node is None:
                continue
            elif search(root2, target - node.val) is not None:
                return True
            d.append(node.left)
            d.append(node.right)
        return False
            