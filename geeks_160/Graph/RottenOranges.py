'''
Given a matrix mat[][] of dimension n * m where each cell in the matrix can have values 0, 1 or 2 which has the following meaning:
0 : Empty cell
1 : Cell have fresh oranges
2 : Cell have rotten oranges

We have to determine what is the earliest time after which all the oranges are rotten. A rotten orange at index (i, j) can rot other fresh orange at indexes (i-1, j), (i+1, j), (i, j-1), (i, j+1) (up, down, left and right) in a unit time.

Note: Your task is to return the minimum time to rot all the fresh oranges. If not possible returns -1.

Examples:

Input: mat[][] = [[0, 1, 2], [0, 1, 2], [2, 1, 1]]
Output: 1
Explanation: Oranges at positions (0,2), (1,2), (2,0) will rot oranges at (0,1), (1,1), (2,2) and (2,1) in unit time.
Input: mat[][] = [[2, 2, 0, 1]]
Output: -1
Explanation: Oranges at (0,0) and (0,1) can't rot orange at (0,3).
Input: mat[][] = [[2, 2, 2], [0, 2, 0]]
Output: 0
Explanation: There is no fresh orange. 
Constraints:
1 ≤ mat.size() ≤ 500
1 ≤ mat[0].size() ≤ 500
mat[i][j] = {0, 1, 2} 
'''
class Solution:
    def orangesRotting(self, mat):
        #Code here
        row=len(mat)
        col=len(mat[0])
        visited=[[False for j in range(col)] for i in range(row)]
        que=[(i,j) for i in range(row) for j in range(col) if mat[i][j]==2]
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        cur=0
        while que:
            length=len(que)
            for i in range(length):
                r,c=que.pop(0)
                if not visited[r][c]:
                    visited[r][c]=True
                    for dx,dy in directions:
                        if 0<=r+dx<row and 0<=c+dy<col and mat[r+dx][c+dy]==1:
                            que.append((r+dx,c+dy))
                            mat[r+dx][c+dy]=2
            cur+=1

        for i in range(row):
            for j in range(col):
                if mat[i][j]==1:
                    return -1
        return cur-1 if cur>0 else 0
# Example usage:
sol = Solution()
print(sol.orangesRotting([[0, 1, 2], [0, 1, 2], [2, 1, 1]]))  # Output: 1
print(sol.orangesRotting([[2, 2, 0, 1]]))  # Output: -1
print(sol.orangesRotting([[2, 2, 2], [0, 2, 0]]))  # Output: 0