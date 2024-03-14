class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        n = len(nums)
        
        counter = 0
        
        for num in nums:
            if num != val:
                nums[counter] = num
                counter += 1
                
        return counter
                
        