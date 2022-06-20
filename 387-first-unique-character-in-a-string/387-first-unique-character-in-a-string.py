class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        count = collections.Counter(s)
        
        for ind, char in enumerate(s):
            if count[char] == 1:
                return ind
        return -1
                
        