class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        counts = {0: -1}
        maxlen = 0
        count = 0

        for index, num in enumerate(nums):
            if num == 0:
                count -= 1
            if num == 1:
                count += 1
            if count in counts:
                maxlen = max(maxlen, index - counts[count])
            else:
                counts[count] = index

        return maxlen
