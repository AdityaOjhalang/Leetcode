class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points.sort(key = lambda x:x[0])
        arr=1
        lastend = points[0][1]
        for x_start , x_end in points:
            if x_start > lastend:
                arr += 1
                lastend = x_end
            lastend = min(x_end,lastend)
        return arr