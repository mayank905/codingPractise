'''
Given a BST and an integer k, the task is to find the kth smallest element in the BST. If there is no kth smallest element present then return -1.

Examples:

Input: root = [2, 1, 3], k = 2
    
Output: 2
Explanation: 2 is the 2nd smallest element in the BST.
Input: root = [2, 1, 3], k = 5
    
Output: -1
Explanation: There is no 5th smallest element in the BST as the size of BST is 3.
Input: root = [20, 8, 22, 4, 12, N, N, N, N, 10, 14], k = 3
     
Output: 10
Explanation: 10 is the 3rd smallest element in the BST.
Constraints:

1 <= number of nodes, k <= 105
1 <= node->data <= 105
'''


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    # Return the kth smallest element in the given BST 
    def kthSmallest(self, root, k): 
        #code here.
        global result
        def traverse(root):
            global k
            global result
            if root.left:
                traverse(root.left)
            k-=1
            if k==0:
                result=root.data
                return
            if root.right:
                traverse(root.right)
            
        result=-1
        traverse(root)
        return result
sol=Solution()
# write code to construct tree
def construct_tree_from_list(lst):
    if not lst or lst[0] is None:
        return None

    root = Node(lst[0])
    queue = [root]
    i = 1

    while queue and i < len(lst):
        current = queue.pop(0)
        if lst[i] is not None:
            current.left = Node(lst[i])
            queue.append(current.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            current.right = Node(lst[i])
            queue.append(current.right)
        i += 1

    return root

root_list = [20, 8, 22, 4, 12, None, None, None, None, 10, 14]
k = 3
root = construct_tree_from_list(root_list)

print(sol.kthSmallest(root,k)) 
