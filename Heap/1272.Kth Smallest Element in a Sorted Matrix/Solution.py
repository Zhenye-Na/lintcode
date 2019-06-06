from heapq import heappush, heappop


class Solution:
    """
    @param matrix: List[List[int]]
    @param k: a integer
    @return: return a integer
    """
    dx = [0, 1]
    dy = [1, 0]

    def kthSmallest(self, matrix, k):
        # write your code here
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0 or len(matrix) * len(matrix[0]) < k:
            return None

        m, n = len(matrix), len(matrix[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        heap = []
        heappush(heap, (matrix[0][0], 0, 0))

        for _ in range(k - 1):
            val, x, y = heappop(heap)
            for i in range(2):
                newx, newy = x + self.dx[i], y + self.dy[i]
                if self._isValid(newx, newy, m, n, visited):
                    heappush(heap, (matrix[newx][newy], newx, newy))
                    visited[newx][newy] = True

        return heap[0][0]

    def _isValid(self, i, j, m, n, visited):
        return 0 <= i < m and 0 <= j < n and not visited[i][j]
