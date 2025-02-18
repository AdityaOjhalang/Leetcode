class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def check(div):
            totalsum = 0
            for num in nums:
                totalsum += ceil(num/div) 
            return totalsum <= threshold 
        
        l = 1
        r = max(nums)
        while l < r:
            k = (l + r)//2
            if check(k):
                r = k
            else:
                l = k + 1
        return l

