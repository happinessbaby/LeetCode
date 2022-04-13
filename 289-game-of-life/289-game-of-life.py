class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #{dead->dead: 0, alive->dead: 1, dead->alive: 2, alive->alive: 3}
        final_states = {0:0, 1:0, 2:1, 3:1}
        i,j=0,0
        row_len = len(board)
        col_len = len(board[0])
        neighbors = [(1,0), (-1,0),(0,1),(0,-1),(-1,-1),(1,1),(-1,1),(1,-1)]
        for i in range(row_len):
            for j in range(col_len):
                live_count = 0
                for n in neighbors:
                    x = n[0]+i
                    y = n[1]+j
                    if x>=0 and x<row_len and y>=0 and y<col_len:
                        #if neighbor originally alive, live_count plus 1
                        if board[x][y]==1 or board[x][y]==3:
                            live_count+=1
                #change current cell in place
                if board[i][j]==0:
                    if live_count==3:
                        board[i][j]=2
                if board[i][j]==1:
                    if live_count==2 or live_count==3:
                        board[i][j]=3
                    else:
                        board[i][j]=1
        for i in range(row_len):
            for j in range(col_len):
                board[i][j]=final_states[board[i][j]]
                
                    
                    
                    
                
        