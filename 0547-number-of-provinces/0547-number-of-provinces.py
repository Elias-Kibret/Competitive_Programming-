class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj_list = self.convertAdjMatrixToAdjList(isConnected)
        visited = set()
        provinces = 0
        
        for i in range(len(adj_list)):
            if i not in visited:  # Only start DFS if the city hasn't been visited
                self.dfsIterative(adj_list, i, visited)
                provinces += 1  # Increment provinces when a new DFS traversal starts
                
        return provinces

    def convertAdjMatrixToAdjList(self, isConnected):
        adj_list = defaultdict(list)
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    adj_list[i].append(j)  # Append the neighbor j, not i
                    
        return adj_list

    def dfsRec(self, adj_list, start, visited):
        visited.add(start)  # Mark the current city as visited
        
        for neighbor in adj_list[start]:
            if neighbor not in visited:
                self.dfsRec(adj_list, neighbor, visited)  # Recursively visit all neighbors
    def dfsIterative(self,adj_list,start,visted):  
        stack=[start]
        while stack:
            node=stack.pop()
            

            if node not in visted:
                visted.add(node)
                for neigh in adj_list[node]:
                    if neigh not in visted:

                        stack.append(neigh)
    
