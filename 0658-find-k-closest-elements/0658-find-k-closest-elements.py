class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []

        for num in arr:
            diff = abs( x - num )
            heapq.heappush(heap,(-diff,-num))
            if len(heap) > k:
                heapq.heappop(heap)
        return sorted([-val[1] for val in heap])
