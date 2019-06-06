# 1272. Kth Smallest Element in a Sorted Matrix

**Description**

Given a `n x n` matrix where each of the rows and columns are sorted in ascending order, find the `k`th smallest element in the matrix.

Note that it is the `k`th smallest element in the sorted order, not the `k`th distinct element.

You may assume `k` is always valid, `1 <= k <= n^2`.

**Example**

Example 1

```
Input:
[[1, 5, 9],[10, 11, 13],[12, 13, 15]]
8
Output: 13
```

Example 2

```
Input:
[[-5]]
1
Output: -5
```

**Challenge**

If `k << n^2`, what's the best algorithm? How about `k ~ n^2`?

**Heap**

```python
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
```