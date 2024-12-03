class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def leftinsrt(arr,t):
            l,r = 0 , len(arr)
            while l < r:
                mid = (l+r)//2
                if arr[mid] >= t:
                    r = mid
                else:
                    l = mid + 1
            return l

        def rightinsrt(arr,t):
            l,r = 0 , len(arr)
            while l < r:
                mid = (l+r)//2
                if arr[mid] <= t:
                    l = mid + 1
                else:
                    r = mid
            return l - 1
        
        left = leftinsrt(nums,target)
        right = rightinsrt(nums,target)

        if left <= right and left < len(nums) and nums[left] == target:
            return [left, right]
        else:
            return [-1,-1]