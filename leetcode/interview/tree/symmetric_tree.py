# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def traversal(node, levels, depth = 0):
            if len(levels) < depth + 1:
                queue = deque()
                levels.append(queue)
            else:
                queue = levels[depth]
            # if node.left or node.right:
            if node.left:
                queue.append(node.left.val)
            else:
                queue.append(None)

            if node.right:
                queue.append(node.right.val)
            else:
                queue.append(None)                

            if node.left:
                traversal(node.left, levels, depth + 1)
            if node.right:
                traversal(node.right, levels, depth + 1)                
        
        if not root:
            return True
        levels = []
        traversal(root, levels)
        # check symmetry on level entry
        for queue in levels:
            while queue:
                print(queue)
                begin = queue.popleft()
                if not queue:
                    return False
                end = queue.pop()
                if begin != end:
                    return False
        return True
