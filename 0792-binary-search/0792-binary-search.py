class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n-1
        while left <= right:
            mid = (right + left) // 2
            val = nums[mid]
            if val == target:
                return mid
            if val > target:
                right = mid - 1
            if val < target:
                left = mid + 1
        
        return -1


 