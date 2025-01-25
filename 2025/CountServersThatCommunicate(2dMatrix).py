'''
You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.

 

Example 1:



Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.
Example 2:



Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.
Example 3:



Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m <= 250
1 <= n <= 250
grid[i][j] == 0 or 1
'''

from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        count=0
        rows=len(grid)
        cols=len(grid[0])
        rlist=[0]*rows
        clist=[0]*cols
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    rlist[i]+=1
                    clist[j]+=1    
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    if rlist[i]>1 or clist[j]>1:
                        count+=1      
        return count
sol=Solution()
grid=[[1,0],[0,1]]
print(sol.countServers(grid))