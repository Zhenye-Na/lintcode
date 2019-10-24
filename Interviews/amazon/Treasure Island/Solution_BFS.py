from collections import deque

class Solution:

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    def treasureIsland(self, island):
        # Output the *minimum* number of steps to get to the treasure
        if not island or len(island) == 0 or len(island[0]) == 0:
            return 0

        m, n = len(island), len(island[0])

        queue = deque([(0, 0)])
        history = set([(0, 0)])
        steps = 1
        while queue:
            steps += 1
            size = len(queue)
            for j in range(size):
                x, y = queue.popleft()
                for i in range(4):
                    new_x, new_y = x + self.dx[i], y + self.dy[i]
                    if self.isValid(new_x, new_y, m, n, island, history):
                        queue.append((new_x, new_y))
                        history.add((new_x, new_y))
                        if island[new_x][new_y] == "X":
                            return steps - 1

        return 0


    def isValid(self, x, y, m, n, island, history):
        return 0 <= x < m and  0 <= y < n and island[x][y] != "D" and (x, y) not in history


sol = Solution()
island = [
    ['O', 'O', 'O', 'O'],
    ['D', 'O', 'D', 'O'],
    ['O', 'O', 'O', 'O'],
    ['X', 'D', 'D', 'O']
]
print(sol.treasureIsland(island))