# 920. Meeting Rooms

**Description**

Given an array of meeting time intervals consisting of start and end times `[[s1,e1],[s2,e2],...]` `(si < ei)`, determine if a person could attend all meetings.

**Example**

Example 1

```
Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation: 
(0,30), (5,10) and (0,30),(15,20) will conflict
```

Example 2

```
Input: intervals = [(5,8),(9,15)]
Output: true
Explanation: 
Two times will not conflict
```

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
    @return: if a person could attend all meetings
    """

    def canAttendMeetings(self, intervals):
        # Write your code here
        if not intervals or len(intervals) == 0:
            return True

        new_intervals = []
        for interval in intervals:
            new_intervals.append((interval.start, 1))
            new_intervals.append((interval.end, -1))

        new_intervals.sort()
        running_num = 0
        for time, delta in new_intervals:
            running_num += delta
            if running_num > 1:
                return False
        return True
```
