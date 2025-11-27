class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        n = len(s)
        

        parent = list(range(n))
        rank = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]


        def union(a, b):
            rootA, rootB = find(a), find(b)
            if rootA == rootB:
                return

            if rank[rootA] < rank[rootB]:
                parent[rootA] = rootB
            elif rank[rootA] > rank[rootB]:
                parent[rootB] = rootA
            else:
                parent[rootB] = rootA
                rank[rootA] += 1


        for a, b in pairs:
            union(a, b)


        from collections import defaultdict
        components = defaultdict(list)

        for i in range(n):
            root = find(i)
            components[root].append(i)


        s = list(s)

        for indices in components.values():
            chars = [s[i] for i in indices]
            indices.sort()
            chars.sort()
            for idx, ch in zip(indices, chars):
                s[idx] = ch

        return "".join(s)
