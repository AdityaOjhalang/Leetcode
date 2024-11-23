class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        updates = [0] * (n + 1)  # because of end + 1

        for start, end in queries:
            updates[start] += 1
            updates[end + 1] -= 1

        for i in range(1, len(updates)):
            updates[i] += updates[i - 1]

        for i in range(len(nums)):
            if nums[i] > updates[i]:
                return False

        return True
