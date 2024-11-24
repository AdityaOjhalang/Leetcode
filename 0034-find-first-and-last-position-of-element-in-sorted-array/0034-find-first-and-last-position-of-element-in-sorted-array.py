class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def leftinsrt(arr,t):
            left , right = 0 , len(arr)
            while left < right:
                mid = (left + right)//2
                if arr[mid] >= t:
                    right = mid
                else:
                    left = mid + 1
            return left

        def rightinst(arr,t):
            left,right = 0, len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid] > t:
                    right = mid
                else:
                    left = mid + 1
            return left - 1
        
        left = leftinsrt(nums,target)
        right = rightinst(nums,target)

        if left <= len(nums) - 1 and nums[left] == target and left <= right:
            return [left,right]
        else:
            return [-1,-1]
        

        