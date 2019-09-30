# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        def insert(node, tree = [], index = 0):
            if not node:
                return
            if len(tree) - 1 < index:
                tree.append([node.val])
            else:
                tree[index].append(node.val)
                
            if node.left:
                insert(node.left, tree, index + 1)
            if node.right:    
                insert(node.right, tree, index + 1)
        tree = []
        insert(root, tree)
        return tree