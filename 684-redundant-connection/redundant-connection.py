class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent, size = [i for i in range(n)], [1] * n

        def union(a, b):
            a, b = find(a), find(b)
            if a != b:
                if size[a] < size[b]:
                    a, b = b, a
                parent[b] = a
                size[a] += size[b]

        def find(a):
            a_copy = a
            while a != parent[a]:
                a = parent[a]
            while a_copy != a:
                parent[a_copy] = a
                a_copy = parent[a_copy]
            return a

        for node1, node2 in edges:
            node1 -= 1
            node2 -= 1
            if find(node1) == find(node2):
                return [node1+1, node2+1]
            union(node1, node2)