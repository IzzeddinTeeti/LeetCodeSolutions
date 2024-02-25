class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        total_sum = n*(n+1)/2
        current_sum = sum(nums)
        
        return int(total_sum-current_sum)
            
#         n = len(nums)
        
#         nums = set(nums)
        
#         for i in range(n+1):
#             if i not in nums:
#                 return i
          # total_sum = n * (n+1) / 2
        
            
        