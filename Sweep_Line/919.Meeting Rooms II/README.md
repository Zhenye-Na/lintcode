# 919. Meeting Rooms II

**Description**

Given an array of meeting time intervals consisting of start and end times `[[s1,e1],[s2,e2],...](si < ei)`, find the minimum number of conference rooms required.

**Example**

Example 1

```
Input: intervals = [(0,30),(5,10),(15,20)]
Output: 2
Explanation:
We need two meeting rooms
room1: (0,30)
room2: (5,10),(15,20)
```

Example 2

```
Input: intervals = [(2,7)]
Output: 1
Explanation: 
Only need one meeting room
```

**Sweep Line**

把区间打散成 `(start, 1)` 和 `(end, -1)` 在用扫描线扫一次, 取最大值

```python
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        if not intervals or len(intervals) == 0:
            return 0

        new_intervals = []
        for interval in intervals:
            new_intervals.append([interval.start, 1])
            new_intervals.append([interval.end, -1])

        new_intervals.sort()
        min_rooms, curr_rooms = 0, 0
        for _, delta in new_intervals:
            curr_rooms += delta
            min_rooms = max(min_rooms, curr_rooms)

        return min_rooms
```