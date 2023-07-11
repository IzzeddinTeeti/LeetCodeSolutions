class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        upper_limit = len(nums)
        exist = {}
        
        for num in range(upper_limit +1):
            if num not in nums:
                return num
        