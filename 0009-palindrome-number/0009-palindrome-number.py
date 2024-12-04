class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False
        
        # Use helper function to reverse the number
        def reverse_number(n: int) -> int:
            rev = 0
            while n > 0:
                rev = rev * 10 + n % 10
                n //= 10
            return rev
        
        # Get the reversed number
        reversed_x = reverse_number(x)
        
        # Check if the reversed number is equal to the original number
        return x == reversed_x
