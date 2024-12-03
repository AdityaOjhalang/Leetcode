class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        res = float("inf")
        visited = set()
        for x1,y1 in points:
            for x2,y2 in visited:
                if (x1,y2) in visited and (x2,y1) in visited:
                    area = abs(y2-y1) * abs(x2-x1)
                    res = min(res,area)

            visited.add((x1,y1))
                
        return res if res != float("inf") else 0