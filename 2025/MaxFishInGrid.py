'''
You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:

A land cell if grid[r][c] = 0, or
A water cell containing grid[r][c] fish, if grid[r][c] > 0.
A fisher can start at any water cell (r, c) and can do the following operations any number of times:

Catch all the fish at cell (r, c), or
Move to any adjacent water cell.
Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.

An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.

 

Example 1:


Input: grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
Output: 7
Explanation: The fisher can start at cell (1,3) and collect 3 fish, then move to cell (2,3) and collect 4 fish.
Example 2:


Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
Output: 1
Explanation: The fisher can start at cells (0,0) or (3,3) and collect a single fish. 
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
0 <= grid[i][j] <= 10
'''

from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        visited=[[0]*cols for _ in range(rows)]
        maxsum=0
        def isvalid(x,y):
            return 0<=x<rows and 0<=y<cols
        for i in range(rows):
            for j in range(cols):
                cursum=0
                if grid[i][j]==0 or visited[i][j]:
                    visited[i][j]=1
                    continue
                else:
                    q=[(i,j)]
                    visited[i][j]=1
                    while q:
                        curx,cury=q.pop(0)
                        cursum+=grid[curx][cury]
                        for dx,dy in directions:
                            x=curx+dx
                            y=cury+dy
                            if isvalid(x,y) and grid[x][y]>0 and not visited[x][y]:
                                visited[x][y]=1
                                q.append((x,y))
                    maxsum=max(maxsum,cursum)
        return maxsum
                        
sol=Solution()
grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
grid = [[6,1,10]]
print(sol.findMaxFish(grid))