class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        def leftstart(arr, target):
            left = 0
            right = len(arr)

            while left < right:
                mid = (left + right) // 2
                val = arr[mid]
                if val >= target:
                    right = mid 
                else:
                    left = mid + 1

            return left

        potions.sort()
        res = []
        n = len(potions)
        for spell in spells:
            ind = leftstart(potions, success / spell)
            res.append(n - ind)
        return res
