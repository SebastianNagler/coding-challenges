# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        values = []
        max_depth = -1
        def recursiveRightSideView(self, root: Optional[TreeNode], depth: int) -> List[int]:
            nonlocal values
            nonlocal max_depth
            if depth > max_depth:
                max_depth += 1
                values.append(root.val)
            if root.right:
                recursiveRightSideView(self, root.right, depth + 1)
            if root.left:
                recursiveRightSideView(self, root.left, depth + 1)
        recursiveRightSideView(self, root=root, depth=0)
        return values