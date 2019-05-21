"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: values: a hash mapping, <UndirectedGraphNode, (int)value>
    @param: node: an Undirected graph node
    @param: target: An integer
    @return: a node
    """
    def searchNode(self, graph, values, node, target):
        # write your code here
        if graph is None or node is None or target is None:
            return None

        return self._search(node, target, values)

    def _search(self, node, target, values):
        # BFS find the nearest node
        from collections import deque
        if values[node] == target:
            return node

        queue = deque([])
        history = set()

        queue.append(node)
        history.add(node)

        while queue:
            graphNode = queue.popleft()
            for neighbor in graphNode.neighbors:
                if values[neighbor] == target:
                    return neighbor
                if neighbor not in history:
                    queue.append(neighbor)
                    history.add(neighbor)

        return None
