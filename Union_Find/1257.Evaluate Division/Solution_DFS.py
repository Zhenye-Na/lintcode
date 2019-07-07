"""
Author: Huahua
Running time: 32 ms (beats 100%)
"""


class Solution:
    def calcEquation(self, equations, values, queries):
        def divide(x, y, visited):
            if x == y:
                return 1.0
            visited.add(x)
            for n in g[x]:
                if n in visited:
                    continue
                visited.add(n)
                d = divide(n, y, visited)
                if d > 0:
                    return d * g[x][n]
            return -1.0

        g = collections.defaultdict(dict)
        for (x, y), v in zip(equations, values):
            g[x][y] = v
            g[y][x] = 1.0 / v

        ans = [divide(x, y, set()) if x in g and y in g else -
               1 for x, y in queries]
        return ans
