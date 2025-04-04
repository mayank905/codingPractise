'''
Given an undirected graph with V vertices and E edges, represented as a 2D vector edges[][], where each entry edges[i] = [u, v] denotes an edge between vertices u and v, determine whether the graph contains a cycle or not.

Examples:

Input: V = 4, E = 4, edges[][] = [[0, 1], [0, 2], [1, 2], [2, 3]]
Output: true
Explanation: 
 
1 -> 2 -> 0 -> 1 is a cycle.
Input: V = 4, E = 3, edges[][] = [[0, 1], [1, 2], [2, 3]]
Output: false
Explanation: 
 
No cycle in the graph.
Constraints:
1 ≤ V ≤ 105
1 ≤ E = edges.size() ≤ 105
'''
class Solution:
    def isCycleUtil(self, node, parent, visited, graph):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if self.isCycleUtil(neighbor, node, visited, graph):
                    return True
            elif parent != neighbor:
                return True
        return False

    def isCycle(self, V, edges):
        graph = [[] for _ in range(V)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * V
        for i in range(V):
            if not visited[i]:
                if self.isCycleUtil(i, -1, visited, graph):
                    return True
        return False
# Example usage:
sol = Solution()
# print(sol.isCycle(4, [[0, 1], [0, 2], [1, 2], [2, 3]]))  # Output: True
print(sol.isCycle(4, [[0, 1], [1, 2], [2, 3]]))  # Output: False