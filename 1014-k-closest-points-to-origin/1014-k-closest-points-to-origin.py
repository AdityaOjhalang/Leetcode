class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x,y in points:
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(heap,(-dist,(x,y)))
            if len(heap) > k:
                heapq.heappop(heap)
        return [val[1] for val in heap]