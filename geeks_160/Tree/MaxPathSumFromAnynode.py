'''
Given a binary tree, the task is to find the maximum path sum. The path may start and end at any node in the tree.

Examples:

Input: root[] = [10, 2, 10, 20, 1, N, -25, N, N, N, N, 3, 4]
Output: 42
Explanation: 

Max path sum is represented using green colour nodes in the above binary tree.
Input: root[] = [-17, 11, 4, 20, -2, 10]
Output: 31
Explanation: 

Max path sum is represented using green colour nodes in the above binary tree.
Constraints:
1 ≤ number of nodes ≤ 103
-104 ≤ node->data ≤ 104
'''


class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    #Function to return maximum path sum from any node in a tree.
    def findMaxSum(self, root): 
        #Your code here
        global max1
        def currentSum(root):
            global max1
            if root==None:
                return -10**4
            left=currentSum(root.left)
            right=currentSum(root.right)
            max2=max(left,right)
            max1=max(max1,left,right,root.data,root.data+left+right,root.data+max2)
            if max2<0:
                return root.data
            return root.data+max2
        max1=-10**4
        currentSum(root)
        return max1
    
# Driver code
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

root_list = [10, 2, 10, 20, 1, None, -25, None, None, None, None, 3, 4]
root_list=[10, 2, -25, 20, 1, 3, 4]
# root_list=[-2, -10, -90]
root = construct_tree_from_list(root_list)

print(sol.findMaxSum(root)) 