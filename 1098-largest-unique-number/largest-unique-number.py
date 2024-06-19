class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        hmap = Counter(nums)
        lar = -1
        for num in hmap:
            curr = hmap[num] 
            if curr < 2:
                lar = max(lar , num)
            else:
                continue
        return lar