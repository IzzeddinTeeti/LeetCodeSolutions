class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows <= 1 or len(s) <= numRows:
            return s

        current_row = 0
        direction = -1
        rows = [''] * numRows

        for char in s:
            rows[current_row] += char

            if current_row == 0 or current_row == numRows-1:
                direction *= -1
            
            current_row += direction 

        return ''.join(rows)
        
        
        