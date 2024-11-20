class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        low = 0
        high = n - 1
        res = float("-inf")
        while low < high :
            area  =  min(height[low],height[high]) * (high - low)
            res = max(area,res)
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1
        return res