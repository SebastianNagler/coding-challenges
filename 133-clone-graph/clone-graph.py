"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        visited = dict()
        def dfs(cloned_node):
            clone_node = Node(cloned_node.val)
            visited[cloned_node.val] = clone_node
            for cloned_child in cloned_node.neighbors:
                if cloned_child.val in visited:
                    clone_node.neighbors.append(visited[cloned_child.val])
                else:
                    clone_node.neighbors.append(dfs(cloned_child))
            return clone_node

        return dfs(node)