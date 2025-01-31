'''
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

 

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 500
grid[i][j] is either 0 or 1.
'''
from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        parent=dict()
        size=dict()
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        maxsize=1
        def findparent(x):
            if parent[x]!=x:
                parent[x]=findparent(parent[x])
            return parent[x]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    prev=None
                    for dx,dy in directions:
                        curx=i+dx
                        cury=j+dy
                        if 0<=curx<rows and 0<=cury<cols:
                            if (curx,cury) in parent:
                                if prev is None:
                                    rootparent=findparent(parent[(curx,cury)])
                                    parent[(i,j)]=(curx,cury)
                                    size[rootparent]+=1
                                    maxsize=max(maxsize,size[rootparent])
                                    prev=rootparent
                                else:
                                    curparent=findparent(parent[(curx,cury)])
                                    if curparent!=prev:
                                        size[prev]+=size[curparent]
                                        size.pop(curparent)
                                        parent[curparent]=prev
                                        maxsize=max(maxsize,size[prev])

                    if (i,j) not in parent:
                        parent[(i,j)]=(i,j)
                        size[(i,j)]=1
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    tempsize=0
                    set1=set()
                    for dx,dy in directions:
                        curx=i+dx
                        cury=j+dy
                        if 0<=curx<rows and 0<=cury<cols:
                            if (curx,cury) in parent:
                                rootparent=findparent((curx,cury))
                                if rootparent in size and rootparent not in set1:
                                    set1.add(rootparent)
                                    tempsize+=size[parent[(curx,cury)]]
                    maxsize=max(maxsize,tempsize+1)
        return maxsize
sol=Solution()
grid = [[1,0],[0,1]]
# grid = [[1,1],[1,0]]
# grid=[[1,1],[1,1]]
# grid=[[0,0],[0,0]]
# grid=[[1,0,0,1,1],[1,0,0,1,0],[1,1,1,1,1],[1,1,1,0,1],[0,0,0,1,0]]
# grid=[[0,1,0,0,1,0,0,0],[1,1,0,1,0,1,1,0],[1,1,1,0,0,1,1,1],[1,0,0,1,1,0,1,0],[0,0,1,1,1,1,0,1],[0,0,1,1,1,0,1,0],[0,0,1,0,1,0,0,0],[0,0,0,1,1,1,1,0]]
print(sol.largestIsland(grid)) #3