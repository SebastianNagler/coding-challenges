binary_tree = TreeNode('init')
inorder_dict = 'empty'
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder = deque(preorder)
        n = len(inorder)
        in_map = {inorder[i]: i for i in range(n)}

        def recursiveBuildTree(preorder, in_low, in_high):
            if in_low > in_high:
                return None
            node = TreeNode(preorder.popleft())
            node.left = recursiveBuildTree(preorder, in_low, in_map[node.val]-1)
            node.right = recursiveBuildTree(preorder, in_map[node.val]+1, in_high)
            
            return node

        return recursiveBuildTree(preorder, 0, n-1)