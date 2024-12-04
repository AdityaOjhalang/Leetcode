class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[0])
        heap = []
        heapq.heappush(heap, intervals[0][1])
        rooms = 1
        for interval in intervals[1:]:
            if interval[0] < heap[0]:
                rooms+=1
            else:
                heapq.heappop(heap)
            
            heapq.heappush(heap,interval[1])
        return rooms
                