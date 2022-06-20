class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {'I':1,
                     'IV':4,
                     'V':5,
                     'IX':9,
                     'X':10,
                     'XL':40,
                     'L':50,
                     'XC':90,
                     'C':100,
                     'CD':400,
                     'D':500,
                     'CM':900,
                     'M':1000}
        ans = 0
        
        for i in range(len(s)):
            if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i+1]]:
                ans -=roman_map[s[i]]
            else:
                ans +=roman_map[s[i]]
                
        return ans
            