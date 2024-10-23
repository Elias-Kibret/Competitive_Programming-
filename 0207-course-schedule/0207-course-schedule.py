class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build adjacency list for the graph
        adj_list = {i: [] for i in range(numCourses)}
        for dest, src in prerequisites:
            adj_list[src].append(dest)
        
        # Create sets to track visited nodes and the recursion stack
        visited = set()
        recStack = set()

        # Helper function to perform DFS
        def dfs(v):
            if v in recStack:  # Cycle detected
                return False
            if v in visited:  # Node already fully processed
                return True
            
            # Add the current node to the recursion stack
            recStack.add(v)

            # Visit all the neighbors (outgoing edges)
            for neighbor in adj_list[v]:
                if not dfs(neighbor):
                    return False
            
            # Remove the node from recursion stack and mark it as fully processed
            recStack.remove(v)
            visited.add(v)
            
            return True
        
        # Perform DFS for each course
        for course in range(numCourses):
            if course not in visited:
                if not dfs(course):
                    return False  # Cycle detected
        
        return True  # No cycles, courses can be finished
