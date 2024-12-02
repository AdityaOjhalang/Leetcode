class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)

        def good(target):
            updates = [0] * (n + 1)
            for start, end, val in queries[:target]:
                updates[start] += val
                updates[end + 1] -= val
            
            for i in range(1, n + 1):
                updates[i] += updates[i - 1]
            
            for i in range(n):
                if nums[i] > updates[i]:
                    return False
            return True

        l, r = 0, len(queries)+1  # Use len(queries) here
        while l < r:
            mid = (l + r) // 2
            if good(mid):
                r = mid
            else:
                l = mid + 1

        if l == len(queries)+1:  # If we exhausted all queries and couldn't zero out
            return -1
        return l
