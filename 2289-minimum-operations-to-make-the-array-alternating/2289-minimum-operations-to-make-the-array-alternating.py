class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        from collections import Counter
        
        n = len(nums)
        
        # Count frequencies separately for even and odd indexed elements
        even_count = Counter(nums[i] for i in range(0, n, 2))
        odd_count = Counter(nums[i] for i in range(1, n, 2))

        # Get the two most common elements and their counts for even indices
        even_common = even_count.most_common(2)
        # Get the two most common elements and their counts for odd indices
        odd_common = odd_count.most_common(2)

        # Fill missing entries with (0,0) if there are less than 2 distinct numbers
        if len(even_common) < 2:
            even_common.append((0, 0))
        if len(odd_common) < 2:
            odd_common.append((0, 0))

        # Case 1: Most common numbers for even and odd indices are different
        if even_common[0][0] != odd_common[0][0]:
            operations = (n // 2 + n % 2 - even_common[0][1]) + (n // 2 - odd_common[0][1])
        else:
            # Case 2: Most common numbers are the same → pick the better second-best
            option1 = (n // 2 + n % 2 - even_common[1][1]) + (n // 2 - odd_common[0][1])
            option2 = (n // 2 + n % 2 - even_common[0][1]) + (n // 2 - odd_common[1][1])
            operations = min(option1, option2)

        return operations