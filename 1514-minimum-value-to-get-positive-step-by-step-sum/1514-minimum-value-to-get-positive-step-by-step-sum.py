class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        pref = [nums[0]]
        for i in range(1,len(nums)):
            pref.append(nums[i] + pref[-1])
        lowest = min(pref)
        if lowest < 1:
            return abs(lowest) + 1
        else:
            return 1
        