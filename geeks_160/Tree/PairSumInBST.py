'''
Given a Binary Search Tree(BST) and a target. Check whether there's a pair of Nodes in the BST with value summing up to the target. 

Examples:

Input: root = [7, 3, 8, 2, 4, N, 9], target = 12
       bst
Output: True
Explanation: In the binary tree above, there are two nodes (8 and 4) that add up to 12.
Input: root = [9, 5, 10, 2, 6, N, 12], target = 23
          bst-3
Output: False
Explanation: In the binary tree above, there are no such two nodes exists that add up to 23.
Constraints:

1 ≤ Number of Nodes ≤ 105
1 ≤ target ≤ 106
'''

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''

class Solution:
    def findTarget(self, root, target): 
        # your code here.
        def traverse(root,dict1):
            if not root:
                return False
            if target-root.data in dict1:
                return True
            dict1.add(root.data)
            bol1=traverse(root.left,dict1)
            bol2=traverse(root.right,dict1)
            return bol1 or bol2
        dict1=set()
        return traverse(root,dict1)