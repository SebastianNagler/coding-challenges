# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recursiveIsValidBST(root, lower_bound, upper_bound):
            if root == None:
                return True
            if (root.val <= lower_bound) or (root.val >= upper_bound):
                return False
            return recursiveIsValidBST(root.left, lower_bound, root.val) and recursiveIsValidBST(root.right, root.val, upper_bound)
        
        return recursiveIsValidBST(root, float("-inf"), float("inf"))