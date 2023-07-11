class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        passed = {}
        
        for ind, value in enumerate(nums):
            if target-value in passed.keys():
                return [passed[target-value], ind]
            else:
                passed[value] = ind
                
        
        