'''
Given a grid of size n*m (n is the number of rows and m is the number of columns in the grid) consisting of 'W's (Water) and 'L's (Land). Find the number of islands.

Note: An island is either surrounded by water or the boundary of a grid and is formed by connecting adjacent lands horizontally or vertically or diagonally i.e., in all 8 directions.

Examples:

Input: grid[][] = [['L', 'L', 'W', 'W', 'W'], ['W', 'L', 'W', 'W', 'L'], ['L', 'W', 'W', 'L', 'L'], ['W', 'W', 'W', 'W', 'W'], ['L', 'W', 'L', 'L', 'W']]
Output: 4
Explanation:
The image below shows all the 4 islands in the grid.
 
Input: grid[][] = [['W', 'L', 'L', 'L', 'W', 'W', 'W'], ['W', 'W', 'L', 'L', 'W', 'L', 'W']]
Output: 2
Expanation:
The image below shows 2 islands in the grid.
 
Constraints:
1 ≤ n, m ≤ 500
grid[i][j] = {'L', 'W'}
'''
class Solution:
    def numIslands(self, grid):
        # code here
        row=len(grid)
        col=len(grid[0])
        visited=[[True if grid[i][j] == 'W' else False for j in range(col)] for i in range(row)]
        directions=[(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
        count=0
        for i in range(row):
            for j in range(col):
                if not visited[i][j]:
                    count+=1
                    que=[(i,j)]
                    while que:
                        x,y=que.pop(0)
                        if not visited[x][y]:
                            visited[x][y]=True
                            for dx,dy in directions:
                                if 0<=x+dx<row and  0<=y+dy<col and not visited[x+dx][y+dy]:
                                    que.append((x+dx,y+dy))
        return count