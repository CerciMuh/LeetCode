class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def bfs(r,c):
            queue = [(r,c)]
            board[r][c]= "T"
            directions =[(1,0),(-1,0),(0,1),(0,-1)]
            while queue:
                x,y = queue.pop(0)
                for dx,dy in directions:
                    if x + dx <len(board) and x+dx >= 0 and y+dy>=0 and y+dy < len(board[0]) and board[x+dx][y+dy]=="O":
                        board[x+dx][y+dy]="T"
                        queue.append((x+dx,y+dy))
        
        for r in range (len(board)):
            for c in range(len(board[0])):
                if (r == len(board)-1 or r == 0 or c ==len(board[0])-1 or c == 0 )and board[r][c]=="O":
                    bfs(r,c)


        for r in range (len(board)):
            for c in range(len(board[0])):
                if board[r][c] =="T":
                    board [r][c] = "O"       
                elif board [r][c]=="O":
                    board[r][c] = "X"
