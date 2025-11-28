class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parent = [i for i in range(len(isConnected))]


        def find(x):
            if parent[x]==x:
                return x
            else:
                return find(parent[x])
        def union(x,y):
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return
            else: 
                parent[rootX] = rootY
            
        for r in range(len(isConnected)):
            for c in range(len(isConnected[0])):
                if isConnected[r][c]==1:
                    union(r,c)
        numProvinces = 0
        for i in range(len(parent)):
            if find(i)==i:
                numProvinces+=1
        return numProvinces