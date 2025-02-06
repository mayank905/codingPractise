'''
Given two arrays representing the inorder and preorder traversals of a binary tree, construct the tree and return the root node of the constructed tree.

Note: The output is written in postorder traversal.

Examples:

Input: inorder[] = [1, 6, 8, 7], preorder[] = [1, 6, 7, 8]
Output: [8, 7, 6, 1]
Explanation: The tree will look like

Input: inorder[] = [3, 1, 4, 0, 2, 5], preorder[] = [0, 1, 3, 4, 2, 5]
Output: [3, 4, 1, 5, 2, 0]
Explanation: The tree will look like

Input: inorder[] = [2, 5, 4, 1, 3], preorder[] = [1, 4, 5, 2, 3]
Output: [2, 5, 4, 3, 1]
Explanation: The tree will look like

Constraints:
1 ≤ number of nodes ≤ 103
0 ≤ nodes -> data ≤ 103
Both the inorder and preorder arrays contain unique values
'''

#User function Template for python3
# Node class
class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None


# Note: Build tree and return root node
class Solution:
    def buildTree(self, inorder, preorder):
        # code here
        if not inorder or not preorder:
            return None
        root=Node(preorder[0])
        index=inorder.index(preorder[0])
        root.left=self.buildTree(inorder[:index],preorder[1:index+1])
        root.right=self.buildTree(inorder[index+1:],preorder[index+1:])
        return root
    
    def postOrder(self, root):
        # code here
        if root is None:
            return []
        return self.postOrder(root.left)+self.postOrder(root.right)+[root.data]
    
sol=Solution()
inorder = [1, 6, 8, 7]
preorder = [1, 6, 7, 8]
root=sol.buildTree(inorder, preorder)
print(sol.postOrder(root))  # Output: [8, 7, 6, 1]