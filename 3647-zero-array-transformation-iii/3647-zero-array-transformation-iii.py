from typing import List
from heapq import heappush, heappop
from collections import deque

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        # Sort the queries by their left bounds to process them in order
        sorted_queries = deque(sorted(queries))  # Queries are now sorted based on start (li)
        
        # Min-heap to store the right bounds (ri) of available queries
        available_right_bounds = []  
        
        # Min-heap to track the "currently working" right bounds (indices being processed)
        current_working_bounds = []
        
        # Traverse through each index in nums
        for index in range(len(nums)):
            
            # Step 1: Add all queries whose left bound <= current index
            # Push their right bounds (negated for max-heap behavior) into available_right_bounds
            while sorted_queries and sorted_queries[0][0] <= index:
                _, right_bound = sorted_queries.popleft()
                heappush(available_right_bounds, -right_bound)  # Use negative for max-heap
                
            # Step 2: Remove expired right bounds from the working set
            # "Expired" means the bound is less than the current index
            while current_working_bounds and current_working_bounds[0] < index:
                heappop(current_working_bounds)
            
            # Step 3: Ensure we can decrement `nums[index]` enough times
            # nums[index] tells us how many decrements are required at this index
            while nums[index] > len(current_working_bounds):
                # If available_right_bounds has valid queries covering the current index
                if available_right_bounds and -available_right_bounds[0] >= index:
                    # Pop the right bound from the available queries and add it to the working set
                    heappush(current_working_bounds, -heappop(available_right_bounds))
                else:
                    # If no valid right bounds are available, return -1 (impossible case)
                    return -1
        
        # Remaining valid queries in the available_right_bounds
        return len(available_right_bounds)
