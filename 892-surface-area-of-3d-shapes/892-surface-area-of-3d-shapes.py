class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        
        top_down = sum([sum(i > 0 for i in row) for row in grid]) * 2
        sides = sum([sum(i for i in row) for row in grid]) * 4
        
        hor_adj = sum([adjecent(row) for row in grid])
        ver_adj = sum([adjecent(row) for row in zip(*grid)])
        
        return top_down + sides - hor_adj - ver_adj
        
def adjecent(row: list[int]) -> int:

    total = 0

    for i in range(len(row)-1):
        if row[i] and row[i+1]:
            total += min(row[i], row[i+1]) * 2
    return total