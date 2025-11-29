class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacificVisited = [[False] * cols for _ in range(rows)]
        atlanticVisited = [[False] * cols for _ in range(rows)]
        def dfs(x,y,visited):
            if visited[x][y] == True:
                return
            visited[x][y] = True
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            for dx, dy in directions:
                ndx = dx+x
                ndy = dy+y
                if ndx < len(visited) and ndx >= 0 and ndy < len(visited[0]) and ndy >= 0 and heights[ndx][ndy]>=heights[x][y] and visited[ndx][ndy]==False:
                    dfs(ndx,ndy,visited)
        
        for c in range(cols):
            dfs (0,c,pacificVisited)
        for r in range(rows):
            dfs(r,0,pacificVisited) 
        for c in range(cols):
            dfs (rows-1,c,atlanticVisited)
        for r in range(rows):
            dfs(r,cols-1,atlanticVisited)
        
        result = []
        for r in range(rows):
            for c in range(cols):
                if pacificVisited[r][c] and atlanticVisited[r][c]:
                    result.append([r, c])
        return result
        