class Solution:
    def totalFruit(self, f: List[int]) -> int:
        start = end = 0
        max_len = 0
        d = {}
        
        while end < len(f):
            d[f[end]] = end
            if len(d) >= 3:
                min_val = min(d.values())
                del d[f[min_val]]
                start = min_val + 1
                
            max_len = max(max_len, end - start + 1)
            end += 1
        
        return max_len
        