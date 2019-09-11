class Solution:
    """
    @param grid: a 2D array of integers
    @param rules: an array of strings
    @param k: an integer that denotes the number of steps to perform
    @return: return a grid
    """

    ALIVE = []

    dx = [1, 1, 1, 0, 0, -1, -1, -1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    def GridGame(self, grid, rules, k):
        # write your code here
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return [[]]

        n, m = len(grid), len(grid[0])

        for idx, rule in enumerate(rules):
            if rule == 'alive':
                self.ALIVE.append(idx)

        for _ in range(k):
            print(grid)
            new_grid = [[0 for _ in range(m)] for _ in range(n)]

            for i in range(n):
                for j in range(m):
                    if self.count(i, j, grid, n, m) in self.ALIVE:
                        new_grid[i][j] = 1
            grid = new_grid

        return grid

    def count(self, i, j, grid, n, m):
        count = 0
        for idx in range(len(self.dx)):
            temp_x = self.dx[idx] + i
            temp_y = self.dy[idx] + j
            if temp_x >= 0 and temp_x < n and temp_y >= 0 and temp_y < m and grid[temp_x][temp_y] == 1:
                count += 1
        return count
