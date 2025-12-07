# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nr_visited = 0
        val = None

        def recursiveKthSmallest(node: Optional[TreeNode]):
            nonlocal nr_visited, val
            if node:
                recursiveKthSmallest(node.left)
                nr_visited += 1
                if nr_visited == k:
                    val = node.val
                recursiveKthSmallest(node.right)

        recursiveKthSmallest(root)

        return val