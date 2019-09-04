# 1374. Shortest Distance in 3D Space

Description


Given an integer `N` represents an `N*N*N` space, and an array of coordinates represents the position of the barrier, return the minimum number of steps from `(0,0,0)` to `(n-1,n-1,n-1)`, if you can't reach `(n-1,n-1,n-1)`, return `-1`.

> 1. The range of the N is [1,10].


**Example**

Example 1:

```
Input: N = 3, barrier = [[1,0,0],[1,0,1],[1,0,2],[1,1,0],[1,1,1],[1,1,2],[1,2,1],[1,2,2]]
Output: 6
```

Example 2:

```
Input: N = 3, barrier = [[2,2,2]]
Output: -1
```


**BFS**

```python
from collections import deque


class Solution:
    """
    @param N: the size of space
    @param barriers: an array of coordinates represents the position of the barrier
    @return: the minimum number of steps
    """
    DIRECTIONS = ((0, 0, 1), (0, 0, -1), (0, 1, 0),
                  (0, -1, 0), (1, 0, 0), (-1, 0, 0))

    def shortestDistance(self, N, barriers):
        # Write your code here
        if (0, 0, 0) in barriers or (N - 1, N - 1, N - 1) in barriers:
            return -1

        queue = deque([])
        queue.append((0, 0, 0))
        visited = set([(0, 0, 0)])
        steps = 0

        while queue:
            size = len(queue)
            for _ in range(size):
                x, y, z = queue.popleft()
                if x == N - 1 and y == N - 1 and z == N - 1:
                    return steps
                for idx in range(len(self.DIRECTIONS)):
                    new_x, new_y, new_z = x + \
                        self.DIRECTIONS[idx][0], y + \
                        self.DIRECTIONS[idx][1], z + self.DIRECTIONS[idx][2]

                    if self.isValid(new_x, new_y, new_z, N, visited, barriers):
                        queue.append((new_x, new_y, new_z))
                        visited.add((new_x, new_y, new_z))

            steps += 1

        return -1

    def isValid(self, x, y, z, n, visited, barriers):
        return 0 <= x < n and 0 <= y < n and 0 <= z < n and (x, y, z) not in visited and [x, y, z] not in barriers
```