# 364. Trapping Rain Water II

**Description**

Given `n x m` non-negative integers representing an elevation map 2d where the area of each cell is `1 x 1`, compute how much water it is able to trap after raining.

![](https://lintcode-media.s3.amazonaws.com/problem/trapping-rain-water-ii.jpg)

**Example**

Example 1:

```
Given `5*4` matrix 
Input:
[[12,13,0,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]
Output:
14
```

Example 2:

```
Input:
[[2,2,2,2],[2,2,3,4],[3,3,3,1],[2,3,4,5]]
Output:
0
```

**Heap 小顶堆**

将矩阵周边的格子都放到堆里，这些格子上面是无法盛水的。

每次在堆里挑出一个高度最小的格子 `cell`，把周围的格子加入到堆里。

这些格子被加入堆的时候，计算他们上面的盛水量。

```
盛水量 = cell.height - 这个格子的高度
```

当然如果这个值是负数，盛水量就等于 `0`。

```python
from heapq import heappush, heappop


class Solution:
    """
    @param heights: a matrix of integers
    @return: an integer
    """
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    borders = []
    visited = set([])

    def trapRainWater(self, heights):
        # write your code here
        if heights is None or len(heights) == 0 or len(heights[0]) == 0:
            return 0

        self._create_boders(heights)

        water = 0
        while self.borders:
            bar_height, x, y = heappop(self.borders)

            for d in range(4):
                new_x, new_y = x + self.dx[d], y + self.dy[d]

                if self._inBound(new_x, new_y):
                    water += max(0, bar_height - heights[new_x][new_y])
                    new_height = max(bar_height, heights[new_x][new_y])
                    heappush(self.borders, (new_height, new_x, new_y))
                    self.visited.add((new_x, new_y))

        return water

    def _create_boders(self, heights):
        self.m, self.n = len(heights), len(heights[0])
        for row in [0, self.m - 1]:
            for col in range(self.n):
                heappush(self.borders, (heights[row][col], row, col))
                self.visited.add((row, col))

        for col in [0, self.n - 1]:
            for row in range(self.m):
                heappush(self.borders, (heights[row][col], row, col))
                self.visited.add((row, col))

    def _inBound(self, x, y):
        return 0 <= x < self.m and 0 <= y < self.n and (x, y) not in self.visited
```