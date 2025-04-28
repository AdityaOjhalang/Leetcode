class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0  # Initialize the counter for valid subarrays
        
        # Iterate through the array, making sure to stop 2 elements before the end
        for i in range(len(nums) - 2):
            first = nums[i]          # First number of the subarray
            middle = nums[i + 1]      # Middle number of the subarray
            third = nums[i + 2]       # Last number of the subarray
            
            # Check if sum of first and third equals half of the middle
            if 2*(first + third) == middle:
                count += 1  # If the condition matches, increment the counter
        
        return count  # Return the total count
        