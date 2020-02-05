from collections import deque


class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def __init__(self):
        self.OBSTACLE = -1
        self.GATE = 0
        self.ROOM = (1 << 31) - 1
        self.dx = [1, -1, 0, 0]
        self.dy = [0, 0, 1, -1]


    def wallsAndGates(self, rooms):
        # write your code here
        if not rooms or len(rooms) == 0 or len(rooms[0]) == 0:
            return rooms

        # level order BFS on all of the gates
        self.m, self.n = len(rooms), len(rooms[0])
        for i in range(self.m):
            for j in range(self.n):
                if rooms[i][j] == self.GATE:
                    self.bfs(i, j, rooms)

        return rooms


    def bfs(self, i, j, rooms):
        queue = deque([(i, j)])

        distance = 0
        while queue:
            size = len(queue)
            distance += 1
            for _ in range(size):
                i, j = queue.popleft()
                for d in range(4):
                    x, y = i + self.dx[d], j + self.dy[d]
                    if self.inBound(x, y, rooms) and rooms[x][y] > distance:
                        queue.append((x, y))
                        rooms[x][y] = distance


    def inBound(self, x, y, rooms):
        return 0 <= x < self.m and 0 <= y < self.n and rooms[x][y] != self.GATE and rooms[x][y] != self.OBSTACLE

