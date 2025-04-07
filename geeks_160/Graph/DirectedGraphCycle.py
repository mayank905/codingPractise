'''
Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, check whether it contains any cycle or not.
The graph is represented as a 2D vector edges[][], where each entry edges[i] = [u, v] denotes an edge from verticex u to v.

Examples:

Input: V = 4, edges[][] = [[0, 1], [1, 2], [2, 3], [3, 3]]



Output: true
Explanation: 3 -> 3 is a cycle
Input: V = 3, edges[][] = [[0, 1], [1, 2]]



Output: false
Explanation: no cycle in the graph
Constraints:
1 ≤ V, E ≤ 105
'''
from collections import defaultdict
class Solution:
    def isCycle(self, V, edges):
        # code here
        vertex=defaultdict(list)
        def isCycle(node,visit):
            if node not in vertex:
                return False
            if node in visit:
                return True
            visit.add(node)
            for adj in vertex[node]:
                if isCycle(adj,visit):
                    return True
            visit.remove(node)
            return False
        for u,v in edges:
            vertex[u].append(v)
        for i in range(V):
            set1=set()
            if isCycle(i,set1):
                return True
        return False
sol=Solution()
# print(sol.isCycle(4, [[0, 1], [1, 2], [2, 3], [3, 3]])) # Output: True
# edges=[[0, 1], [1, 2]]
# print(sol.isCycle(3, edges)) # Output: False
# edges=[[0, 3],[0, 1],[1, 3]]
# print(sol.isCycle(4, edges)) # Output: False
edges=[
[2, 0],
[1, 0],
[3, 2],
[4, 2],
[3, 4],
[3, 1]]
print(sol.isCycle(5, edges)) # Output: False