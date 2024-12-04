class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        currsum = 0
        sums = {0:1}

        for num in nums:
            currsum += num
            res += sums.get(currsum-k,0)
            sums[currsum] = sums.get(currsum,0) + 1

        return res