class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:

        n = len(costs)
        left, right = [], []
        l, r = 0, n - 1  
        res = 0

        for i in range(candidates):
            if l <= r:
                heapq.heappush(left,(costs[l],l))
                l += 1
            if l <= r:
                heapq.heappush(right,(costs[r],r))
                r -= 1
        
        for i in range(k):
            if left and (not right or left[0] <= right[0]):
                cost , _ = heapq.heappop(left)
                res += cost
                if l <= r:
                    heapq.heappush(left,(costs[l],l))
                    l += 1
            else:
                cost, _ = heapq.heappop(right)
                res += cost 
                if l <= r:
                    heapq.heappush(right,(costs[r],r))
                    r -= 1
        return res

