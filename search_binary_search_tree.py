""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

# In-order traversal: left -> root -> right

def check(root, left_d, right_d):
    if root is None:
        return True
    if root.data <= left_d or root.data >= right_d:
        return False
    return check(root.left, left_d, root.data) and check(root.right, root.data, right_d)

def checkBST(root):
    return check(root, 0, 10000)
