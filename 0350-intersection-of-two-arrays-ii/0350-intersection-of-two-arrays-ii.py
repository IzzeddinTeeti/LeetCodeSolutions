import collections

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        nums1 = collections.Counter(nums1)
        nums2 = collections.Counter(nums2)
        
        if len(nums1) < len(nums2):
            looped = nums1
            checked = nums2
        else:
            looped = nums2
            checked = nums1
        
        ans = []
        for key in looped.keys():
            if key in checked.keys():
                ans += [key] * min(looped[key], checked[key])
                checked[key] -= min(looped[key], checked[key])
                
                
        return ans
            
        