630. Knight Shortest Path II
Description
中文
English
Given a knight in a chessboard n * m (a binary matrix with 0 as empty and 1 as barrier). the knight initialze position is (0, 0) and he wants to reach position (n - 1, m - 1), Knight can only be from left to right. Find the shortest path to the destination position, return the length of the route. Return -1 if knight can not reached.

Have you met this question in a real interview?  
Clarification
If the knight is at (x, y), he can get to the following positions in one step:

(x + 1, y + 2)
(x - 1, y + 2)
(x + 2, y + 1)
(x - 2, y + 1)
Example
Example 1:

Input:
[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
Output:
3
Explanation:
[0,0]->[2,1]->[0,2]->[2,3]
Example 2:

Input:
[[0,1,0],[0,0,1],[0,0,0]]
Output:
-1


**BFS**

试着用了一下新的数据结构 `collections.namedtuple` , 好玩 ~

```python
from collections import deque, namedtuple


class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """
    EMPTY = 0
    BARRIER = 1

    dX = [1, -1, 2, -2]
    dY = [2, 2, 1, 1]

    def shortestPath2(self, grid):
        # write your code here
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return -1

        Source = namedtuple("Source", ["x", "y"])
        Destination = namedtuple("Destination", ["x", "y"])

        source = Source(0, 0)
        destination = Destination(len(grid) - 1, len(grid[0]) - 1)


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

                for i in range(4):
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