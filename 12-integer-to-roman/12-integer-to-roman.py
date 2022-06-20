class Solution:
    def intToRoman(self, num: int) -> str:
        match = {1:'I', 
                 4: 'IV', 
                 5: 'V', 
                 9: 'IX', 
                 10: 'X', 
                 40: 'XL', 
                 50: 'L', 
                 90: 'XC', 
                 100: 'C', 
                 400: 'CD', 
                 500: 'D', 
                 900: 'CM', 
                 1000: 'M'}
        ans = ''
        
        for key in reversed(match.keys()):
            if num >= key:
                freq = int(num/key)
                ans += match[key] * freq
                num %= key
                
        return ans
        
        
        
        