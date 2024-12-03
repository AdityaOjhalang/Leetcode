class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        points.sort(key = lambda x : x[0])
        n = len(points)
        res = 1
        start = points[0][0]
        for currstart , _ in points:
            if currstart - start > w:
                res += 1
                start = currstart
        return res 