class Solution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        self.num_provinces = n
        self.parent = list(range(n))
        self.size = [1] * n
        for row in range(n):
            for column in range(row + 1, n):
                if isConnected[row][column]:
                    self.union(row, column)
        return self.num_provinces

        
    def findRoot(self, node_idx):
        node_idx_copy = node_idx
        while node_idx != self.parent[node_idx]:
            node_idx = self.parent[node_idx]
        while node_idx != node_idx_copy:
            node_idx_copy = self.parent[node_idx_copy]
            self.parent[node_idx_copy] = node_idx
        return node_idx

    def union(self, node1, node2):
        node1, node2 = self.findRoot(node1), self.findRoot(node2)
        if node1 != node2:
            if self.size[node1] < self.size[node2]:
                node1, node2 = node2, node1
            self.parent[node2] = node1
            self.num_provinces -= 1
            self.size[node1] += self.size[node2]