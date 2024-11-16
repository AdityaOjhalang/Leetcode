class Solution:
    def intToRoman(self, num: int) -> str:
        # Define a list of tuples with integer values and their corresponding Roman numeral symbols
        val_map = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]

        # Initialize an empty result string to store the Roman numeral
        result = ''
        
        # Iterate through each tuple in val_map
        for value, symbol in val_map:
            # While num is greater than or equal to the current value, subtract the value and append the symbol
            while num >= value:
                result += symbol
                num -= value
        
        return result
