class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last_ind = {}
        
        for i, ch in enumerate(s):
            last_ind[ch] = i
        
        ans = []
        size, end = 0, 0
        
        for i, ch in enumerate(s):
            size +=1
            end = max(end, last_ind[ch])
            
            if i == end:
                ans.append(size)
                size = 0
            
        return ans
            
        