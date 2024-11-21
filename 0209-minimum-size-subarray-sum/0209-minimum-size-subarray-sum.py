class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        size = n + 1
        low = 0
        currsum = 0  # Start with the first element
        for high in range(0, n):  # Start high from 1
            currsum += nums[high]  # Add nums[high] to the current sum
            while currsum >= target:
                size = min(size, high - low + 1)
                currsum -= nums[low]
                low += 1
        return 0 if size == n + 1 else size
