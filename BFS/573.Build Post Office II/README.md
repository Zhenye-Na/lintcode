# 573. Build Post Office II

**Description**

Given a 2D grid, each cell is either a wall `2`, an house `1` or empty `0` (the number zero, one, two), find a place to build a post office so that the sum of the distance from the post office to all the houses is smallest.

Return the smallest sum of distance. Return `-1` if it is not possible.

```
You cannot pass through wall and house, but can pass through empty.
You only build post office on an empty.
```

**Example**

Example 1:

```
Input:
[[0,1,0,0,0],
 [1,0,0,2,1],
 [0,1,0,0,0]]
Output: 8
Explanation: Placing a post office at (1,1), the distance that post office to all the house sum is smallest.
```

Example 2:

```
Input:
[[0,1,0],
 [1,0,1],
 [0,1,0]]
Output: 4
Explanation: Placing a post office at (1,1), the distance that post office to all the house sum is smallest.
```

**Challenge**

Solve this problem within `O(n^3)` time.


**BFS**

对每个 house 做 BFS，记录每个 empty

- 能被多少个 house 触及
- 这些能触及的 house 到达这个 empty 的总步数之和

如果最后每个 empty 都无法被所有 house 触及 (即不等于 house 个数)，则返回 -1

如果有能被所有 house 触及的 empty，取其最小的返回



```python
class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
    """
    EMPTY = 0
    HOUSE = 1
    WALL = 2

    INFINITY = float('inf')
    VECTOR = (
        ( 0, -1),
        ( 0,  1),
        (-1,  0),
        ( 1,  0),
    )

    visited_time = None
    distance_sum = None

    def shortestDistance(self, grid):
        # write your code here
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return -1

        self.m, self.n = len(grid), len(grid[0])
        self.visited_time = [[0] * self.n for _ in range(self.m)]
        self.distance_sum = [[0] * self.n for _ in range(self.m)]

        # BFS each house and record visited time
        house_count = 0
        for x in range(self.m):
            for y in range(self.n):
                if grid[x][y] == self.HOUSE:
                    house_count += 1
                    self._bfs(x, y, grid)

        # Select the position which gives the minimum cumulative distance
        min_distance = self.INFINITY
        for x in range(self.m):
            for y in range(self.n):
                if self._isValidCandidate(x, y, grid, house_count, min_distance):
                    min_distance = self.distance_sum[x][y]

        return min_distance if min_distance < self.INFINITY else -1

    def _isValidCandidate(self, x, y, grid, house_count, min_distance):
        return grid[x][y] == self.EMPTY and self.visited_time[x][y] == house_count and self.distance_sum[x][y] < min_distance

    def _bfs(self, x, y, grid):
        queue, _queue = [(x, y)], None
        visited = [[False] * self.n for _ in range(self.m)]
        distance = 0

        while queue:
            _queue = []
            distance += 1

            for x, y in queue:
                for dx, dy in self.VECTOR:
                    _x = x + dx
                    _y = y + dy

                    if self._inBound(_x, _y, grid, visited):
                        visited[_x][_y] = True
                        self.visited_time[_x][_y] += 1
                        self.distance_sum[_x][_y] += distance
                        _queue.append((_x, _y))

            queue = _queue

    def _inBound(self, _x, _y, grid, visited):
        return 0 <= _x < self.m and 0 <= _y < self.n and grid[_x][_y] == self.EMPTY and not visited[_x][_y]
```

