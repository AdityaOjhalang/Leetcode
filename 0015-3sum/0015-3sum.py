class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []

        for i , a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            
            low = i + 1 
            high = n - 1

            while low < high:
                curr = a + nums[low] + nums[high]
                if curr > 0:
                    high -= 1
                elif curr < 0 :
                    low += 1
                else:
                    res.append([a,nums[low],nums[high]])
                    low += 1
                    while low < high and nums[low-1] == nums[low]:
                        low+=1
        return res