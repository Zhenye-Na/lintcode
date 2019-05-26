# 677. Number of Big Islands

**Description**

Given a boolean 2D matrix, `0` is represented as the sea, `1` is represented as the island. If two `1` is adjacent, we consider them in the same island. We only consider `up/down/left/right` adjacent.

Find the number of islands that size bigger or equal than `K`.

**Example**

Example 1

```
Input: 
[[1,1,0,0,0],[0,1,0,0,1],[0,0,0,1,1],[0,0,0,0,0],[0,0,0,0,1]]
2
Output: 2
Explanation:
the 2D grid is
[
  [1, 1, 0, 0, 0],
  [0, 1, 0, 0, 1],
  [0, 0, 0, 1, 1],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1]
]
there are two island which size is equals to 3.
```


Example 2

```
Input: 
[[1,0],[0,1]]
1
Output: 2
```

**BFS**

```python
from collections import deque


class Solution:
    """
    @param grid: a 2d boolean array
    @param k: an integer
    @return: the number of Islands
    """
    ISLAND = 1
    SEA = 0

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def numsofIsland(self, grid, k):
        # Write your code here
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        m, n = len(grid), len(grid[0])
        if k > m * n:
            return 0

        results = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == self.ISLAND:
                    area = self._bfs(i, j, grid)
                    if area > k:
                        results += 1

        return results


    def _bfs(self, i, j, grid):
        queue = deque([(i, j)])
        area = 1

        while queue:
            x, y = queue.popleft()
            for i in range(4):
                newX, newY = x + self.dx[i], y + self.dy[i]

                if not self._isValid(newX, newY, grid):
                    continue

                queue.append((newX, newY))
                grid[newX][newY] = self.SEA
                area += 1

        return area


    def _isValid(self, x, y, grid):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == self.ISLAND
```