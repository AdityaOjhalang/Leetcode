class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        res, maxcount = 0, 0

        for n in nums:
            count[n] = 1 + count.get(n, 0)
            if count[n] > maxcount:
                res = n
            maxcount = max(maxcount, count[n])

        return res