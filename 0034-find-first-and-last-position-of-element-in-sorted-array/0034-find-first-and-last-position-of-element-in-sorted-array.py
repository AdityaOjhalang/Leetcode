class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def leftinsrt(arr,t):
            l,r = 0, len(arr)
            while l < r:
                mid = (l+r)//2
                if arr[mid] >= t:
                    r=mid
                else:
                    l= mid + 1
            return l
        def rightinsrt(arr,t):
            l,r = 0, len(arr)
            while l < r:
                mid = (l+r)//2
                if arr[mid] <= t:
                    l= mid + 1
                else:
                    r= mid 
            return l - 1
        
        l = leftinsrt(nums,target)
        r = rightinsrt(nums,target)
        if l <= r and r < len(nums) and nums[l] == target:
            return [l,r]
        else:
            return [-1,-1]