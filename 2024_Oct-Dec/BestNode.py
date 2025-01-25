from collections import defaultdict
from typing import List

class Solution:
    def bestNode(self, N : int, A : List[int], P : List[int]) -> int:
            # code here
            # Create an adjacency list to represent the tree
        tree = defaultdict(list)
        for i in range(1, N):
            parent = P[i]
            child = i + 1
            tree[parent].append(child)
        
        # Helper function to perform DFS and calculate alternating sum for each path
        def dfs(node, sign):
            # Start with the value of the current node with the given sign
            max_sum = sign * A[node - 1]
            local_max = max_sum
            
            # Explore all children, alternate the sign for each level
            for child in tree[node]:
                child_max_sum = dfs(child, -sign)
                local_max = max(local_max, max_sum + child_max_sum)
            
            return local_max

        # Calculate the maximum value of f(B) starting from each node and returning the global max
        global_max = float('-inf')
        for node in range(1, N + 1):
            global_max = max(global_max, dfs(node, 1))
        
        return global_max
        
sol=Solution()
N=3
A=[3,1,2]
P=[-1,1,2]
print(sol.bestNode(N,A,P))