class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # nums_set = set(nums)
        for ind, num in enumerate(nums):
            nums_set = set(nums[:ind] + nums[ind+1:])
            if target-num in nums_set and ind != nums.index(target-num):
                return [ind, nums.index(target-num)]