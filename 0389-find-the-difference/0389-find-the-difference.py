class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        tot_s = sum([ord(char) for char in s])
        tot_t = sum([ord(char) for char in t])
        
        diff = tot_t - tot_s
        
        return chr(diff)
    