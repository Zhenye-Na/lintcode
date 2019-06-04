# 156. Merge Intervals

**Description**

Given a collection of intervals, merge all overlapping intervals.

**Example**

Example 1:

```
Input: [(1,3)]
Output: [(1,3)]
```

Example 2:

```
Input:  [(1,3),(2,6),(8,10),(15,18)]
Output: [(1,6),(8,10),(15,18)]
```

**Challenge**

`O(n log n)` time and `O(1)` extra space.

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
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        # write your code here
        merged = []
        if not intervals or len(intervals) == 0:
            return merged

        intervals = sorted(intervals, key=lambda interval: (interval.start, interval.end))
        for i in range(len(intervals)):
            if len(merged) == 0 or merged[-1].end < intervals[i].start:
                merged.append(intervals[i])
            else:
                merged[-1].end = max(merged[-1].end, intervals[i].end)

        return merged
```

```cpp
/**
 * Definition of Interval:
 * classs Interval {
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    /**
     * @param intervals: interval list.
     * @return: A new interval list.
     */
    vector<Interval> merge(vector<Interval> &intervals) {
        // write your code here
        if (intervals.empty())
            return {};
        
        sort(intervals.begin(), intervals.end(), 
             [](const Interval & l, const Interval & r) { 
                 return l.start < r.start;
             });
        
        vector<Interval> res;
        for (const auto & interval: intervals) {
            if (res.empty() || interval.start > res.back().end)
                res.push_back(interval);
            else
                res.back().end = max(res.back().end, interval.end);
        }
        return res;
    }
};
```