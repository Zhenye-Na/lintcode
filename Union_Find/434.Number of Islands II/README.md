# 434. Number of Islands II

**Description**

Given a `n`, `m` which means the row and column of the 2D matrix and an array of pair `A` (size `k`). Originally, the 2D matrix is all `0` which means there is only sea in the matrix. The list pair has `k` operator and each operator has two integer `A[i].x`, `A[i].y` means that you can change the grid `matrix[A[i].x][A[i].y]` from sea to island. Return how many island are there in the matrix after each operator.

`0` is represented as the sea, `1` is represented as the island. If two `1` is adjacent, we consider them in the same island. We only consider `up/down/left/right` adjacent.

**Example**

Example 1:

```
Input: n = 4, m = 5, A = [[1,1],[0,1],[3,3],[3,4]]
Output: [1,1,2,2]
Explanation:
1.  00000
    00000
    00000
    00000
2.  00000
    01000
    00000
    00000
3.  01000
    01000
    00000
    00000
4.  01000
    01000
    00000
    00010
5.  01000
    01000
    00000
    00011
```

Example 2:

```
Input: n = 3, m = 3, A = [[0,0],[0,1],[2,2],[2,1]]
Output: [1,1,2,2]
```

**Union Find**

连通块的个数 (实时)

```python
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
```