class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r= 0 , n-1
        res = float("-inf")
        while l < r:
            currarea = min(height[l],height[r]) * (r-l)
            res = max(res,currarea)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res 