# 465. Kth Smallest Sum In Two Sorted Arrays

**Description**

Given two integer arrays sorted in ascending order and an integer `k`. Define `sum = a + b`, where `a` is an element from the first array and `b` is an element from the second one. Find the kth smallest sum out of all possible sums.

**Example**

Example 1

```
Input:
a = [1, 7, 11]
b = [2, 4, 6]
k = 3
Output: 7
Explanation: The sums are [3, 5, 7, 9, 11, 13, 13, 15, 17] and the 3th is 7.
```

Example 2

```
Input:
a = [1, 7, 11]
b = [2, 4, 6]
k = 4
Output: 9
Explanation: The sums are [3, 5, 7, 9, 11, 13, 13, 15, 17] and the 4th is 9.
```

Example 3

```
Input:
a = [1, 7, 11]
b = [2, 4, 6]
k = 8
Output: 15
Explanation: The sums are [3, 5, 7, 9, 11, 13, 13, 15, 17] and the 8th is 15.
```

**Challenge**

Do it in either of the following time complexity:

- `O(k log min(n, m, k))`. where `n` is the size of `A`, and `m` is the size of `B`.
- `O( (m + n) log maxValue)`. where maxValue is the max number in A and B.


**Heap**

用数组记录是否访问过, 不推荐, 空间容易爆

```python
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
```

**Heap**

用 `set` 记录是否访问过, 推荐


```python
import heapq


class Solution:
    """
    @param A: an integer arrays sorted in ascending order
    @param B: an integer arrays sorted in ascending order
    @param k: An integer
    @return: An integer
    """
    def kthSmallestSum(self, A, B, k):
        if not A or not B:
            return None

        n, m = len(A), len(B)
        minheap = [(A[0] + B[0], 0, 0)]
        visited = set([0])
        num = None
        for _ in range(k):
            num, x, y = heapq.heappop(minheap)
            if x + 1 < n and (x + 1) * m + y not in visited:
                heapq.heappush(minheap, (A[x + 1] + B[y], x + 1, y))
                visited.add((x + 1) * m + y)
            if y + 1 < m and x * m + y + 1 not in visited:
                heapq.heappush(minheap, (A[x] + B[y + 1], x, y + 1))
                visited.add(x * m + y + 1)

        return num
```