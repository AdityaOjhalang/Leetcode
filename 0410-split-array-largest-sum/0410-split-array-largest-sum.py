class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(tot):
            subarr = 1
            currsum = 0
            for num in nums:
                currsum += num
                if currsum > tot:
                    subarr += 1
                    currsum = num
            return subarr <= k

        l, r = max(nums), sum(nums)
        res = r
        while l < r:
            mid = ( l + r )//2
            if check(mid):
                res = mid
                r = mid
            else:
                l = mid + 1
        return res