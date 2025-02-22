'''
We run a preorder depth-first search (DFS) on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.

If a node has only one child, that child is guaranteed to be the left child.

Given the output traversal of this traversal, recover the tree and return its root.

 

Example 1:


Input: traversal = "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]
Example 2:


Input: traversal = "1-2--3---4-5--6---7"
Output: [1,2,5,3,null,6,null,4,null,7]
Example 3:


Input: traversal = "1-401--349---90--88"
Output: [1,401,null,349,88,90]
 

Constraints:

The number of nodes in the original tree is in the range [1, 1000].
1 <= Node.val <= 109
'''
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack=[]
        depth=0
        st=''
        traversal+='-'
        for ch in traversal:
            if ch!='-':
                st+=ch
            else:
                if st=='':
                    depth+=1
                else:
                    if not stack:
                        node=TreeNode(int(st))
                        stack.append((1,node))
                        st=''
                        depth=1
                        continue
                    node=TreeNode(int(st))
                    while stack[-1][0]!=depth:
                        stack.pop()
                    cur=stack[-1][1]
                    if not cur.left:
                        cur.left=node
                    else:
                        cur.right=node
                    stack.append((depth+1,node))
                    depth=1
                    st=''
        return stack[0][1]
sol=Solution()
traversal="1-2--3--4-5--6--7"
traversal="1-401--349---90--88"
traversal="1-2--3--4-5--6--7"
print(sol.recoverFromPreorder(traversal))