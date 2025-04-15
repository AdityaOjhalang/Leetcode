class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []
        n = len(potions)

        def leftindx(target):
            l,r = 0,len(potions)
            while l < r:
                mid = (l + r) // 2 
                if potions[mid] >= target:
                    r = mid
                else:
                    l = mid + 1
            return l
        
        for spell in spells:
            target = success/spell
            ind = leftindx(target)
            res.append(n-ind)
        return res