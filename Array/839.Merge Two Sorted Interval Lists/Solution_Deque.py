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
