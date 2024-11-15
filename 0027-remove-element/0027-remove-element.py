class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        toadd = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[toadd] = nums[i]
                toadd += 1
        return toadd