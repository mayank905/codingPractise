'''
Given a Directed Acyclic Graph (DAG) of V (0 to V-1) vertices and E edges represented as a 2D list of edges[][], where each entry edges[i] = [u, v] denotes an directed edge u -> v. Return topological sort for the given graph.

Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge u -> v, vertex u comes before v in the ordering.
Note: As there are multiple Topological orders possible, you may return any of them. If your returned Topological sort is correct then the output will be true else false.

Examples:

Input: V = 4, E = 3, edges[][] = [[3, 0], [1, 0], [2, 0]]

Output: true
Explanation: The output true denotes that the order is valid. Few valid Topological orders for the given graph are:
[3, 2, 1, 0]
[1, 2, 3, 0]
[2, 3, 1, 0]
Input: V = 6, E = 6, edges[][] = [[1, 3], [2, 3], [4, 1], [4, 0], [5, 0], [5,2]]

Output: true
Explanation: The output true denotes that the order is valid. Few valid Topological orders for the graph are:
[4, 5, 0, 1, 2, 3]
[5, 2, 4, 0, 1, 3]
Constraints:
2  ≤  V  ≤  103
1  ≤  E = edges.size()  ≤  (V * (V - 1)) / 2
'''
class Solution:
    
    def topoSort(self, V, edges):
        # Code here
        # Create an adjacency list from the edges
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
        # Initialize indegree array
        indegree = [0] * V
        # Calculate indegree of each vertex
        for u in range(V):
            for v in adj[u]:
                indegree[v] += 1
        # Initialize queue for vertices with indegree 0
        queue = []
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)
        # Initialize result list for topological order
        topo_order = []
        # Perform BFS
        while queue:
            node = queue.pop(0)
            topo_order.append(node)
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        # Check if topological sort is possible (i.e., no cycles)
        if len(topo_order) == V:
            return True
        else:
            return False
# The above code is a solution to the Topological Sort problem for Directed Acyclic Graphs (DAGs). It constructs an adjacency list from the given edges, calculates the indegree of each vertex, and uses BFS to generate a topological order. If the length of the resulting topological order matches the number of vertices, it returns True, indicating a valid topological sort exists; otherwise, it returns False.
