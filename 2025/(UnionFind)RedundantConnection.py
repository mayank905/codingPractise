'''
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 

Example 1:


Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Example 2:


Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
 

Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.
'''
from collections import defaultdict
from typing import List
#Solution 1:
#Also Better Optimized

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1
            return True
        return False

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges) + 1)
        result=[]
        for n1, n2 in edges:
            if not uf.union(n1, n2):
                result.append([n1,n2])
        return result[-1]
        
'''
class Grp:
    def __init__(self,n):
        self.name=n
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        grps=dict()
        adrs=defaultdict(list)
        stack=[]
        for n1,n2 in edges:
            if n1 in grps and n2 in grps:
                if grps[n1]==grps[n2]:
                    stack.append((n1,n2))
                else:
                    if len(adrs[grps[n1]])>len(adrs[grps[n2]]):
                        templist=adrs[grps[n2]].copy()
                        tempnode=grps[n2]
                        while templist:
                            cur=templist.pop()
                            grps[cur]=grps[n1]
                            adrs[grps[n1]].append(cur)
                        adrs[tempnode]=[]
                    else:
                        templist=adrs[grps[n1]].copy()
                        tempnode=grps[n1]
                        while templist:
                            cur=templist.pop()
                            grps[cur]=grps[n2]
                            adrs[grps[n2]].append(cur)
                        adrs[tempnode]=[]
            else:
                if n1 in grps:
                    grps[n2]=grps[n1]
                    adrs[grps[n1]].append(n2)
                elif n2 in grps:
                    grps[n1]=grps[n2]
                    adrs[grps[n2]].append(n1)
                else:
                    address=Grp(n1)
                    grps[n1]=address
                    grps[n2]=address
                    adrs[address].append(n1)
                    adrs[address].append(n2)
        return stack[-1]
'''
sol=Solution()
edges = [[1,2],[1,3],[2,3]]
edges=[[1,2],[2,3],[3,4],[1,4],[1,5]]
edges=[[9,10],[5,8],[2,6],[1,5],[3,8],[4,9],[8,10],[4,10],[6,8],[7,9]]
edges=[[16,25],[7,9],[3,24],[10,20],[15,24],[2,8],[19,21],[2,15],[13,20],[5,21],[7,11],[6,23],[7,16],[1,8],[17,20],[4,19],[11,22],[5,11],[1,16],[14,20],[1,4],[22,23],[12,20],[15,18],[12,16]]
# edges=[[21,22],[4,7],[12,13],[13,25],[12,15],[17,23],[15,16],[8,21],[23,24],[3,9],[19,21],[13,21],[4,10],[5,6],[1,20],[10,16],[1,4],[10,14],[5,20],[1,2],[3,24],[2,11],[11,24],[24,25],[17,18]]
print(sol.findRedundantConnection(edges))# [2,3]