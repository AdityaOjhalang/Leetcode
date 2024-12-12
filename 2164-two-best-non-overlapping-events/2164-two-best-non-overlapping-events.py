from typing import List
from bisect import bisect_right

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Step 1: Sort events based on their end times
        events.sort(key=lambda x: x[1])  # Sort by endTime
        
        # To store the best value seen so far and the corresponding end time
        best_value = 0
        max_sum = 0
        event_values = []  # Stores [endTime, max_value_so_far]
        
        for i in range(len(events)):
            start, end, value = events[i]
            
            # Step 2: Binary Search to find the best previous event that doesn't overlap
            pos = bisect_right(event_values, [start - 1, float('inf')]) - 1
            
            # Value if we include the current event with a previous best non-overlapping event
            total_value = value
            if pos >= 0:
                total_value += event_values[pos][1]
            
            # Update the max sum
            max_sum = max(max_sum, total_value)
            
            # Step 3: Update the best value seen so far
            best_value = max(best_value, value)
            
            # Append to event_values list for binary search
            event_values.append([end, best_value])
        
        return max_sum
