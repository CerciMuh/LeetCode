class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}

        for a, b in prerequisites:
            graph[b].append(a)
        visiting = set()
        visited = set()
        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return True
            visiting.add(node)

            for neighbor in graph[node]:
                if dfs(neighbor)==False:
                    return False
            visiting.remove(node)
            visited.add(node)
            return True
        
        for course in range(numCourses):
            if dfs(course) == False:
                return False
        return True
