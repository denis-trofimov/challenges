""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
from collections import deque
def checkBST(root):
    
    def checkNode(node, l, r):
        if node is None:
            return True
        # print("current val", node.data)
        if l and node.data <= l.data:
            # print("bigger than", l.data)
            return False
        if r and node.data >= r.data:
            # print("lower than", r.data)
            return False
        return checkNode(node.left, l, node) and checkNode(node.right, node, r)
    
    return checkNode(root, None, None)
