"""
Definition of Interval:
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

    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)

        previous_end = 0
        for i in intervals:
            start = i.start
            end = i.end
            if start < previous_end:
                return False
            previous_end = end

        return True


# print(Solution().can_attend_meetings([(0, 30), (5, 10), (15, 20)]))
# print(Solution().can_attend_meetings([(5,8),(9,15)]))
