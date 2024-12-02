class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        best = [1]*n
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                best[i] = best[i-1] + 1
            else:
                best[i] = 1
        
        mx = 1
        for i in range(1,n):
            prevstart = i - best[i] # total length - curr subarr length
            if prevstart >= 0:
                mx = max(mx,min(best[prevstart],best[i]))
            mx = max(mx, best[i] // 2)
        return mx