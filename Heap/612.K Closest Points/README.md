# 612. K Closest Points

**Description**

Given some points and an origin point in two-dimensional space, find `k` points which are *nearest* to the origin.

```
Return these points sorted by distance, if they are same in distance, sorted by the x-axis, and if they are same in the x-axis, sorted by y-axis.
```

**Example**

Example 1:

```
Input: points = [[4,6],[4,7],[4,4],[2,5],[1,1]], origin = [0, 0], k = 3 
Output: [[1,1],[2,5],[4,4]]
```

Example 2:

```
Input: points = [[0,0],[0,9]], origin = [3, 1], k = 1
Output: [[0,0]]
```

**Priority Queue**

heapq 小顶堆

这里用到了一个 trick, 就是把所有的都变成负的, 因为 heapq 是小顶堆, 距离越远, 取负数就越小, 那么就最先 pop 出去, x y 坐标同理

最后 k 个就是答案咯


```python
import heapq


"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        # write your code here
        pq = []
        for point in points:
            triplet = [-self._computeDistance(point, origin), -point.x, -point.y]
            heapq.heappush(pq, triplet)
            if len(pq) > k:
                heapq.heappop(pq)

        res = []
        while len(pq) > 0:
            _, x, y = heapq.heappop(pq)
            res.append(Point(-x, -y))

        return res[::-1]


    def _computeDistance(self, point, origin):
        return (point.x - origin.x) ** 2 + (point.y - origin.y) ** 2
```