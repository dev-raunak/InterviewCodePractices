# Node to store binary tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None
    

def leftView(root, level, max_level):
    #check if root is null
    if root is None:
        return

    if level > max_level[0]:
        print(root.data)
        max_level[0] = level
        
    leftView(root.left, level+1, max_level)
    leftView(root.right, level+1, max_level)

def leftViewTree(root):
    max_level = [0]
    leftView(root, 1, max_level)

#additonal right view 
def rightView(root, level, max_level):
    if root is None:
        return

    if level > max_level[0]:
        print(root.data)
        max_level[0] = level

    rightView(root.right, level+1, max_level)
    rightView(root.left, level+1, max_level)

def rightViewTree(root):
    max_level = [0]
    rightView(root, 1, max_level)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.right = Node(6)

leftViewTree(root)
print("__________________")
print("right view tree")
rightViewTree(root)
