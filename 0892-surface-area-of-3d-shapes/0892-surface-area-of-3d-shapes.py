class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        area = 0
        
        for row in range(n):
            for col in range(n):
                if grid[row][col]:
                    area += 4 * grid[row][col] + 2
                if row+1 < n:
                    area -= 2 * min(grid[row][col], grid[row+1][col])
                if col+1 < n:
                    area -= 2 * min(grid[row][col], grid[row][col+1])
                
                
        
        return area