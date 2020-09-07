# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        S1, S2, result = [], [], []
        while root1 != None or root2 != None or len(S1) > 0 or len(S2) > 0:
            while root1 != None:
                S1.append(root1)
                root1 = root1.left
            while root2 != None:
                S2.append(root2)
                root2 = root2.left
            if len(S2) == 0 or (len(S1) > 0 and S1[-1].val <= S2[-1].val):
                root1 = S1.pop()
                result.append(root1.val)
                root1 = root1.right
            else:
                root2 = S2.pop()
                result.append(root2.val)
                root2 = root2.right

        return result;
