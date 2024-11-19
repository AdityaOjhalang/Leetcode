class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        toadd = 1
        count = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                count = 1
            else:
                count +=1
            if count <= 2:
                nums[toadd] = nums[i]
                toadd += 1
        return toadd