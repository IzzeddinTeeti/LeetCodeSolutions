class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        l = ind = 0
        r = n-1
        
        while l <= r:
            m = l + ((r-l) //2 )
            
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m+1
                ind = m+1
            else:
                r = m-1
        
        return ind
        