from collections import deque

class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    self._bfs(grid, i, j)
                    islands += 1

        return islands                    
    
    def _bfs(self, grid, x, y):
        queue = deque([(x, y)])
        grid[x][y] = False

        while queue:
            x, y = queue.popleft()

            for delta_x, delta_y in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                next_x = x + delta_x
                next_y = y + delta_y

                if not self.is_valid(grid, next_x, next_y):
                    continue

                queue.append((next_x, next_y))
                grid[next_x][next_y] = False
                
    def is_valid(self, grid, x, y):
        n, m = len(grid), len(grid[0])
        return 0 <= x < n and 0 <= y < m and grid[x][y]
