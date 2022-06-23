class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        len1, len2 = len(nums1), len(nums2)
        
        counts, looped = (collections.Counter(nums2), nums1) if (len1 < len2) else (collections.Counter(nums1), nums2)
            
        for num in looped:
            if num in counts.keys() and counts[num] > 0:
                ans.append(num)
                counts[num] -= 1
        return ans
        
        