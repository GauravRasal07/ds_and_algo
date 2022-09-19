def invertTree(root):
    if root == None:
        return
    
    invertTree(root.left)
    invertTree(root.right)
    
    root.left, root.right = root.right, root.left
    return root

