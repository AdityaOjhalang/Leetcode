class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        cost = 0
        while len(sticks) > 1:
            first,second = heapq.heappop(sticks),heapq.heappop(sticks)
            cost += first+second
            heapq.heappush(sticks,first+second)
        return cost