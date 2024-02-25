class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        passed = {}
        
        for ind, num in enumerate(nums):
            
            if target- num in passed.keys():
                return [ind, passed[target-num]]
            else:
                passed[num] = ind