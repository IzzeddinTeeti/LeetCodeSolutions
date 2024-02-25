class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low = 1
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            count = sum(1 for x in nums if x <= mid)

            if count > mid:
                high = mid
            else:
                low = mid + 1

        return low
        
        
#         visited = {}
        
#         for num in nums:
#             if num in visited.keys():
#                 return num
#             else:
#                 visited[num] = 1
        
        
#         n = len(nums) # 5
        
#         final_n = n-1 #4
        
#         total_sum = (final_n * final_n + final_n) // 2 #12
        
#         current_sum = sum(nums)
        
#         return current_sum - total_sum
        