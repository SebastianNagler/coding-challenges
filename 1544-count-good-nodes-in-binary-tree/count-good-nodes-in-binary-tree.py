# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        num_good = 0

        def recursiveGoodNodes(root: TreeNode, max_value: float):
            nonlocal num_good
            if root.val >= max_value:
                max_value = root.val
                num_good += 1
            if root.left:
                recursiveGoodNodes(root.left, max_value)
            if root.right:
                recursiveGoodNodes(root.right, max_value)

        recursiveGoodNodes(root, float("-inf"))
        return num_good