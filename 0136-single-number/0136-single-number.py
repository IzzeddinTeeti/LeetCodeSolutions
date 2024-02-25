class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        passed = {}
        
        for i in nums:
            if i in passed.keys():
                del passed[i]
                
            else:
                passed[i] = 1
                
        
        answer = list(passed.keys())
        return answer[0]
            