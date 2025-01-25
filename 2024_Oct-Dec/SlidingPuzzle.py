from typing import List

###   DFS Approach  ###########
'''
class Solution:
    # Direction map for zero's possible moves in a flattened 1D array (2x3 board)
    directions = [
        [1, 3],
        [0, 2, 4],
        [1, 5],
        [0, 4],
        [3, 5, 1],
        [4, 2],
    ]

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # Helper method to swap characters at indices i and j in the string
        def _swap(s, i, j):
            s = list(s)
            s[i], s[j] = s[j], s[i]
            return "".join(s)

        # Convert the 2D board into a string representation to use as state
        start_state = "".join(str(num) for row in board for num in row)

        # Dictionary to store the minimum moves for each visited state
        visited = {}

        def _dfs(state, zero_pos, moves):
            # Skip if this state has been visited with fewer or equal moves
            if state in visited and visited[state] <= moves:
                return
            visited[state] = moves

            # Try moving zero to each possible adjacent position
            for next_pos in self.directions[zero_pos]:
                new_state = _swap(
                    state, zero_pos, next_pos
                )  # Swap to generate new state
                _dfs(
                    new_state, next_pos, moves + 1
                )  # Recursive DFS with updated state and move count

        # Start DFS traversal from initial board state
        _dfs(start_state, start_state.index("0"), 0)

        # Return the minimum moves required to reach the target state, or -1 if unreachable
        return visited.get("123450", -1)
'''
###   BFS Approach  ###########

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # Direction map for zero's possible moves in a flattened 1D array (2x3 board)
        directions = [
            [1, 3],
            [0, 2, 4],
            [1, 5],
            [0, 4],
            [3, 5, 1],
            [4, 2],
        ]

        # Convert the 2D board into a string representation to use as state
        start_state = "".join(str(num) for row in board for num in row)

        # Initialize queue with the initial state and zero position
        queue = [(start_state, start_state.index("0"), 0)]
        visited = {start_state}

        # BFS traversal
        while queue:
            state, zero_pos, moves = queue.pop(0)

            # Return moves if target state is reached
            if state == "123450":
                return moves

            # Try moving zero to each possible adjacent position
            for next_pos in directions[zero_pos]:
                new_state = self._swap(state, zero_pos, next_pos)  # Swap to generate new state

                # Skip if this state has been visited
                if new_state in visited:
                    continue
                visited.add(new_state)

                # Add the new state to the queue for further traversal
                queue.append((new_state, next_pos, moves + 1))

        # Return -1 if target state is unreachable
        return -1

    # Helper method to swap characters at indices i and j in the string
    def _swap(self, s, i, j):
        s = list(s)
        s[i], s[j] = s[j], s[i]
        return "".join(s)

sol=Solution()
boards=[[[1, 2, 3], [4, 0, 5]],
        [[1, 2, 3], [5, 4, 0]],
        [[4, 1, 2], [5, 0, 3]],
        [[3, 2, 4], [1, 5, 0]],
        [[1, 2, 3], [5, 0, 4]]]
for board in boards:
    print(sol.slidingPuzzle(board))