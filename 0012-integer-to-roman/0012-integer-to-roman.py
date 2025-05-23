class Solution:
    def intToRoman(self, num: int) -> str:
        # Define the mapping of integers to Roman numerals
        value_symbols = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

        roman_numeral = ""

        # Iterate through each value-symbol pair
        for value, symbol in value_symbols:
            # Append the corresponding Roman symbols
            while num >= value:
                roman_numeral += symbol
                num -= value

        return roman_numeral
