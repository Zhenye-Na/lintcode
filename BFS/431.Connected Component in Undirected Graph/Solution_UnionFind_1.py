"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""
from collections import defaultdict

class UnionFind:
    def __init__(self, nodes):
        self.father = {}
        self.children = defaultdict(list)
        for node in nodes:
            self.father[node.label] = node.label
            self.children[node.label].append(node.label)

    def find(self, node):
        path = []
        while node != self.father[node]:
            path.append(node)
            node = self.father[node]
        for n in path:
            self.father[n] = node
        return node

    def union(self, nodeA, nodeB):
        rootA, rootB = self.find(nodeA), self.find(nodeB)
        if rootA != rootB:
            self.father[rootA] = rootB
            self.children[rootB].extend(self.children[rootA])
            self.children[rootA] = []


class Solution:
    """
    @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    @return {int[][]} a connected set of a undirected graph
    """
    def connectedSet(self, nodes):
        # write your code here
        uf = UnionFind(nodes)

        for node in nodes:
            for neighbor in node.neighbors:
                uf.union(node.label, neighbor.label)

        result = []
        for k, v in uf.children.items():
            if len(v) > 0:
                result.append(sorted(v))

        return result
