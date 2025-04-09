'''
You are given an undirected graph with V vertices and E edges. The graph is represented as a 2D array edges[][], where each element edges[i] = [u, v] indicates an undirected edge between vertices u and v.
Your task is to return all the articulation points (or cut vertices) in the graph.
An articulation point is a vertex whose removal, along with all its connected edges, increases the number of connected components in the graph.

Note: The graph may be disconnected, i.e., it may consist of more than one connected component.
If no such point exists, return {-1}.

Examples :

Input: V = 5, edges[][] = [[0, 1], [1, 4], [4, 3], [4, 2], [2, 3]]

Output: [1, 4]
Explanation: Removing the vertex 1 or 4 will disconnects the graph as-
   
Input: V = 4, edges[][] = [[0, 1], [0, 2]]
Output: [0]
Explanation: Removing the vertex 0 will increase the number of disconnected components to 3.  
Constraints:
1 ≤ V, E ≤ 104
'''
class Solution:
    def articulationPoints(self, V, edges):
        # code here
        def findpoints(root,adj,time,lowestTime,firstTime,ap,visited,parent):
            visited[root]=True
            time+=1
            lowestTime[root]=time
            firstTime[root]=time
            child=0
            for aj in adj[root]:
                if not visited[aj]:
                    child+=1
                    findpoints(aj,adj,time,lowestTime,firstTime,ap,visited,root)
                    lowestTime[root]=min(lowestTime[aj],lowestTime[root])
                    if parent!=-1 and lowestTime[aj]>=firstTime[root]:
                        ap[root]=True
                elif aj!=parent:
                    lowestTime[root]=min(lowestTime[root],firstTime[aj])
            if parent==-1 and child>1:
                ap[root]=1
                
        visited=[False]*V
        adj=[[] for _ in range(V)]
        lowestTime=[0]*V
        firstTime=[0]*V
        ap=[False]*V
        time=0
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        for i in range(V):
            if not visited[i]:
                findpoints(i,adj,time,lowestTime,firstTime,ap,visited,-1)
        result=[index for index in range(V) if ap[index]]
        return result if result else [-1]
sol=Solution()
print(sol.articulationPoints(5, [[0, 1], [1, 4], [4, 3], [4, 2], [2, 3]])) # Output: [1, 4]