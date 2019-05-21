# 598. Zombie in Matrix

**Description**

Given a 2D grid, each cell is either a wall `2`, a zombie `1` or people `0` (the number zero, one, two). Zombies can turn the nearest people (`up/down/left/right`) into zombies every day, but can not through wall. How long will it take to turn all people into zombies?

Return `-1` if can not turn all people into zombies.

**Example**

Example 1:

```
Input:
[[0,1,2,0,0],
 [1,0,0,2,1],
 [0,1,0,0,0]]
Output:
2
```

Example 2:

```
Input:
[[0,0,0],
 [0,0,0],
 [0,0,1]]
Output:
4
```

**BFS**

多源点 BFS

从所有的源点出发, 向外感染

```python
from collections import deque

class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """
    WALL = 2
    ZOMBIE = 1
    PEOPLE = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def zombie(self, grid):
        # write your code here
        if not grid or len(grid) == 0:
            return -1

        zombies = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == self.ZOMBIE:
                    zombies.append((i, j))

        queue = deque(zombies)
        days = 0

        # 分层遍历
        while queue:
            days += 1
            size = len(queue)

            for _ in range(size):
                cordinate = queue.popleft()

                for dX, dY in zip(self.dx, self.dy):
                    if self.isPeople(cordinate[0] + dX, cordinate[1] + dY, grid):
                        grid[cordinate[0] + dX][cordinate[1] + dY] = self.ZOMBIE
                        queue.append((cordinate[0] + dX, cordinate[1] + dY))

        # Double check
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == self.PEOPLE:
                    return -1

        return days - 1

    def isPeople(self, x, y, grid):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == self.PEOPLE
```