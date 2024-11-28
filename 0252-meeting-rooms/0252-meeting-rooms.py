class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(1,len(intervals)):
            if intervals[i][0] < intervals[i-1][1]: #start time of next < end time of prev
                return False
        return True