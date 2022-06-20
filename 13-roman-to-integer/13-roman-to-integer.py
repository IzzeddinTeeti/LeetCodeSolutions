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
        
        current_ind = 0
        while current_ind <= len(s)-1:
            if (len(s)-1 - current_ind) >= 1 and (s[current_ind] + s[current_ind+1]) in roman_map.keys():
                ans += roman_map[s[current_ind] + s[current_ind+1]]
                current_ind +=2
                
            else:
                ans += roman_map[s[current_ind]]
                current_ind +=1
                
        return ans
            