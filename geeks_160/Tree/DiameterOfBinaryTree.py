'''
Given a binary tree, the diameter (also known as the width) is defined as the number of edges on the longest path between two leaf nodes in the tree. This path may or may not pass through the root. Your task is to find the diameter of the tree.

Examples:

Input: root[] = [1, 2, 3]

Output: 2
Explanation: The longest path has 2 edges (node 2 -> node 1 -> node 3).

Input: root[] = [5, 8, 6, 3, 7, 9]

Output: 4
Explanation: The longest path has 4 edges (node 3 -> node 8 -> node 5 -> node 6 -> node 9).

Constraints:
1 ≤ number of nodes ≤ 105
0 ≤ node->data ≤ 105
'''

# Python3 program to find the diameter of a Binary Tree

# A binary tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def diameter(self, root):
        # Your code here
        def dfs(root):
            global maxpath
            if not root:
                return -1
            curlength=0
            left=1+dfs(root.left)
            right=1+dfs(root.right)
            curlength=left+right
            maxpath=max(maxpath,curlength)
            return max(left,right)
        global maxpath
        maxpath=0
        dfs(root)
        return maxpath

# Driver code
if __name__ == '__main__':
    # Construct the Binary Tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    sol=Solution()
    print(sol.diameter(root))  # Output: 3

    root = Node(5)
    root.left = Node(8)
    root.right = Node(6)
    root.left.left = Node(3)
    root.left.right = Node(7)
    root.right.right = Node(9)

    print(sol.diameter(root))  # Output: 4