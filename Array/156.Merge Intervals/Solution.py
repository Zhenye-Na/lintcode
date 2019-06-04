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
