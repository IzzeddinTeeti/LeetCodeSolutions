class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = float('-inf')
        n = len(grid)
        m = len(grid[0])
        self.count = 0
        directions = [[1, 0], [-1, 0], [0, 1],[0, -1]]
        
        def dfs(i,j):
            grid[i][j] = 0
            self.count+=1
            
            for x, y in directions:
                if (0 <= i+x < n) and (0 <= j+y < m) and (grid[i+x][j+y] == 1):
                    dfs(i+x, j+y)
                    
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    dfs(i,j)
                    max_area= max(max_area,self.count)
                    self.count = 0
                    
        return max_area if max_area != float('-inf') else 0