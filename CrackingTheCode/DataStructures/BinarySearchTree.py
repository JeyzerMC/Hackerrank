""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def inOrderAppend(root, a):
    if root.left is not None:
        inOrderAppend(root.left, a)
    a.append(root.data)
    if root.right is not None:
        inOrderAppend(root.right, a)
    return

def checkBST(root):
    a = []
    inOrderAppend(root, a)
      
    if a == sorted(a) and len(a) == len(set(a)):
        return True
    return False
