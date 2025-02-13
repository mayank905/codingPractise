'''
Given the root of a Binary search tree(BST), where exactly two nodes were swapped by mistake. Your task is to fix (or correct) the BST by swapping them back. Do not change the structure of the tree.
Note: It is guaranteed that the given input will form BST, except for 2 nodes that will be wrong. All changes must be reflected in the original linked list.
 
Examples :
Input: root = [10, 5, 8, 2, 20]
     
Output: 1
       

Explanation: The nodes 20 and 8 were swapped. 
Input: root = [5, 10, 20, 2, 8]
     
Output: 1 
     
Explanation: The nodes 10 and 5 were swapped.
Constraints:
1 ≤ Number of nodes ≤ 103
'''

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def correctBST(self, root):
        # your code here
        def traverse(root,list1,node):
            if root.left:
                traverse(root.left,list1,node)
            node.append(root)
            list1.append(root.data)
            if root.right:
                traverse(root.right,list1,node)
        list1=[]
        node=[]
        traverse(root,list1,node)
        elist1=list(enumerate(list1))
        elist1.sort(key=lambda x:x[1])
        for i in range(len(elist1)):
            if elist1[i][1]!=node[i].data:
                temp=node[i].data
                node[i].data=elist1[i][1]
                node[elist1[i][0]].data=temp
                break
        return root
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
root_list=[10, 5, 8, 2, 20]
# root_list=[-2, -10, -90]
root = construct_tree_from_list(root_list)

print(sol.correctBST(root)) 