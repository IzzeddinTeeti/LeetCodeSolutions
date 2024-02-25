class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        visited = {}
        
        for num in nums:
            if num in visited.keys():
                visited[num] += 1
            else:
                visited[num] = 1
                
        ans = []
        for num in visited.keys():
            if visited[num] == 1:
                ans.append(num)
                
        return ans
            
        