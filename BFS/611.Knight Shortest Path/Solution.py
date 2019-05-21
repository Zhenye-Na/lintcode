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
