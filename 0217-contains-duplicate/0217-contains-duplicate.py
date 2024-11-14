class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hmap = Counter(nums)
        for ind in hmap:
            if hmap[ind] >= 2:
                return True
        return False