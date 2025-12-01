# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        if self.isBalanced(root.left) and self.isBalanced(root.right):
            if root.left == None and root.right == None:
                root.val = 1
                return True
            elif root.left and root.right:
                root.val = 1 + max(root.left.val, root.right.val)
                if abs(root.left.val - root.right.val) < 2:
                    return True
            elif root.left:
                root.val = 1 + root.left.val
                if root.left.val < 2:
                    return True
            else:
                root.val = 1 + root.right.val
                if root.right.val < 2:
                    return True
        return False