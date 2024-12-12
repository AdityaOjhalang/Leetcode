class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Helper function to expand around a center and find palindrome length
        def expand_around_center(left, right):
            # Expand as long as characters match and we are in bounds
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1  # Move left pointer outwards
                right += 1  # Move right pointer outwards
            # Return the valid palindrome substring length
            return right - left - 1  # Exclude the extra left/right moves

        # Edge case: empty string
        if not s or len(s) == 0:
            return ""
        
        start, end = 0, 0  # Initialize the start and end indices of the longest palindrome
        for i in range(len(s)):
            # Odd-length palindrome (center is a single character)
            len1 = expand_around_center(i, i)
            # Even-length palindrome (center is two characters)
            len2 = expand_around_center(i, i + 1)
            
            # Find the maximum length palindrome for the current center
            max_len = max(len1, len2)
            
            # Update start and end indices if a longer palindrome is found
            if max_len > (end - start):
                start = i - (max_len - 1) // 2  # Adjust start index
                end = i + max_len // 2  # Adjust end index
        
        # Return the longest palindrome substring
        return s[start:end + 1]

