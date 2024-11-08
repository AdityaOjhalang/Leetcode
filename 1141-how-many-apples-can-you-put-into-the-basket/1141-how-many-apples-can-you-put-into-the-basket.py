class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weights = sorted(weight)
        res = 0
        units = 0
        for i in range(len(weights)):
            units += weights[i]
            if units > 5000:
                break
            res += 1
        return res
            

            
