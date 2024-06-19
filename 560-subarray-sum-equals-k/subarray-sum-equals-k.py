class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        currsum = 0
        prefixsums = {0 : 1}

        for n in nums:
            currsum += n
            todel = currsum - k
            res += prefixsums.get(todel,0)
            prefixsums[currsum] = prefixsums.get(currsum,0) + 1
            
        return res