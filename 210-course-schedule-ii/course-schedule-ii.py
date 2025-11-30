class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        for a,b in prerequisites:
            graph[b].append(a)
        visiting = set()
        visited = set()
        order = []

        def dfs(node):
            if node in visiting:
                return False
            if node in visited: 
                return True
            visiting.add(node)
            for neighbor in graph[node]:
                if dfs(neighbor) == False:
                    return False
            visiting.remove(node)
            visited.add(node)
            order.append(node)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return []

        return order[::-1]  

