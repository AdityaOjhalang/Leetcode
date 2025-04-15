class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        def check(k):
            hours = 0
            for banana in piles:
                hours += ceil(banana / k)
            return hours <= h
        
        l,r = 1,max(piles)
        while l < r:
            mid = (l + r)// 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l

