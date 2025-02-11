class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []

        def leftindx(arr,target):
            left , right = 0 , len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid] >= target:
                    right = mid 
                else:
                    left = mid + 1
            return left
        
        n = len(potions)
        for spell in spells:
            ind = leftindx(potions,success/spell)
            res.append(n-ind)
        return res 