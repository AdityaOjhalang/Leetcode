class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = list(zip(nums2,nums1))
        pairs.sort(reverse = True)
        currsum = res = 0

        heap = []
        for nums2,nums1 in pairs:
            heapq.heappush(heap,nums1)
            currsum += nums1
            if len(heap) > k :
                smallest = heapq.heappop(heap)
                currsum -= smallest
            if len(heap) == k:
                res = max(res,currsum * nums2)

        return res 

