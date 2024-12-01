class Solution:
    def reverse(self, x: int) -> int:
        int_min = -2**31
        int_max = 2**31 - 1
        
        negative = x < 0
        x = abs(x)
        reversed_x = 0

        while x != 0:
            number = x % 10
            reversed_x = reversed_x * 10 + number
            x = x // 10
        
        if negative:
            reversed_x *= -1


        if reversed_x < int_min or reversed_x > int_max:
            return 0
        
        return reversed_x
        



        
        