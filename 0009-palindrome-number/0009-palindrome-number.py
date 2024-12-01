class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        n = len(x)

        split = n//2
        first = x[:split]
        second = x[split:] if n%2==0 else x[split+1:]
        second = second[::-1]

        return first == second
        