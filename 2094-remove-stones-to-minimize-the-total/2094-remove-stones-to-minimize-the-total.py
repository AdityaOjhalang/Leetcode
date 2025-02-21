class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-num for num in piles]
        heapq.heapify(heap)

        for i in range(k):
            val = -heapq.heappop(heap)
            toremove = val//2
            heapq.heappush(heap,-(val-toremove))

        return -sum(heap)
        