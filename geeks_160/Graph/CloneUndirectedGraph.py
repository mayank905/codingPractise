'''
Given a connected undirected graph represented by adjacency list, adjList[][] with n nodes, having a distinct label from 0 to n-1, where each adj[i] represents the list of vertices connected to vertex i.

Create a clone of the graph, where each node in the graph contains an integer val and an array (neighbors) of nodes, containing nodes that are adjacent to the current node.

class Node {
    val: integer
    neighbors: List[Node]
}
Your task is to complete the function cloneGraph( ) which takes a starting node of the graph as input and returns the copy of the given node as a reference to the cloned graph.

Note: If you return a correct copy of the given graph, then the driver code will print true; and if an incorrect copy is generated or when you return the original node, the driver code will print false.

Examples :

Input: n = 4, adjList[][] = [[1, 2], [0, 2], [0, 1, 3], [2]]
Output: true
Explanation: 

As the cloned graph is identical to the original one the driver code will print true.
Input: n = 3, adjList[][] = [[1, 2], [0], [0]]
Output: true
Explanation: 

As the cloned graph is identical to the original one the driver code will print true.
Constraints:
1 ≤ n ≤ 104
0 ≤ no. of edges ≤ 105
0 ≤ adjList[i][j] < n
'''

# from collections import defaultdict
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors


class Solution():
    def cloneGraph(self, node):
        #code here
        newNode=dict()
        visited=set()
        root=Node(node.val)
        newNode[node]=root
        q=[node]
        while q:
            length=len(q)
            for i in range(length):
                cur=q.pop(0)
                if cur not in visited:
                    visited.add(cur)
                    if cur in newNode:
                        curnod=newNode[cur]
                    else:
                        curnod=Node(cur.val)
                        newNode[cur]=curnod
                    list1=[]
                    for negh in cur.neighbors:
                        if negh in newNode:
                            nod=newNode[negh]
                        else:
                            nod=Node(negh.val)
                            newNode[negh]=nod
                        if negh not in visited:
                            q.append(negh)
                        list1.append(nod)
                            
                    curnod.neighbors=list1
                    newNode[cur]=curnod
        return root