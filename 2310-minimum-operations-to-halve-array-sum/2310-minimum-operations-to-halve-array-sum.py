class Solution:
    def halveArray(self, nums: List[int]) -> int:
        targetsum = sum(nums) / 2 #sum we need to remove from array
        heap = [-num for num in nums]
        heapq.heapify(heap)

        steps = 0
        while targetsum > 0 :
            steps += 1
            val = abs(heapq.heappop(heap))/2
            targetsum -= val
            heapq.heappush(heap,-val)
        
        return steps