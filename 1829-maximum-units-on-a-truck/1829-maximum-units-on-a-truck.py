class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1],reverse = True)
        res = 0
        for boxes , units in boxTypes:
            if truckSize <= 0:
                break
            boxtotake = min(truckSize,boxes)
            res += boxtotake * units
            truckSize -= boxtotake
                
        return res
