# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def updateDiameter(root):
            nonlocal diameter
            if root == None:
                return
            updateDiameter(root.left)
            updateDiameter(root.right)
            left_d = 0 if root.left == None else root.left.val
            right_d = 0 if root.right == None else root.right.val
            diameter = max(diameter, left_d + right_d)
            root.val = 1 + max(left_d, right_d)

        updateDiameter(root)

        return diameter