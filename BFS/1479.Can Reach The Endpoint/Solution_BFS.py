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
