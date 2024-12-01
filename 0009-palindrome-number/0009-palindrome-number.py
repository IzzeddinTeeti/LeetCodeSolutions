class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        n = len(x)
        
        # if n == 2:
        #     return x[0] ==x[1]

        split = n//2
        first = x[:split]
        second = x[split:] if n%2==0 else x[split+1:]
        second = second[::-1]
        # second = reversed(second).item()
        print(split, first, second)

        return first == second
        