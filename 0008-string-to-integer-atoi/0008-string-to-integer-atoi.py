class Solution:
    def myAtoi(self, s: str) -> int:

        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        s = s.lstrip()
        sign = 1
        ans = ''

        if not s:
            return 0

        if s[0] in ['-', '+']:
            sign = -1 if s[0] == '-' else 1
            s = s[1:]

        for char in s:
            if char.isdigit():
                ans += char
            else:
                break
        
        if not ans:
            return 0
            
        ans = int(ans)

        ans *= sign
        
        if ans < INT_MIN:
            ans = INT_MIN
        elif ans > INT_MAX:
            ans = INT_MAX

        return ans