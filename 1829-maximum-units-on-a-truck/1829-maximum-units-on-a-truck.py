class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1],reverse = True)
        res = 0
        for amt , units in boxTypes:
            if truckSize <= 0:
                break
            while amt >0 and truckSize > 0:
                truckSize -= 1
                amt -= 1
                res += units
                
               
        return res
