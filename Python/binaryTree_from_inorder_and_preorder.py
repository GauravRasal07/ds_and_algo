preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

tree = [3,9,20,None,None,15,7]
# ans = []

def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None
    root = preorder[0]
    root_index = inorder.index(root)
    left_tree = buildTree(preorder[1:root_index+1], inorder[:root_index])
    right_tree = buildTree(preorder[root_index+1:], inorder[root_index+1:])
    return [root, left_tree, right_tree]

print("Solution: ", buildTree(preorder, inorder))

# idx = 0

# class Node:

#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


# def inorderTraversal(root):
#     if root == None:
#         return

#     inorderTraversal(root.left)
#     print(root.val, end=" ")
#     inorderTraversal(root.right)    


# def buildTree(ino, pre, start, end):
#     global idx
#     if start > end or idx == len(pre):
#         return None

#     curr = pre[idx]

#     idx += 1

#     node = Node(curr)

#     if start == end:
#         return node

#     pos = ino.index(curr)
#     print("Pos: ", pos)
#     node.left = buildTree(ino, pre, start, pos - 1)
#     node.right = buildTree(ino, pre, pos + 1, end)

#     return node 


# # def temp():
# #     idx += 1
# #     print("Idx: ", idx)


# newNode = buildTree(inorder, preorder, 0, len(inorder))
# print("The inorder traversal of answer is: ")
# inorderTraversal(newNode)
# temp()