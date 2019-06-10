"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    def numIslands2(self, n, m, operators):
        # write your code here
        if not n or not m or m == 0 or n == 0 or not operators or len(operators) == 0:
            return []

        self.parents = {point.x * m + point.y : point.x * m + point.y for point in operators}
        self.num_of_islands = 0

        results = []
        islands = set()
        for point in operators:
            x, y = point.x, point.y

            if x * m + y in islands:
                results.append(self.num_of_islands)
                continue

            islands.add(x * m + y)
            self.num_of_islands += 1
            for d in range(4):
                newx, newy = x + self.dx[d], y + self.dy[d]
                location = newx * m + newy
                if self._inBound(newx, newy, m, n) and location in islands:
                    self._connect(x * m + y, location)
                    islands.add(location)

            results.append(self.query())

        return results

    def _inBound(self, x, y, m, n):
        return 0 <= x < n and 0 <= y < m


    def _connect(self, a, b):
        root_a = self._find(a)
        root_b = self._find(b)
        if root_b != root_a:
            self.parents[root_b] = root_a
            self.num_of_islands -= 1


    def _find(self, node):
        path = []
        while node != self.parents[node]:
            path.append(node)
            node = self.parents[node]

        for n in path:
            self.parents[n] = node

        return node

    def query(self):
        return self.num_of_islands
