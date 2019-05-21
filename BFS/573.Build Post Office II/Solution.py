class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
    """
    EMPTY = 0
    HOUSE = 1
    WALL = 2

    INFINITY = float('inf')
    VECTOR = (
        ( 0, -1),
        ( 0,  1),
        (-1,  0),
        ( 1,  0),
    )

    visited_time = None
    distance_sum = None

    def shortestDistance(self, grid):
        # write your code here
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return -1

        self.m, self.n = len(grid), len(grid[0])
        self.visited_time = [[0] * self.n for _ in range(self.m)]
        self.distance_sum = [[0] * self.n for _ in range(self.m)]

        # BFS each house and record visited time
        house_count = 0
        for x in range(self.m):
            for y in range(self.n):
                if grid[x][y] == self.HOUSE:
                    house_count += 1
                    self._bfs(x, y, grid)

        # Select the position which gives the minimum cumulative distance
        min_distance = self.INFINITY
        for x in range(self.m):
            for y in range(self.n):
                if self._isValidCandidate(x, y, grid, house_count, min_distance):
                    min_distance = self.distance_sum[x][y]

        return min_distance if min_distance < self.INFINITY else -1

    def _isValidCandidate(self, x, y, grid, house_count, min_distance):
        return grid[x][y] == self.EMPTY and self.visited_time[x][y] == house_count and self.distance_sum[x][y] < min_distance

    def _bfs(self, x, y, grid):
        queue, _queue = [(x, y)], None
        visited = [[False] * self.n for _ in range(self.m)]
        distance = 0

        while queue:
            _queue = []
            distance += 1

            for x, y in queue:
                for dx, dy in self.VECTOR:
                    _x = x + dx
                    _y = y + dy

                    if self._inBound(_x, _y, grid, visited):
                        visited[_x][_y] = True
                        self.visited_time[_x][_y] += 1
                        self.distance_sum[_x][_y] += distance
                        _queue.append((_x, _y))

            queue = _queue

    def _inBound(self, _x, _y, grid, visited):
        return 0 <= _x < self.m and 0 <= _y < self.n and grid[_x][_y] == self.EMPTY and not visited[_x][_y]
