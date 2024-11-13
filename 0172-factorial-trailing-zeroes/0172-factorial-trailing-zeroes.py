class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeros = 0
        power_of_5 = 5
        while n >= power_of_5:
            zeros += n // power_of_5
            power_of_5 *= 5
        return zeros
