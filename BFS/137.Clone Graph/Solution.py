"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        # write your code here
        if node is None:
            return None

        # get all the nodes in the graph
        nodes = self._get_nodes(node)

        # map from original node to new node
        mapping = dict()

        # copy ndoes
        for graphNode in nodes:
            mapping[graphNode] = UndirectedGraphNode(graphNode.label)

        # copy edges
        for graphNode in nodes:
            for neighbor in graphNode.neighbors:
                newNeighbor = mapping[neighbor]
                mapping[graphNode].neighbors.append(newNeighbor)

        return mapping[node]


    def _get_nodes(self, node):
        from collections import deque

        queue = deque([])
        history = set()
        nodes = []

        queue.append(node)
        history.add(node)

        while queue:
            graphNode = queue.popleft()
            nodes.append(graphNode)

            for neighbor in graphNode.neighbors:
                if neighbor not in history:
                    queue.append(neighbor)
                    history.add(neighbor)

        return nodes