import math

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        counts = collections.Counter()
        # print()
        ans = 0
        
        for t in time:
            ans += counts.get(60 - t%60 if t%60 else 0, 0)
            print(t, ans)
            counts[t%60] +=1
        return ans