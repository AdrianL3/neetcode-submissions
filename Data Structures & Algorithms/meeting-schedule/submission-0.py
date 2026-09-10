"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_intervals = sorted(intervals, key=lambda var: var.start)
        end = -1

        for time in sorted_intervals:
            if time.start < end:
                return False
            end = time.end

        return True
