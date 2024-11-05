class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda i: i[0])
        
        if len(intervals) <= 1: return True

        s, e = intervals[0]
        for start, end in intervals[1:]:
            if start < e : 
                return False
            s, e = start, end
        return True