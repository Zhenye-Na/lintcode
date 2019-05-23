from collections import deque
import sys

class Solution:
    """
    @param grid: The gird
    @return: Return the steps you need at least
    """
    def getBestRoad(self, grid):
        # Write your code here
        m, n = len(grid), len(grid[0])
        src = [ [sys.maxsize] * n for _ in range(m)] 
        dst = [ [sys.maxsize] * n for _ in range(m)] 

        self.bfs(grid, src, m, n, True)
        self.bfs(grid, dst, m, n, False)

        minDis = sys.maxsize
        for i in range(m):
            for j in range(n):
                if src[i][j] != sys.maxsize and dst[i][j] != sys.maxsize:
                    minDis = min(minDis, src[i][j] + dst[i][j])

        if minDis == sys.maxsize:
            return -1
        else:
            return minDis


    def bfs(self, grid, dis, m, n, isSrc):
        q = deque()

        if isSrc:
            q.append((0, 0))
            dis[0][0] = 0
        else:
            q.append((m - 1, n - 1))
            dis[m - 1][n - 1] = 0

        step = 0
        while q:
            step += 1
            qsize = len(q)
            for _ in range(qsize):
                i, j = q.popleft()
                for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    ni = i + di
                    nj = j + dj
                    if self._isValid(ni, nj, m, n, dis):
                        if grid[ni][nj] == 1:
                            dis[ni][nj] = step
                        else:
                            dis[ni][nj] = step
                            q.append((ni, nj))

    def _isValid(self, ni, nj, m, n, dis):
        return 0 <= ni < m and 0 <= nj < n and dis[ni][nj] == sys.maxsize
