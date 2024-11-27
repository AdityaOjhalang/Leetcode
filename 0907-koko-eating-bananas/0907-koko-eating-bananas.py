class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r =  1, max(piles)
        res = 0
        while l < r:
            k = (l+r)//2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            
            if hours <= h:
                res = min(k,res)
                r = k 
            else:
                l = k + 1
        return l