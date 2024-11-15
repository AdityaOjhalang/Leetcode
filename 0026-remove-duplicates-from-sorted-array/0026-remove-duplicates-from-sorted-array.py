class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        toadd = 1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[toadd] = nums[i]
                toadd+=1
        return toadd