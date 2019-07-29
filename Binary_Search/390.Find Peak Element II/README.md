# 390. Find Peak Element II

**Description**

Given an integer matrix `A` which has the following features :

```
The numbers in adjacent positions are different.
The matrix has n rows and m columns.
For all i < n, A[i][0] < A[i][1] && A[i][m - 2] > A[i][m - 1].
For all j < m, A[0][j] < A[1][j] && A[n - 2][j] > A[n - 1][j]
We define a position [i, j] is a peak if:
    A[i][j] > A[i + 1][j] && A[i][j] > A[i - 1][j] && 
    A[i][j] > A[i][j + 1] && A[i][j] > A[i][j - 1]
```

Find a peak element in this matrix. Return the `index` of the peak.

```
Guarantee that there is at least one peak, and if there are multiple peaks, return any one of them.
```

**Example**

Example 1:

```
Input: 
    [
      [1, 2, 3, 6,  5],
      [16,41,23,22, 6],
      [15,17,24,21, 7],
      [14,18,19,20,10],
      [13,14,11,10, 9]
    ]
Output: [1,1]
Explanation: [2,2] is also acceptable. The element at [1,1] is 41, greater than every element adjacent to it.
```

Example 2:

```
Input: 
    [
      [1, 5, 3],
      [4,10, 9],
      [2, 8, 7]
    ]
Output: [1,1]
Explanation: There is only one peek.
```

**Challenge**

Solve it in `O(n+m)` time.

If you come up with an algorithm that you thought it is `O(nlogm)` or `O(mlogn)`, can you prove it is actually `O(n+m)` or propose a similar but `O(n+m)` algorithm?


**BFS (TLE)**

爬山法

先二分列(或者行都可以), 找到一个列上或者行上的最大值, 然后在最大值点处, "向上爬山", 在爬的过程中保证不会再越过这一列/行, 因为起点是最大值, 而且回向高处爬

```python
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
```

**二分列/行**

`O(n logm)` or `O(m logn)`

可以看哪一个大, 二分哪一个

```python
class Solution:
    """
    @param: A: An integer matrix
    @return: The index of the peak
    """
    def findPeakII(self, A):
        # write your code here
        if not A or len(A) == 0 or len(A[0]) == 0:
            return [-1, -1]

        # 二分列
        n, m = len(A), len(A[0])
        lo, hi = 0, len(A[0]) - 1
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            max_idx, max_num = -1, -1
            for row in range(n):
                if A[row][mid] > max_num:
                    max_num, max_idx = A[row][mid], row

            if A[max_idx][mid - 1] < A[max_idx][mid] and A[max_idx][mid] > A[max_idx][mid + 1]:
                return [max_idx, mid]
            elif A[max_idx][mid - 1] < A[max_idx][mid] < A[max_idx][mid + 1]:
                lo = mid
            elif A[max_idx][mid - 1] > A[max_idx][mid] > A[max_idx][mid + 1]:
                hi = mid
            else:
                hi = mid

        return [-1, -1]
```

**O(m + n)**

交叉的二分行和列

```python
# 本参考程序来自九章算法，由 @令狐冲 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    """
    @param: A: An integer matrix
    @return: The index of the peak
    """
    def findPeakII(self, A):
        if not A or not A[0]:
            return None
            
        return self.find_peak(A, 0, len(A) - 1, 0, len(A[0]) - 1)
        
    def find_peak(self, matrix, top, bottom, left, right):
        if top + 1 >= bottom and left + 1 >= right:
            for row in range(top, bottom + 1):
                for col in range(left, right + 1):
                    if self.is_peak(matrix, row, col):
                        return [row, col]
            return [-1, -1]

        if bottom - top < right - left:
            col = (left + right) // 2
            row = self.find_col_peak(matrix, col, top, bottom)
            if self.is_peak(matrix, row, col):
                return [row, col]
            if matrix[row][col - 1] > matrix[row][col]:
                return self.find_peak(matrix, top, bottom, left, col - 1)
            return self.find_peak(matrix, top, bottom, col + 1, right)

        row = (top + bottom) // 2
        col = self.find_row_peak(matrix, row, left, right)
        if self.is_peak(matrix, row, col):
            return [row, col]
        if matrix[row - 1][col] > matrix[row][col]:
            return self.find_peak(matrix, top, row - 1, left, right)
        return self.find_peak(matrix, row + 1, bottom, left, right)

    def is_peak(self, matrix, x, y):
        return matrix[x][y] == max(
            matrix[x][y],
            matrix[x - 1][y],
            matrix[x][y - 1],
            matrix[x][y + 1],
            matrix[x + 1][y],
        )

    def find_row_peak(self, matrix, row, left, right):
        peak_val = -sys.maxsize
        peak = []
        for col in range(left, right + 1):
            if matrix[row][col] > peak_val:
                peak_val = matrix[row][col]
                peak = col
        return peak

    def find_col_peak(self, matrix, col, top, bottom):
        peak_val = -sys.maxsize
        peak = None
        for row in range(top, bottom + 1):
            if matrix[row][col] > peak_val:
                peak_val = matrix[row][col]
                peak = row
        return peak
```