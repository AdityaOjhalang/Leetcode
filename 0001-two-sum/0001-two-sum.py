class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i,num in enumerate(nums):
            compl = target - num
            if compl in hmap:
                return [hmap[compl],i]
            hmap[num] = i
        