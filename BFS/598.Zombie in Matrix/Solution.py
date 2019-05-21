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
