class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # If only one row or the string is shorter than numRows, return the string as is
        if numRows == 1 or numRows >= len(s):
            return s

        # Initialize a list to hold strings for each row
        rows = [''] * numRows
        curRow = 0
        goingDown = False

        # Traverse the input string
        for char in s:
            rows[curRow] += char
            # Change direction when reaching the top or bottom row
            if curRow == 0 or curRow == numRows - 1:
                goingDown = not goingDown
            curRow += 1 if goingDown else -1

        # Combine rows to form the final zigzag string
        return ''.join(rows)

# Example Usage
solution = Solution()
print(solution.convert("PAYPALISHIRING", 3))  # Output: "PAHNAPLSIIGYIR"
print(solution.convert("PAYPALISHIRING", 4))  # Output: "PINALSIGYAHRPI"
print(solution.convert("A", 1))  # Output: "A"
