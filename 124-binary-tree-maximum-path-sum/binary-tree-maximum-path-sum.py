# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")
        def recursivePathSum(node):
            nonlocal max_sum
            if node is None:
                return 0
            left_max_branch = recursivePathSum(node.left)
            right_max_branch = recursivePathSum(node.right)
            max_sum = max(max_sum, node.val + max(0, left_max_branch) + max(0, right_max_branch))
            return node.val + max(left_max_branch, right_max_branch, 0)

        recursivePathSum(root)
        return max_sum
        