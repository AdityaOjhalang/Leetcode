class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        nums.sort()
        res = []

        for i , a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            
            l = i+1
            r = n-1

            while(l < r):
                currsum = a + nums[l] + nums[r]
                if currsum < 0:
                    l+=1
                elif currsum > 0:
                    r-=1
                else:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r :
                        l+=1
                    
        return res
