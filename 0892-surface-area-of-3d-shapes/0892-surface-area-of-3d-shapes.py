class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        top_bot = sum([sum([2 if i>0 else 0 for i in row]) for row in grid])
        
        side = 0
        
        for row in range(n):
            for col in range(n):
                side += 4 * grid[row][col]
                if row+1 < n:
                    side -= 2 * min(grid[row][col], grid[row+1][col])
                if col+1 < n:
                    side -= 2 * min(grid[row][col], grid[row][col+1])
                
                
        
        res = side + top_bot        
        return res