from collections import deque


class Solution:
    """
    @param: A: An integer matrix
    @return: The index of the peak
    """
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def findPeakII(self, A):
        # write your code here
        # 爬山法
        if not A or len(A) == 0 or len(A[0]) == 0:
            return [-1, -1]

        history = set([(0, 0)])
        queue = deque([(0, 0)])
        n, m = len(A), len(A[0])

        while queue:
            x, y = queue.popleft()
            for d in range(4):
                newx, newy = x + self.dx[d], y + self.dy[d]
                if self.inBound(newx, newy, n, m) and (newx, newy) not in history:
                    queue.append((newx, newy))
                    history.add((newx, newy))

                    if self.isPeak(newx, newy, history, A, n, m):
                        return [newx, newy]

        return [-1, -1]

    def isPeak(self, x, y, history, A, n, m):
        # 边界不可能是峰
        if x == n - 1 or x == 0 or y == m - 1 or y == 0:
            return False

        # 如果四周有比它高 就不是
        for i in range(4):
            adj_x, adj_y = x + self.dx[i], y + self.dy[i]
            if self.inBound(adj_x, adj_y, n, m) and (adj_x, adj_y) not in history:
                if A[adj_x][adj_y] > A[x][y]:
                    return False

        return True

    def inBound(self, x, y, n, m):
        return 0 <= x < n and 0 <= y < m
