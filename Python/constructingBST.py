class node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def addNode(root, data):
    newNode = node(data)

    if root is None:
        # root = newNode
        return root

    elif data < root.val:
        if root.left is None:
            root.left = newNode
        else:
            addNode(root.left, data)

    elif data > root.val:
        if root.right is None:
            root.right = newNode
        else:
            addNode(root.right, data)

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)

root = node(10)
addNode(root, 5)
addNode(root, 15)
addNode(root, 3)
addNode(root, 7)
addNode(root, 13)
addNode(root, 17)
print("The BST is: ")
inorder(root)