class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        visited = {}
                
        for ind, num in enumerate(nums):
            if target-num in visited.keys():
                return [visited[target-num], ind]
            else:
                visited[num] = ind
            
        
        