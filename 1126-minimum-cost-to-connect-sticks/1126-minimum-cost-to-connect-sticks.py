class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heap = [stick for stick in sticks]
        heapq.heapify(heap)
        total = 0 
        while len(heap)>1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            val  = second+first
            total += val
            heapq.heappush(heap,val)
        
        return total