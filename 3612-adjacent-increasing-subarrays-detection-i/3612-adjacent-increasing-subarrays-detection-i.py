class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        
        def checkinc(i):
            for j in range(i,i+k-1):
                if nums[j] >= nums[j+1]:
                    return False
            return True
        
        n = len(nums)
        for i in range(n - 2*k + 1):
            if checkinc(i) and checkinc(i + k):
                return True
        return False
