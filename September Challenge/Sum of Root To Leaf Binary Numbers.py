class BinaryTree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def __sumRootToLeaf(root, val):
    if root == None:
        return 0
    val = val * 10 + root.data
    print("val", val)
    if root.left == None and root.right == None:
        return val
    left = __sumRootToLeaf(root.left, val)
    right = __sumRootToLeaf(root.right, val)
    print(left, right)
    sum = int(str(left), 2) + int(str(right), 2)
    print("sum", sum)
    return sum

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
