class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        n = len(nums)
        difference = float('inf')
        result = 0

        for i in range(n):
            left = i+1
            right = n-1

            if i>0 and nums[i] == nums[i-1]:
                continue

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if abs(total-target) <= difference:
                    difference = abs(total-target)
                    result = total

                
                if total > target:
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    return result

        return result



        