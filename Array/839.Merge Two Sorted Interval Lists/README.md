# 839. Merge Two Sorted Interval Lists

**Description**

Merge two *sorted* (ascending) lists of interval and return it as a new sorted list. The new sorted list should be made by splicing together the intervals of the two lists and sorted in ascending order.

```
The intervals in the given list do not overlap.
The intervals in different lists may overlap.
```

**Example**

Example 1

```
Input: list1 = [(1,2),(3,4)] and list2 = [(2,3),(5,6)]
Output: [(1,4),(5,6)]
Explanation:
(1,2),(2,3),(3,4) --> (1,4)
(5,6) --> (5,6)
```

Example 2

```
Input: list1 = [(1,2),(3,4)] and list2 = [(4,5),(6,7)]
Output: [(1,2),(3,5),(6,7)]
Explanation:
(1,2) --> (1,2)
(3,4),(4,5) --> (3,5)
(6,7) --> (6,7)
```

**Deque (Queue)**

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
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """
    def mergeTwoInterval(self, list1, list2):
        # write your code here
        merged = []
        if not list1 and not list2:
            return merged

        if len(list1) == 0:
            return list2

        if len(list2) == 0:
            return list1

        l1, l2 = deque(l1), deque(l2)
        i, j = 0, 0
        interval = None
        while l1 and l2:
            if l1[0].start < l2[0].start:
                interval = l1.popleft()
            else:
                interval = l2.popleft()
            
            if len(merged) == 0 or merged[-1].end < interval.start:
                merged.append(interval)
            else:
                merged[-1].end = max(merged[-1].end, interval.end)

        while l1:
            interval = l1.popleft()
            if len(merged) == 0 or merged[-1].end < interval.start:
                merged.append(interval)
            else:
                merged[-1].end = max(merged[-1].end, interval.end)

        while l2:
            interval = l2.popleft()
            if len(merged) == 0 or merged[-1].end < interval.start:
                merged.append(interval)
            else:
                merged[-1].end = max(merged[-1].end, interval.end)

        return merged
```
