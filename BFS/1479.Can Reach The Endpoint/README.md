1479. Can Reach The Endpoint
Description
中文
English
Given a map size of m*n, 1 means space, 0 means obstacle, 9 means the endpoint. You start at (0,0) and return whether you can reach the endpoint.

Have you met this question in a real interview?  
Example
Example 1

Input: 
[
	[1,1,1],
	[1,1,1],
	[1,1,9]
]
Output: true
Example 2

Input: 
[
	[1,1,1],
	[1,0,0],
	[1,0,9]
]
Output: false


**BFS**

```python
from collections import deque


class Solution:
    """
    @param grid: the map grid
    @return: can you reach the endpoint
    """
    SPACE = 1
    OBSTACLE = 0
    ENDPOINT = 9

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def reachEndpoint(self, grid):
        # Write your code here
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return False

        m, n = len(grid), len(grid[0])
        queue = deque([(0, 0)])
        history = set()

        while queue:
            x, y = queue.popleft()
            history.add((x, y))
            if grid[x][y] == self.ENDPOINT:
                return True

            for i in range(4):
                new_x, new_y = x + self.dx[i], y + self.dy[i]
                if (new_x, new_y) in history:
                    continue

                if not self._isValid(new_x, new_y, m , n, grid):
                    continue

                queue.append((new_x, new_y))
                history.add((new_x, new_y))

        return False

    def _isValid(self, x, y, m , n, grid):
        return 0 <= x < m and 0 <= y < n and (grid[x][y] == self.SPACE or grid[x][y] == self.ENDPOINT)
```


**DFS**


