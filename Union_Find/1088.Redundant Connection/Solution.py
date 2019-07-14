class UnionFind:

    def __init__(self, n):
        self.parent = {i: i for i in range(1, n + 1)}

    def find(self, node):
        path = []
        while node != self.parent[node]:
            path.append(node)
            node = self.parent[node]

        for p in path:
            self.parent[p] = node

        return node

    def union(self, node1, node2):
        parent1, parent2 = self.find(node1), self.find(node2)
        if parent1 != parent2:
            self.parent[max(parent1, parent2)] = min(parent1, parent2)
            return False

        return True


class Solution:
    """
    @param edges: List[List[int]]
    @return: List[int]
    """

    def findRedundantConnection(self, edges):
        # write your code here
        if not edges or len(edges) == 0:
            return [0, 0]

        ans = []
        max_node = -1
        for edge in edges:
            max_node = max(max_node, max(edge))

        uf = UnionFind(max_node)
        for edge in edges:
            res = uf.union(edge[0], edge[1])
            if res:
                ans.append(edge)

        return ans.pop() if ans else [0, 0]
