class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[0])
        arrows = 1
        last_end = points[0][1]

        for x_start , x_end in points:
            if x_start > last_end:
                arrows+=1
                last_end = x_end
            else:
                last_end = min(x_end,last_end)
        return arrows