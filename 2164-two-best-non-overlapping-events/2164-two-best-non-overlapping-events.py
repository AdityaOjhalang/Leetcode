from typing import List
import heapq

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Step 1: Sort events by start time
        events.sort()
        
        max_sum = 0
        max_value_so_far = 0
        min_heap = []  # To store [endTime, value]
        
        for start, end, value in events:
            # Step 2: Remove all overlapping events from the heap
            while min_heap and min_heap[0][0] < start:
                _, heap_value = heapq.heappop(min_heap)
                max_value_so_far = max(max_value_so_far, heap_value)
            
            # Step 3: Update the maximum sum considering the current event
            max_sum = max(max_sum, value + max_value_so_far)
            
            # Step 4: Add the current event to the heap
            heapq.heappush(min_heap, (end, value))
        
        return max_sum
