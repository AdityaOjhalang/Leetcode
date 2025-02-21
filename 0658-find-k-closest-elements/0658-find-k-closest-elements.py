class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for num in arr:
            delta = abs(x - num)
            heapq.heappush(heap, (-delta, -num))
            if len(heap) > k:
                heapq.heappop(heap)
        return sorted([-val[1] for val in heap])
