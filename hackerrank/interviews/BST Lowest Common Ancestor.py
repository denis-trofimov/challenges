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



def lca(root, v1, v2):

    def find_path(start, key):
        path = deque()
        node = start
        while node is not None:
            path.append(node)
            if node.info == key:
                break
            elif node.info < key:
                node = node.left
            else:
                node = node.right
        return path

    path_v1 = find_path(root, v1)
    path_v2 = find_path(root, v2)
    # print(path_v1, path_v2)
    lca = None
    while path_v1 and path_v2:
        node1 = path_v1.popleft()
        node2 = path_v2.popleft()
        if node1.info == node2.info:
            lca = node1
        else:
            break
    return lca



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print (ans.info)
