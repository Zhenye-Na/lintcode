# 821. Time Intersection

**Description**

Give two users' ordered online time series, and each section records the user's login time point `x` and offline time point `y`. Find out the time periods when both users are online at the same time, and output in ascending order. you need return a list of `intervals`.

```
We guarantee that the length of online time series meet 1 <= len <= 1e6.
For a user's online time series, any two of its sections do not intersect.
```

**Example**

Example 1:

```
Input: seqA = [(1,2),(5,100)], seqB = [(1,6)]
Output: [(1,2),(5,6)]
Explanation: In these two time periods (1,2), (5,6), both users are online at the same time.
```

Example 2:

```
Input: seqA = [(1,2),(10,15)], seqB = [(3,5),(7,9)]
Output: []
Explanation: There is no time period, both users are online at the same time.
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
    @param seqA: the list of intervals
    @param seqB: the list of intervals
    @return: the time periods
    """
    def timeIntersection(self, seqA, seqB):
        # Write your code here
        if not seqA or not seqB or len(seqA) == 0 or len(seqB) == 0:
            return []

        timelines = []
        for a in seqA:
            timelines.append((a.start, 1))
            timelines.append((a.end, -1))

        for b in seqB:
            timelines.append((b.start, 1))
            timelines.append((b.end, -1))

        timelines.sort()

        results = []
        start_time, end_time = -1, -1
        running_count, max_count = 0, 0
        for time, delta in timelines:
            running_count += delta
            if running_count == 2 and max_count < 2:
                start_time = time
                max_count = running_count

            elif running_count < 2 and max_count == 2:
                end_time = time
                max_count = running_count

            if start_time != -1 and end_time != -1:
                results.append(Interval(start_time, end_time))
                start_time, end_time = -1, -1

        return results
```