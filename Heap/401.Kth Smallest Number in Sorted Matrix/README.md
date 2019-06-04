# 401. Kth Smallest Number in Sorted Matrix

**Description**

Find the `kth` smallest number in a row and column sorted matrix.

Each row and each column of the matrix is incremental.

**Example**

Example 1:

```
Input:
[
  [1 ,5 ,7],
  [3 ,7 ,8],
  [4 ,8 ,9],
]
k = 4
Output: 5
```

Example 2:

```
Input:
[
  [1, 2],
  [3, 4]
]
k = 3
Output: 3
```

Challenge

`O(klogn)` time, `n` is the maximum of the width and height of the matrix.


```python
from heapq import heappush, heappop


class Solution:
    """
    @param matrix: a matrix of integers
    @param k: An integer
    @return: the kth smallest number in the matrix
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
```