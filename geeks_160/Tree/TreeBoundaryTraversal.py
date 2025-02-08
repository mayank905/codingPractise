'''
Given a Binary Tree, find its Boundary Traversal. The traversal should be in the following order: 

Left Boundary: This includes all the nodes on the path from the root to the leftmost leaf node. You must prefer the left child over the right child when traversing. Do not include leaf nodes in this section.

Leaf Nodes: All leaf nodes, in left-to-right order, that are not part of the left or right boundary.

Reverse Right Boundary: This includes all the nodes on the path from the rightmost leaf node to the root, traversed in reverse order. You must prefer the right child over the left child when traversing. Do not include the root in this section if it was already included in the left boundary.

Note: If the root doesn't have a left subtree or right subtree, then the root itself is the left or right boundary. 

Examples:

Input: root[] = [1, 2, 3, 4, 5, 6, 7, N, N, 8, 9, N, N, N, N]
Output: [1, 2, 4, 8, 9, 6, 7, 3]
Explanation:

Input: root[] = [1, 2, N, 4, 9, 6, 5, N, 3, N, N, N, N 7, 8]
Output: [1, 2, 4, 6, 5, 7, 8]
Explanation:












As the root doesn't have a right subtree, the right boundary is not included in the traversal.
Input: root[] = [1, N, 2, N, 3, N, 4, N, N] 
    1
     \
      2
       \
        3
         \
          4

Output: [1, 4, 3, 2]
Explanation:
Left boundary: [1] (as there is no left subtree)
Leaf nodes: [4]
Right boundary: [3, 2] (in reverse order)
Final traversal: [1, 4, 3, 2]
Constraints:
1 ≤ number of nodes ≤ 105
1 ≤ node->data ≤ 105
'''

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def boundaryTraversal(self, root):
        # Code here
        def traverse(r,l,le,ri,bn):
            if bn=='root':
                l.append(r.data)
                if r.left:
                    traverse(r.left,l,le,ri,'left')
                if r.right:
                    traverse(r.right,l,le,ri,'right')
            if bn=='left':
                l.append(r.data)
                if r.left:
                    traverse(r.left,l,le,ri,'left')
                    if r.right:
                        traverse(r.right,l,le,ri,'leaf')
                elif r.right:
                    traverse(r.right,l,le,ri,'left')
            if bn=='right':
                ri.append(r.data)
                if r.right:
                    if r.left:
                        traverse(r.left,l,le,ri,'leaf')
                    traverse(r.right,l,le,ri,'right')
                elif r.left:
                    traverse(r.left,l,le,ri,'right')
            if bn=='leaf':
                if r.left:
                    traverse(r.left,l,le,ri,'leaf')
                if r.right:
                    traverse(r.right,l,le,ri,'leaf')
                if not r.left and not r.right:
                    le.append(r.data)
            
            
        leftboundary=[]
        leafboundary=[]
        rightboundary=[]
        traverse(root,leftboundary,leafboundary,rightboundary,'root')
        result=[]
        if leftboundary:
            result.extend(leftboundary)
        if leafboundary:
            result.extend(leafboundary)
        if rightboundary:
            result.extend(rightboundary[::-1])
        return result

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

root_list = [1, 2, None, None, 3, 4, None, 5, None, 6, None, 7, 8, None, None, None, None]
root = construct_tree_from_list(root_list)

print(sol.boundaryTraversal(root)) 