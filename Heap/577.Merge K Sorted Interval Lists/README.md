# 577. Merge K Sorted Interval Lists

**Description**

Merge `K` sorted interval lists into one sorted interval list. You need to merge overlapping intervals too.

**Example**

Example 1

```
Input: [
  [(1,3),(4,7),(6,8)],
  [(1,2),(9,10)]
]
Output: [(1,3),(4,8),(9,10)]
```

Example2

```
Input: [
  [(1,2),(5,6)],
  [(3,4),(7,8)]
]
Output: [(1,2),(3,4),(5,6),(7,8)]
```

**Heap**

```python
import heapq


"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """
    def mergeKSortedIntervalLists(self, intervals):
        # write your code here
        if not intervals or len(intervals) == 0:
            return intervals

        heap, merged = [], []
        for idx, interval in enumerate(intervals):
            if interval:
                heapq.heappush(heap, (interval[0].start, interval[0].end, idx, 0))

        while heap:
            start, end, idx1, idx2 = heap[0]
            heapq.heappop(heap)
            if len(merged) == 0 or merged[-1].end < start:
                merged.append(Interval(start, end))
            else:
                merged[-1].end = max(merged[-1].end, end)

            if idx2 + 1 < len(intervals[idx1]):
                heapq.heappush(heap, (intervals[idx1][idx2 + 1].start, intervals[idx1][idx2 + 1].end, idx1, idx2 + 1))

        return merged
```

**Divide and Conquer**

```python
from collections import deque


"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """
    def mergeKSortedIntervalLists(self, intervals):
        # write your code here
        if not intervals or len(intervals) == 0:
            return intervals

        return self._divideConquer(intervals, 0, len(intervals) - 1)

    def _divideConquer(self, intervals, start, end):
        if start == end:
            return intervals[start]

        mid = start + (end - start) // 2
        left = self._divideConquer(intervals, start, mid)
        right = self._divideConquer(intervals, mid + 1, end)

        return self._mergeIntervalLists(left, right)

    def _mergeIntervalLists(self, left, right):
        left, right = deque(left), deque(right)
        interval = None
        merged = []

        while left and right:
            if left[0].start < right[0].start:
                interval = left.popleft()
            else:
                interval = right.popleft()

            if len(merged) == 0 or merged[-1].end < interval.start:
                merged.append(interval)
            else:
                merged[-1].end = max(merged[-1].end, interval.end)

        while left:
            interval = left.popleft()
            if len(merged) == 0 or merged[-1].end < interval.start:
                merged.append(interval)
            else:
                merged[-1].end = max(merged[-1].end, interval.end)

        while right:
            interval = right.popleft()
            if len(merged) == 0 or merged[-1].end < interval.start:
                merged.append(interval)
            else:
                merged[-1].end = max(merged[-1].end, interval.end)

        return merged
```
