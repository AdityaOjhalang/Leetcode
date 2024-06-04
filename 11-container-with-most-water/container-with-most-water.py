class Solution:
    def maxArea(self, height: List[int]) -> int:

        n = len(height)
        res = 0
        lmax = height[0]
        rmax = height[n-1]
        l = 0
        r = n-1

        while(l<r):
            area = (r-l)*min(height[l],height[r])
            res = max(area,res)
            

            if(lmax<rmax):
                l+=1
                lmax = max(height[l],lmax)
            else:
                r-=1
                rmax = max(height[r],rmax)

        return res