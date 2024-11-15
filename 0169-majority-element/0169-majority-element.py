class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hmap = Counter(nums)
        for i in hmap:
            if hmap[i] > len(nums) / 2:
                return i