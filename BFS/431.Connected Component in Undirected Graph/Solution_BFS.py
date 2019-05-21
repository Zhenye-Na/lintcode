from collections import deque

"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

class Solution:
    """
    @param {UndirectedGraphNode[]} nodes an array of undirected graph node
    @return {int[][]} a connected set of a undirected graph
    """
    def connectedSet(self, nodes):
        # write your code here
        connected_components = []

        if not nodes or len(nodes) == 0:
            return connected_components

        visited = set()

        for node in nodes:
            if node in visited:
                continue
            
            component = []
            queue = deque([node])
            visited.add(node)

            while queue:
                cur_node = queue.popleft()
                component.append(cur_node.label)
                for neighbor in cur_node.neighbors:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)

            component.sort()
            connected_components.append(component)

        return connected_components
