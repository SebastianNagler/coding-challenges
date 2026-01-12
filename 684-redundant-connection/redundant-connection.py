class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent, size = [i for i in range(n)], [1] * n

        def union(a, b):
            nonlocal parent, size
            a, b = find(a), find(b)
            if a != b:
                if size[a] < size[b]:
                    a, b = b, a
                parent[b] = a
                size[a] += size[b]

        def find(a):
            nonlocal parent
            a_copy = a
            while a != parent[a]:
                a = parent[a]
            while a_copy != a:
                parent[a_copy] = a
                a_copy = parent[a_copy]
            return a

        def was_visited(node):
            nonlocal parent
            return parent[node] != node or size[node] > 1

        for node1, node2 in edges:
            node1 -= 1
            node2 -= 1
            if was_visited(node1) and was_visited(node2) and find(node1) == find(node2):
                return [node1+1, node2+1]
            union(node1, node2)