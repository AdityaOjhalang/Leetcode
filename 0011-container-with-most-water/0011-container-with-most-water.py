class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        res = float('-inf')
        low = 0
        high = n - 1
        while low < high:
            area = (high - low) * min(height[low],height[high])
            res = max(res,area)
            if height[low]<=height[high]:
                low+=1
            else:
                high-=1
        return res
            

