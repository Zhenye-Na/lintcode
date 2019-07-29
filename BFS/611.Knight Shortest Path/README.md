# 611. Knight Shortest Path

**Description**

Given a knight in a chessboard (a binary matrix with `0` as empty and `1` as barrier) with a source position, find the shortest path to a destination position, return the `length` of the route.

Return `-1` if destination cannot be reached.

```
source and destination must be empty.
Knight can not enter the barrier.
Path length refers to the number of steps the knight takes.
```

**Clarification**

If the knight is at `(x, y)`, he can get to the following positions in one step:

```
(x + 1, y + 2)
(x + 1, y - 2)
(x - 1, y + 2)
(x - 1, y - 2)
(x + 2, y + 1)
(x + 2, y - 1)
(x - 2, y + 1)
(x - 2, y - 1)
```


**Example**

Example 1:

```
Input:
[[0,0,0],
 [0,0,0],
 [0,0,0]]
source = [2, 0] destination = [2, 2] 
Output: 2
Explanation:
[2,0]->[0,1]->[2,2]
```

Example 2:

```
Input:
[[0,1,0],
 [0,0,1],
 [0,0,0]]
source = [2, 0] destination = [2, 2] 
Output:-1
```

**BFS**

普通方法会导致 MLE, 所以需要用一个 `HashMap<Tuple, Integer>` 来记录从 `source` 到当前每一个位置走了多少步.

```python
from collections import deque

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    EMPTY = 0
    BARRIER = 1

    dX = [1, 1, -1, -1, 2, 2, -2, -2]
    dY = [2, -2, 2, -2, 1, -1, 1, -1]

    def shortestPath(self, grid, source, destination):
        # write your code here
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return -1

        # source and destination must be empty
        if grid[source.x][source.y] != self.EMPTY or grid[destination.x][destination.y] != self.EMPTY:
            return -1

        if source.x == destination.x and source.y == destination.y:
            return 0

        queue = deque([(source.x, source.y)])
        distance = {(source.x, source.y): 0}

        while queue:
            size = len(queue)

            for _ in range(size):
                x, y = queue.popleft()
                if (x, y) == (destination.x, destination.y):
                    return distance[(x, y)]

                for i in range(8):
                    newX, newY = x + self.dX[i], y + self.dY[i]
                    if (newX, newY) in distance:
                        continue

                    if not self._isValid(newX, newY, grid):
                        continue

                    distance[(newX, newY)] = distance[(x, y)] + 1
                    queue.append((newX, newY))

        return -1


    def _isValid(self, x, y, grid):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == self.EMPTY
```
