import math

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        counts = collections.Counter()
        ans = 0
        
        for t in time:
            ans += counts.get(60 - t%60 if t%60 else 0, 0)
            counts[t%60] +=1
        return ans