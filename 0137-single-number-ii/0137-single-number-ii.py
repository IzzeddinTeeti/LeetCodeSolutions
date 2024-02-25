class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        passed = {}
        
        for num in nums:
            if num in passed.keys():
                if passed[num] == 1:
                    passed[num] += 1
                else:
                    del passed[num]
            else:
                passed[num] = 1
            
        res = list(passed.keys())
        return res[0]
        