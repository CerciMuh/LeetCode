class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        queue=[]
        maxTime=0
        fresh=0
        for r in range (len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==2:
                    queue.append((r,c,0))
                elif grid[r][c] == 1:
                    fresh += 1
        while queue:
            x,y,time = queue.pop(0)
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                    grid[nx][ny] = 2             
                    fresh -= 1
                    queue.append((nx, ny, time+ 1))
                    maxTime = max(maxTime, time + 1)
        if fresh >0:
            return -1
        else:
            return maxTime