class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        res = []
        for q in queries:
            indx = bisect.bisect_right(nums,q)
            res.append(indx)
        return res

        