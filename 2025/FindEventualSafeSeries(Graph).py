'''
There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

 

Example 1:

Illustration of graph
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Explanation: The given graph is shown above.
Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.
Example 2:

Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
Output: [4]
Explanation:
Only node 4 is a terminal node, and every path starting at node 4 leads to node 4.
 

Constraints:

n == graph.length
1 <= n <= 104
0 <= graph[i].length <= n
0 <= graph[i][j] <= n - 1
graph[i] is sorted in a strictly increasing order.
The graph may contain self-loops.
The number of edges in the graph will be in the range [1, 4 * 104].
'''

#Solution Using DFS

from typing import List


class Solution:
    def dfs(self, node, adj, visit, inStack):
        # If the node is already in the stack, we have a cycle.
        if inStack[node]:
            return True
        if visit[node]:
            return False
        # Mark the current node as visited and part of current recursion stack.
        visit[node] = True
        inStack[node] = True
        for neighbor in adj[node]:
            if self.dfs(neighbor, adj, visit, inStack):
                return True
        # Remove the node from the stack.
        inStack[node] = False
        return False

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        visit = [False] * n
        inStack = [False] * n

        for i in range(n):
            self.dfs(i, graph, visit, inStack)

        safeNodes = []
        for i in range(n):
            if not inStack[i]:
                safeNodes.append(i)

        return safeNodes

# Solution 2: Using Topological Sort

from collections import deque

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        # Create the reverse graph.
        revGraph = [[] for _ in range(n)]
        outDegree = [0] * n
        for i in range(n):
            outDegree[i] = len(graph[i])
            for neighbor in graph[i]:
                revGraph[neighbor].append(i)

        # Initialize the queue with terminal nodes.
        queue = deque()
        for i in range(n):
            if outDegree[i] == 0:
                queue.append(i)

        # Perform topological sort.
        while queue:
            node = queue.popleft()
            for neighbor in revGraph[node]:
                outDegree[neighbor] -= 1
                if outDegree[neighbor] == 0:
                    queue.append(neighbor)

        return [i for i in range(n) if outDegree[i] == 0]
sol=Solution()
graph = [[1,2],[2,3],[5],[0],[5],[],[]]
print(sol.eventualSafeNodes(graph))  # Expected output: [2,4,5,6]