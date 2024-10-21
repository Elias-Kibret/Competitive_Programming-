class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)
        
        visited = set()
        provinces = 0
        
        # Loop through each city
        for i in range(len(isConnected)):
            if i not in visited:  # If the city hasn't been visited, start a DFS
                visited.add(i)
                dfs(i)
                provinces += 1  # One more connected component (province) found
        
        return provinces
