class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = Counter(nums)
        heap = []
        for val,freq in hmap.items():
            heapq.heappush(heap,(freq,val))
            if len(heap) > k:
                heapq.heappop(heap)
        return list(val[1] for val in heap)