preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]

# tree = [3,9,20,None,None,15,7]
# ans = []

# def helper(ino, pre, root):
#     ans = []
#     ans.append(pre[0])
#     left = ino[0 : ino.index(pre[0])]
#     right = ino[ino.index(pre[0])+1 : ]
#     for i in range(1, len(pre)):
#         if i in left:
#             left = ino[0 : ino.index(i)]
#             right = ino[ino.index(i)+1 : ]
#         elif i in right:
#             left = ino[0 : ino.index(i)]
#             right = ino[ino.index(i)+1 : ]