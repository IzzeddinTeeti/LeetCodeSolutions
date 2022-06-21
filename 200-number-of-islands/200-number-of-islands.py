# import numpy as np

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ans = 0
        
        def dfs(r, c):
            grid[r][c] = 0
            directions = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]

            for r, c in directions:
                if r>=0 and r<len(grid) and c>=0 and c<len(grid[0]) and grid[r][c] == '1':
                    dfs(r, c)
            return
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    dfs(r, c)
                    ans += 1
        return ans
                    
                    
                
        