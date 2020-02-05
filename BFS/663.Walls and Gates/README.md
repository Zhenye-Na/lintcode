# 663. Walls and Gates

**Description**

You are given a `m x n` 2D grid initialized with these three possible values.

- `-1` - A wall or an obstacle.
- `0` - A gate.
- `INF` - Infinity means an empty room. We use the value `2^31 - 1 = 2147483647` to represent `INF` as you may assume that the distance to a gate is less than `2147483647`.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a Gate, that room should remain filled with `INF`

**Example**

Example 1

```
Input:
[[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output:
[[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

Explanation:
the 2D grid is:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
the answer is:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
```

Example 2

```
Input:
[[0,-1],[2147483647,2147483647]]
Output:
[[0,-1],[1,2]]
```

多元 BFS。其实就是所有的 0 是 BFS 的第一层。唯一的难点就是**先到先得**。一旦被填了 dist，就不能再访问。


```python
from collections import deque


class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def __init__(self):
        self.OBSTACLE = -1
        self.GATE = 0
        self.ROOM = (1 << 31) - 1
        self.dx = [1, -1, 0, 0]
        self.dy = [0, 0, 1, -1]


    def wallsAndGates(self, rooms):
        # write your code here
        if not rooms or len(rooms) == 0 or len(rooms[0]) == 0:
            return rooms

        # level order BFS on all of the gates
        self.m, self.n = len(rooms), len(rooms[0])
        for i in range(self.m):
            for j in range(self.n):
                if rooms[i][j] == self.GATE:
                    self.bfs(i, j, rooms)

        return rooms


    def bfs(self, i, j, rooms):
        queue = deque([(i, j)])

        distance = 0
        while queue:
            size = len(queue)
            distance += 1
            for _ in range(size):
                i, j = queue.popleft()
                for d in range(4):
                    x, y = i + self.dx[d], j + self.dy[d]
                    if self.inBound(x, y, rooms) and rooms[x][y] > distance:
                        queue.append((x, y))
                        rooms[x][y] = distance


    def inBound(self, x, y, rooms):
        return 0 <= x < self.m and 0 <= y < self.n and rooms[x][y] != self.GATE and rooms[x][y] != self.OBSTACLE
```