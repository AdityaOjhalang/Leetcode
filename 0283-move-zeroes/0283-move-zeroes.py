class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        toadd = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i],nums[toadd] = nums[toadd],nums[i]
                toadd += 1
        