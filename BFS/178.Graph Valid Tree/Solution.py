from collections import deque, defaultdict

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        if n <= 1:
            return True

        # Contraint 1: # of edges equals to # of node minus 1
        if len(edges) != n - 1:
            return False

        # map from integer -> set of neighbors
        mapping = self._get_neighbors(edges)

        # Constraint 2: # of onnected component in the graph is 1
        queue = deque([])
        queue.append(0)
        history = set()

        while queue:
            node = queue.popleft()
            for neighbor in mapping[node]:
                if neighbor not in history:
                    queue.append(neighbor)
                    history.add(neighbor)

        if len(history) == n:
            return True
        return False

    def _get_neighbors(self, edges):
        mapping = defaultdict(set)
        for edge in edges:
            source, target = edge
            mapping[source].add(target)
            mapping[target].add(source)

        return mapping
