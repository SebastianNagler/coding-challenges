# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while True:
            if (p.val < root.val < q.val) or (p.val > root.val > q.val) or (root.val in (p.val, q.val)):
                return root
            elif p.val < root.val:
                root = root.left
            else:
                root = root.right