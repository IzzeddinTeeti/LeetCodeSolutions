class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        
        n = (n-1)%14 + 1
        total = len(cells)
        
        for day in range(n):
            new_cells = [0] * total
            
            for cell in range(1,7):
                new_cells[cell] = int(cells[cell-1]==cells[cell+1])
            
            cells = new_cells
            
        return cells
                    
        
                
                    
        