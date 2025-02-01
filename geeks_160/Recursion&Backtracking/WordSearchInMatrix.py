'''
You are given a two-dimensional mat[][] of size n*m containing English alphabets and a string word. Check if the word exists on the mat. The word can be constructed by using letters from adjacent cells, either horizontally or vertically. The same cell cannot be used more than once.

Examples :

Input: mat[][] = [['T', 'E', 'E'], ['S', 'G', 'K'], ['T', 'E', 'L']], word = "GEEK"
Output: true
Explanation:

The letter cells which are used to construct the "GEEK" are colored.
Input: mat[][] = [['T', 'E', 'U'], ['S', 'G', 'K'], ['T', 'E', 'L']], word = "GEEK"
Output: false
Explanation:

It is impossible to construct the string word from the mat using each cell only once.
Input: mat[][] = [['A', 'B', 'A'], ['B', 'A', 'B']], word = "AB"
Output: true
Explanation:

There are multiple ways to construct the word "AB".
Constraints:
1 ≤ n, m ≤ 6
1 ≤ L ≤ 15
mat and word consists of only lowercase and uppercase English letters.
'''
class Solution:
    def isWordExist(self, mat, word):
        def chkadj(row, col, index):
            if index == len(word):
                return True
            for dx, dy in directions:
                curx, cury = row + dx, col + dy
                if 0 <= curx < rows and 0 <= cury < cols and not visited[curx][cury] and mat[curx][cury] == word[index]:
                    visited[curx][cury] = True
                    if chkadj(curx, cury, index + 1):
                        return True
                    visited[curx][cury] = False
            return False

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(mat), len(mat[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == word[0]:
                    visited[i][j] = True
                    if chkadj(i, j, 1):
                        return True
                    visited[i][j] = False

        return False

# Example usage
sol = Solution()
mat = [['T', 'E', 'E'], ['S', 'G', 'K'], ['T', 'E', 'L']]
word = "GEEK"
print(sol.isWordExist(mat, word))  # Output: False