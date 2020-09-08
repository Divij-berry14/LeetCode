class BinaryTree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def __sumRootToLeaf(root, val):
    if root == None:
        return 0
    val = (val << 1) + root.data
    # print("val", val)
    if root.left == None and root.right == None:
        return val
    return __sumRootToLeaf(root.left, val) + __sumRootToLeaf(root.right, val)

def sumRootToLeaf(root):
    return __sumRootToLeaf(root, 0)

def print_detail_tree(root):
    if root==None:
        return
    print(root.data,end=":")
    if root.left!=None:
        print("L",root.left.data,end=",")
    if root.right!=None:
        print("R",root.right.data,end="")
    print()
    print_detail_tree(root.left)
    print_detail_tree(root.right)

def Tree_input(): #USER_INPUT
    rootData = int(input())
    if rootData == -1:
        return None
    root=BinaryTree(rootData)
    leftTree = Tree_input()
    rightTree = Tree_input()
    root.left = leftTree
    root.right = rightTree
    return root

root = Tree_input()
print_detail_tree(root)
# r = sumRootToLeaf(root)
# print("\n")
# print_detail_tree(r)
print(sumRootToLeaf(root))
