class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                # Minimum must be in the right part
                left = mid + 1
            else:
                # Minimum could be mid or in the left part
                right = mid

        # When left == right, we have found the minimum element
        return nums[left]
