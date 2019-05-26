class Solution:
    """
    @param graph: the given undirected graph
    @return:  return true if and only if it is bipartite
    """
    def isBipartite(self, graph):
        # Write your code here
        if not graph or len(graph) == 0:
            return False

        n = len(graph)
        self.colors = [0 for _ in range(n)]

        for i in range(n):
            if self.colors[i] == 0 and not self._colorize(i, 1, graph):
                return False

        return True


    def _colorize(self, current, color, graph):
        if self.colors[current] != 0:
            return self.colors[current] == color

        self.colors[current] = color
        for neighbor in graph[current]:
            if not self._colorize(neighbor, - color, graph):
                return False
        return True
