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
