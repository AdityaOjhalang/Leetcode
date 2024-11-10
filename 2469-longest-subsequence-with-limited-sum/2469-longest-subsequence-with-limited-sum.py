class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        def bs(arr, tar):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] > tar:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        nums.sort()
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        res = []
        for q in queries:
            indx = bisect.bisect_right(nums,q)
            res.append(indx)
        return res

        