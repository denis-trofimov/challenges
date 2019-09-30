class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break



# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

from collections import deque


def traverse(queue, heights_queue):
    node = queue.popleft()
    h = heights_queue.popleft()
    if node.left:
        queue.append(node.left)
        heights_queue.append(h + 1)
    if node.right:
        queue.append(node.right)
        heights_queue.append(h + 1)
    if node.left or node.right:
        return h + 1
    else:
        return h
        
def height(root):
    max_height = 0
    queue = deque((root, ))
    heights_queue = deque((0, ))
    while queue:
        max_height = max(max_height, traverse(queue, heights_queue))
            
    return max_height




tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

print(height(tree.root))
