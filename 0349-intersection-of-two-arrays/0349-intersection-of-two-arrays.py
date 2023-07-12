class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # n, looped = len(nums1), nums1 if len(nums1) < len(nums2) else len(nums2), nums2
        if len(nums1) < len(nums2):
            looped = set(nums1)
            checked = set(nums2)
        else:
            looped = set(nums2)
            checked = set(nums1)
        intersec = []
        
        for num in looped:
            if num in checked:
                intersec += [num]
                
        return intersec
        