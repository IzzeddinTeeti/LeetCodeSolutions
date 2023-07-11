class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        total_sum = (n * (n + 1)) // 2  # Sum of numbers from 0 to n

        array_sum = sum(nums)  # Sum of elements in the array

        return total_sum - array_sum
        