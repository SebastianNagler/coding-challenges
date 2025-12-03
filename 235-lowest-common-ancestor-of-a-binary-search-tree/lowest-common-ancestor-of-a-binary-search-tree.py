# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        queue = deque([root])
        parent = {root.val: None}
        while queue:
            popped_node = queue.popleft()
            for child in (popped_node.left, popped_node.right):
                if child is not None:
                    queue.append(child)
                    parent[child.val] = popped_node
        
        visited = {p.val, q.val}
        while True:
            if parent[p.val] is not None:
                p = parent[p.val]
                if p.val in visited:
                    return p
                visited.add(p.val)
            if parent[q.val] is not None:
                q = parent[q.val]
                if q.val in visited:
                    return q
                visited.add(q.val)
            
