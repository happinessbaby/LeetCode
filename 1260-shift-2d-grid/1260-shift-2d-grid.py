import numpy as np

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        row_num = len(grid)
        col_num = len(grid[0])
        # new_matrix = [[0]*col_num]*row_num
        new_matrix = np.zeros((row_num, col_num), dtype=int)
        for i in range(row_num):
            for j in range(col_num):
                #check if j+1+k>col_num
                #if true, d, r = divmod((j+k)/col_num)
                #d%row_num = number of rows to shift, r = new col idx
                (d, r)= divmod(j+k, col_num)
                d = (i+d)%row_num
                # new_matrix[d][r]=grid[i][j]
                new_matrix[d, r] = grid[i][j]
        return new_matrix
                