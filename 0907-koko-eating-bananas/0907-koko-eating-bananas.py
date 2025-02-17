class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            hours = 0
            for pile in piles:
                hours += ceil(pile/k)
            return hours <= h
        
        l , r = 1, max(piles)
        while l <= r:
            k = (l+r)// 2
            if check(k):
                r = k - 1
            else:
                l = k+1
        return l    