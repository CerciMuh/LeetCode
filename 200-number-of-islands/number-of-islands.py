class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
            if not grid:
                return 0
            rows=len(grid)
            cols=len(grid[0])
            def dfs(x,y):
                if x>=len(grid)or 0>x or y<0 or y>= len(grid[0]) or grid[x][y]=="0"  :
                    return

                grid[x][y] = "0"

                dfs(x+1,y)
                dfs(x-1,y)
                dfs(x,y+1)
                dfs(x,y-1)
            count = 0

            for r in range( rows):
                for c in range (cols):
                    if grid[r][c] == "1":
                        dfs(r, c)
                        count += 1
            return count