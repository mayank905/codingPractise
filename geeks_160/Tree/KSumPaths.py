'''
Given a binary tree and an integer k, determine the number of downward-only paths where the sum of the node values in the path equals k. A path can start and end at any node within the tree but must always move downward (from parent to child).

Examples:

Input: k = 7   
                8
               /  \
              4    5
             /  \    \
            3    2    2
           / \    \
          3   -2   1

Output: 3
Explanation: The following paths sum to k 
 
Input: k = 3
   1
  /  \
2     3
Output: 2
Explanation:
Path 1 : 1 -> 2 (Sum = 3)
Path 2 : 3 (Sum = 3)
Constraints:

1 ≤ number of nodes ≤ 104
-100 ≤ node value ≤ 100
-109 ≤ k ≤ 109
'''


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def sumK(self, root, k):
        def count_paths_with_sum(node, current_sum):
            if not node:
                return 0

            current_sum += node.data
            sum_count = prefix_count.get(current_sum - k, 0)

            prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1

            sum_count += count_paths_with_sum(node.left, current_sum)
            sum_count += count_paths_with_sum(node.right, current_sum)

            prefix_count[current_sum] -= 1

            return sum_count
        prefix_count=dict()
        prefix_count[0]=1
        return count_paths_with_sum(root, 0)

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
root_list=[8, 4, 5, 3, 2, None, 2, 3, -2, None, 1]
# root_list=[-2, -10, -90]
root = construct_tree_from_list(root_list)
k=7
print(sol.sumK(root,k))
    