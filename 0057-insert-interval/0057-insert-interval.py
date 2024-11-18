class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i , interval in enumerate(intervals):
            #new interval is smaller than current 
            if newInterval[1] < interval[0]:
                res.append(newInterval)
                return res + intervals[i:]
            #new Interval is bigger than current then append current interval
            elif interval[1] < newInterval[0]:
                res.append(interval)
            #They are overlapping intervals
            else:
                newInterval[0] = min(newInterval[0],interval[0])
                newInterval[1] = max(newInterval[1],interval[1])
        res.append(newInterval)
        return res