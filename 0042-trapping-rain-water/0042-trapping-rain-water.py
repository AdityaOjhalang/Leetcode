class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lmax = height[0]
        rmax = height[n-1]
        l = 0
        r = n-1
        water = 0
        while l < r:
            if lmax <= rmax:
                l += 1
                lmax = max(lmax,height[l])
                water += lmax - height[l]
            else:
                r -= 1
                rmax = max(rmax,height[r])
                water += rmax - height[r]
        return water