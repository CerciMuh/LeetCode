class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1
        result=0
        def find(x):
            if parent[x]==x:
                return x

            parent[x] = find(parent[x]) 
            return parent[x]

        def union(a,b):
            rootA = find(a)
            rootB = find(b)
            if rootA!=rootB:
                parent[rootA]=rootB
                
        parent=[i for i in range(n)]

        for a,b in connections:
            union(a,b)
        for c in range(n):
            if find(c)==c:
                result+=1
        return result-1


