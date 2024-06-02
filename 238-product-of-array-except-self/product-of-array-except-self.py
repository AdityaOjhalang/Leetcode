class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        result = [1] * n

        # Create prefix product array
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i]

        # Create suffix product array
        suffix[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i]

        # Calculate result using prefix and suffix arrays
        for i in range(n):
            if i == 0:
                result[i] = suffix[i + 1]
            elif i == n - 1:
                result[i] = prefix[i - 1]
            else:
                result[i] = prefix[i - 1] * suffix[i + 1]

        return result
