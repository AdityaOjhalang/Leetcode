class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float("inf")
        n = len(nums)

        for i,a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                currsum = a + nums[l] + nums[r]
                if abs(res-target) > abs(target-currsum):
                    res = currsum
                if currsum < target:
                    l += 1
                elif currsum > target:
                    r -= 1
                else:
                    return currsum
        return res
                