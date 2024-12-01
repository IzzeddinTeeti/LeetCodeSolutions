class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        negative = x < 0
        x = abs(x)

        # Reverse the digits of the absolute value
        reversed_x = 0
        while x != 0:
            digit = x % 10  # Get the last digit
            reversed_x = reversed_x * 10 + digit
            x //= 10  # Remove the last digit

        # Restore the negative sign if needed
        if negative:
            reversed_x = -reversed_x

        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0

        return reversed_x

        
        