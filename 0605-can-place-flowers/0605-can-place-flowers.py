class Solution:
    def canPlaceFlowers(self, bed: List[int], n: int) -> bool:
        if n == 0:
            return True 
        for i in range(len(bed)):
            if bed[i] == 0:
                left = (i == 0) or (bed[i-1] == 0)
                right = (i == len(bed)-1) or (bed[i+1] == 0)
                if left and right:
                    bed[i] = 1
                    n -= 1
                    if n == 0:
                        return True

        return n == 0
