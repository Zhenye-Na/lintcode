from heapq import heappush, heappop

class Solution:
    """
    @param A: an integer arrays sorted in ascending order
    @param B: an integer arrays sorted in ascending order
    @param k: An integer
    @return: An integer
    """
    dx = [0, 1]
    dy = [1, 0]

    def kthSmallestSum(self, A, B, k):
        # write your code here
        if not A or not B or len(A) == 0 or len(B) == 0:
            return None

        heap = [(A[0] + B[0], 0, 0)]
        visited = [[0 for _ in range(len(A))] for _ in range(len(B))]

        for _ in range(k - 1):
            running_sum, a, b = heappop(heap)
            for i in range(2):
                next_a, next_b = a + self.dx[i], b + self.dy[i]
                if self._isValid(next_a, next_b, A, B, visited):
                    heappush(heap, (A[next_a] + B[next_b], next_a, next_b))
                    visited[next_a][next_b] = 1

        return heap[0][0]

    def _isValid(self, i, j, A, B, visited):
        return 0 <= i < len(A) and 0 <= j < len(B) and visited[i][j] == 0