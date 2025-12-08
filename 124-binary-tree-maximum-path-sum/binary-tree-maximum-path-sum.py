# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-inf")
        def recursivePathSum(node):
            if node is None:
                return 0
            left_max_branch = max(recursivePathSum(node.left), 0)
            right_max_branch = max(recursivePathSum(node.right), 0)
            self.max_sum = max(self.max_sum, node.val + left_max_branch + right_max_branch)
            return node.val + max(left_max_branch, right_max_branch)

        recursivePathSum(root)
        return self.max_sum
        