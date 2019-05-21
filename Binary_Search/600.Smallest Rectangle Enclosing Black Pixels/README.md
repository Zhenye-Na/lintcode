# 600. Smallest Rectangle Enclosing Black Pixels

**Description**

An image is represented by a binary matrix with `0` as a white pixel and `1` as a black pixel. The black pixels are connected, i.e., there is only one black region. Pixels are connected horizontally and vertically. Given the location `(x, y)` of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

**Example**

Example 1:

```
Input: ["0010","0110","0100"]，x = 0，y = 2
Output: 6
Explanation:
The upper left coordinate of the matrix is (0, 1), and the lower right coordinate is (2, 2).
```

Example 2:

```
Input: ["1110""1100""0000""0000"], x = 0, y = 1
Output: 6
Explanation:
The upper left coordinate of the matrix is (0, 0), and the lower right coordinate is (1, 2).
```


**Binary Search**

时间复杂度是 `O(max(mlogN, nlogM))`

```python
class Solution:
    
    def minArea(self, image, i, j):
        
        m, n = len(image), len(image[0])
        
        is_row_empty = lambda image, row : sum(int(cell) for cell in image[row]) == 0 
        is_col_empty = lambda image, col : sum(int(image[i][col]) for i in range(len(image))) == 0
        
        top = self.bisect_left(image, 0, i, is_row_empty)
        bottom = self.bisect_right(image, i, m, is_row_empty)
        left = self.bisect_left(image, 0, j, is_col_empty)
        right = self.bisect_right(image, j, n, is_col_empty)
        
        return (right - left + 1) * (bottom - top + 1)
        
    def bisect_left(self, image, lo, hi, is_file_empty):
        
        while lo < hi:
            mid = (lo+hi) // 2
            if is_file_empty(image, mid):
                lo += 1 
            else:
                hi = mid
        return lo
    
    def bisect_right(self, image, lo, hi, is_file_empty):
        
        while lo < hi:
            mid = (lo+hi) // 2
            if is_file_empty(image, mid):
                hi = mid
            else:
                lo = mid + 1     
        return lo - 1
```

**BFS**


```python
from collections import deque
import sys


class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """
    WHITE = "0"
    BLACK = "1"

    dX = [1, -1, 0, 0]
    dY = [0, 0, 1, -1]

    def minArea(self, image, x, y):
        # write your code here
        if not image or len(image) == 0 or len(image[0]) == 0:
            return 0

        min_x, max_x = sys.maxsize, - sys.maxsize
        min_y, max_y = sys.maxsize, - sys.maxsize

        m, n = len(image), len(image[0])

        start = [(i, j) for i in range(m) for j in range(n) if image[i][j] == self.BLACK]
        start_x, start_y = start[0]

        queue = deque([(start_x, start_y)])
        history = set((start_x, start_y))

        while queue:
            x, y = queue.popleft()

            # update
            if x < min_x:
                min_x = x
            if x > max_x:
                max_x = x
            if y < min_y:
                min_y = y
            if y > max_y:
                max_y = y

            for i in range(4):
                new_x, new_y = x + self.dX[i], y + self.dY[i]

                if not self._isValid(new_x, new_y, m, n, image):
                    continue

                if (new_x, new_y) not in history:
                    history.add((new_x, new_y))
                    queue.append((new_x, new_y))

        return (max_x - min_x + 1) * (max_y - min_y + 1)


    def _isValid(self, x, y, m, n, image):
        return 0 <= x < m and 0 <= y < n and image[x][y] == self.BLACK

```