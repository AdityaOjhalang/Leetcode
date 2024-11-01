class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-num for num in piles]
        heapq.heapify(heap)

        ans = 0

        while ans < k:
            val = -heapq.heappop(heap)
            toremove = val//2
            heapq.heappush(heap,-(val-toremove))
            ans+=1

        return -sum(heap)
        