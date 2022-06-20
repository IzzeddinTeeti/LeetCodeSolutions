class Solution:        
        
    def longestPalindrome(self, s: str) -> str:
        
        max_len = 0
        answer = ''
        
        n = len(s)
        if n < 2:
            return s
        
        for i in range(n):
            # for odd length
            l, r = i, i
            
            while (l >= 0 and r < n) and (s[l] == s[r]):
                if (r - l +1) > max_len:
                    answer = s[l:r+1]
                    max_len = r-l+1
                
                l -= 1
                r += 1
                       
            # for even length
            l, r = i, i+1
            
            while (l >= 0 and r < n) and (s[l] == s[r]):
                if (r - l +1) > max_len:
                    answer = s[l:r+1]
                    max_len = r-l+1
                
                l -= 1
                r += 1
                       
                    
        return answer
    
        
        