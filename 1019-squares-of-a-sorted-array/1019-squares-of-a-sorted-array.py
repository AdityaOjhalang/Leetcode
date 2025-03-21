class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l,r = 0,len(nums) - 1
        res = [0]*len(nums)
        pos = len(res) - 1
        while l <= r:
            sq1 = nums[l]**2
            sq2 = nums[r]**2
            if sq1 > sq2:
                res[pos] = sq1
                l += 1
            else:
                res[pos] = sq2
                r -= 1
            pos -= 1
        return res
