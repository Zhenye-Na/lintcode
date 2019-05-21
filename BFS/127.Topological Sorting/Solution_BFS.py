from collections import deque

"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        if graph is None:
            return []

        order = []
        queue = deque([])
        indegree = self._getIndegree(graph)

        for node, nodeIndegree in indegree.items():
            if nodeIndegree == 0:
                queue.append(node)

        while queue:
            graphNode = queue.popleft()
            order.append(graphNode)

            for neighbor in graphNode.neighbors:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)


        return order if len(order) == len(graph) else None


    def _getIndegree(self, graph):
        indegree = {x: 0 for x in graph}
        for node in graph:
            for neighbor in node.neighbors:
                indegree[neighbor] += 1

        return indegree
