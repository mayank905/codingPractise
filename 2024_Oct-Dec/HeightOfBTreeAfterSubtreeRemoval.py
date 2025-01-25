from typing import List, Optional

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
'''
#Approach no.1 - Two traversal Root,Left,Right and Root,Right,Left
'''
class Solution:
    def treeQueries(
        self, root: Optional[TreeNode], queries: List[int]
    ) -> List[int]:
        max_height_after_removal = [0] * 100001
        self.current_max_height = 0

        def _traverse_left_to_right(node, current_height):
            if not node:
                return

            # Store the maximum height if this node were removed
            max_height_after_removal[node.val] = self.current_max_height

            # Update the current maximum height
            self.current_max_height = max(
                self.current_max_height, current_height
            )

            # Traverse left subtree first, then right
            _traverse_left_to_right(node.left, current_height + 1)
            _traverse_left_to_right(node.right, current_height + 1)

        def _traverse_right_to_left(node, current_height):
            if not node:
                return

            # Update the maximum height if this node were removed
            max_height_after_removal[node.val] = max(
                max_height_after_removal[node.val], self.current_max_height
            )

            # Update the current maximum height
            self.current_max_height = max(
                current_height, self.current_max_height
            )

            # Traverse right subtree first, then left
            _traverse_right_to_left(node.right, current_height + 1)
            _traverse_right_to_left(node.left, current_height + 1)

        _traverse_left_to_right(root, 0)
        self.current_max_height = 0  # Reset for the second traversal
        _traverse_right_to_left(root, 0)

        # Process queries and build the result list
        return [max_height_after_removal[q] for q in queries]

'''
#Approach No.2 - Single traversal

class Solution:
    def treeQueries(
        self, root: Optional[TreeNode], queries: List[int]
    ) -> List[int]:
        result_map = {}
        height_cache = {}

        # Function to calculate the height of the tree
        def _height(node):
            if not node:
                return -1

            # Return cached height if already calculated
            if node in height_cache:
                return height_cache[node]

            h = 1 + max(_height(node.left), _height(node.right))
            height_cache[node] = h
            return h

        # DFS to precompute the maximum values after removing the subtree
        def _dfs(node, depth, max_val):
            if not node:
                return

            result_map[node.val] = max_val

            # Traverse left and right subtrees while updating max values
            _dfs(
                node.left,
                depth + 1,
                max(max_val, depth + 1 + _height(node.right)),
            )
            _dfs(
                node.right,
                depth + 1,
                max(max_val, depth + 1 + _height(node.left)),
            )

        # Run DFS to fill result_map with maximum heights after each query
        _dfs(root, 0, 0)

        # Build the result array based on the queries
        return [result_map[q] for q in queries]

'''
'''
Approach 3 - Using Subtree Size

class Solution:
    def treeQueries(
        self, root: Optional[TreeNode], queries: List[int]
    ) -> List[int]:
        # Dictionary to store the index of each node val
        node_index_map = {}

        # Dictionary to store the number of nodes in the subtree for each node
        subtree_size = {}

        # Lists to store node depths and maximum depths from left and right
        node_depths = []
        max_depth_from_left = []
        max_depth_from_right = []

        # Perform DFS to populate node_index_map and node_depths
        self._dfs(root, 0, node_index_map, node_depths)

        total_nodes = len(node_depths)

        # Calculate subtree sizes
        self._calculate_subtree_size(root, subtree_size)

        # Calculate maximum depths from left and right
        max_depth_from_left.append(node_depths[0])
        max_depth_from_right.append(node_depths[-1])

        for i in range(1, total_nodes):
            max_depth_from_left.append(
                max(max_depth_from_left[i - 1], node_depths[i])
            )
            max_depth_from_right.append(
                max(
                    max_depth_from_right[i - 1],
                    node_depths[total_nodes - i - 1],
                )
            )

        max_depth_from_right.reverse()

        # Process queries
        results = []
        for query_node in queries:
            start_index = node_index_map[query_node] - 1
            end_index = start_index + 1 + subtree_size[query_node]

            max_depth = max_depth_from_left[start_index]
            if end_index < total_nodes:
                max_depth = max(max_depth, max_depth_from_right[end_index])

            results.append(max_depth)

        return results

    # Depth-first search to populate node_index_map and node_depths
    def _dfs(self, root, depth, node_index_map, node_depths):
        if not root:
            return

        node_index_map[root.val] = len(node_depths)
        node_depths.append(depth)

        self._dfs(root.left, depth + 1, node_index_map, node_depths)
        self._dfs(root.right, depth + 1, node_index_map, node_depths)

    # Calculate the size of the subtree for each node
    def _calculate_subtree_size(self, root, subtree_size):
        if not root:
            return 0

        left_size = self._calculate_subtree_size(root.left, subtree_size)
        right_size = self._calculate_subtree_size(root.right, subtree_size)

        total_size = left_size + right_size + 1
        subtree_size[root.val] = total_size

        return total_size
'''
'''
#Approach -4 Eulerian tour

class Solution:
    def treeQueries(
        self, root: Optional[TreeNode], queries: List[int]
    ) -> List[int]:
        # Lists and dictionaries to store tree information
        euler_tour = []
        node_heights = {}
        first_occurrence = {}
        last_occurrence = {}

        # Depth-first search to build the Euler tour and store node information
        def _dfs(root, height):
            if not root:
                return

            node_heights[root.val] = height
            first_occurrence[root.val] = len(euler_tour)
            euler_tour.append(root.val)

            _dfs(root.left, height + 1)
            _dfs(root.right, height + 1)

            last_occurrence[root.val] = len(euler_tour)
            euler_tour.append(root.val)

        # Perform DFS to build Euler tour and node information
        _dfs(root, 0)

        tour_size = len(euler_tour)
        max_depth_left = [0] * tour_size
        max_depth_right = [0] * tour_size

        # Initialize the first and last elements of max_height arrays
        max_depth_left[0] = max_depth_right[-1] = node_heights[root.val]

        # Build max_depth_left and max_depth_right arrays
        for i in range(1, tour_size):
            max_depth_left[i] = max(
                max_depth_left[i - 1], node_heights[euler_tour[i]]
            )

        for i in range(tour_size - 2, -1, -1):
            max_depth_right[i] = max(
                max_depth_right[i + 1], node_heights[euler_tour[i]]
            )

        # Process queries
        return [
            max(
                (
                    max_depth_left[first_occurrence[q] - 1]
                    if first_occurrence[q] > 0
                    else 0
                ),
                (
                    max_depth_right[last_occurrence[q] + 1]
                    if last_occurrence[q] < tour_size - 1
                    else 0
                ),
            )
            for q in queries
        ]

'''


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_level_order(self, data_list):
        if not data_list:
            return None

        # Initialize the root of the tree
        self.root = TreeNode(data_list[0]) if data_list[0] is not None else None
        queue = [self.root] if self.root else []  # Queue to hold nodes at each level

        i = 1  # Start from the second element in the list
        while i < len(data_list):
            # Process nodes in the queue one by one
            current = queue.pop(0)

            # Assign left child if not None
            if i < len(data_list) and data_list[i] is not None:
                current.left = TreeNode(data_list[i])
                queue.append(current.left)
            i += 1

            # Assign right child if not None
            if i < len(data_list) and data_list[i] is not None:
                current.right = TreeNode(data_list[i])
                queue.append(current.right)
            i += 1

    def print_tree_inorder(self, node):
        # Helper function to print the tree inorder for verification
        if node:
            self.print_tree_inorder(node.left)
            print(node.val, end=" ")
            self.print_tree_inorder(node.right)

# Example usage:
data_list = [5,8,9,2,1,3,7,4,6]  # List of numbers
queries = [3,2,4,8]
# data_list=[1,3,4,2,None,6,5,None,None,None,None,None,7]
# queries = [4]
binary_tree = BinaryTree()
binary_tree.insert_level_order(data_list)
# binary_tree.print_tree_inorder(binary_tree.root)  # Output should be in sorted order for BST
sol=Solution()
resultList=sol.treeQueries(binary_tree.root,queries)
print(resultList)

'''
You are given the root of a binary tree with n nodes. Each node is assigned a unique value from 1 to n. You are also given an array queries of size m.

You have to perform m independent queries on the tree where in the ith query you do the following:

Remove the subtree rooted at the node with the value queries[i] from the tree. It is guaranteed that queries[i] will not be equal to the value of the root.
Return an array answer of size m where answer[i] is the height of the tree after performing the ith query.

Note:

The queries are independent, so the tree returns to its initial state after each query.
The height of a tree is the number of edges in the longest simple path from the root to some node in the tree.
'''