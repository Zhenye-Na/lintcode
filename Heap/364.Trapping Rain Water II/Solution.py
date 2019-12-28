from heapq import heappush, heappop


class Solution:
    """
    @param heights: a matrix of integers
    @return: an integer
    """
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    borders = []
    visited = set([])

    def trapRainWater(self, heights):
        # write your code here
        if heights is None or len(heights) == 0 or len(heights[0]) == 0:
            return 0

        self._create_boders(heights)

        water = 0
        while self.borders:
            bar_height, x, y = heappop(self.borders)

            for d in range(4):
                new_x, new_y = x + self.dx[d], y + self.dy[d]

                if self._inBound(new_x, new_y):
                    water += max(0, bar_height - heights[new_x][new_y])
                    new_height = max(bar_height, heights[new_x][new_y])
                    heappush(self.borders, (new_height, new_x, new_y))
                    self.visited.add((new_x, new_y))

        return water

    def _create_boders(self, heights):
        self.m, self.n = len(heights), len(heights[0])
        for row in [0, self.m - 1]:
            for col in range(self.n):
                heappush(self.borders, (heights[row][col], row, col))
                self.visited.add((row, col))

        for col in [0, self.n - 1]:
            for row in range(self.m):
                heappush(self.borders, (heights[row][col], row, col))
                self.visited.add((row, col))

    def _inBound(self, x, y):
        return 0 <= x < self.m and 0 <= y < self.n and (x, y) not in self.visited
