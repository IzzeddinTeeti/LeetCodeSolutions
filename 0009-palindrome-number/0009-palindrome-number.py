class Solution:
    def isPalindrome(self, x: int) -> bool:
        # x = str(x)
        # n = len(x)

        # split = n//2
        # first = x[:split]
        # second = x[split:] if n%2==0 else x[split+1:]
        # second = second[::-1]

        # return first == second
        if x < 0:
            return False

        if x >=0 and x < 10:
            return True

        origional = x
        reversed_x = 0

        while x:
            number = x % 10
            reversed_x = reversed_x * 10 + number
            x = x // 10
            # print(x, reversed_x)

        return origional == reversed_x

        # s = str(x)
        # return s == s[::-1]
        