class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        # s = set(s)
#         s = list(s)
#         t = list(t)
        
        tot_s = sum([ord(char) for char in s])
        tot_t = sum([ord(char) for char in t])
        
        diff = tot_t - tot_s
        
        return chr(diff)
        
#         for char in s:
#             if char in t:
#                 del t[char]
        
#         return t[0]
            
        