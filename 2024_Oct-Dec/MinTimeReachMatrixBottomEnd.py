'''
Minimum Time to Reach Destination in a Grid
You are in a 2D grid of size m x n, and you are located at (0, 0). You are trying to reach a cell with coordinates (m - 1, n - 1).
Each cell in the grid has a non-negative integer value representing the time it takes to visit this cell. If it takes time x to visit a cell, you must wait for x seconds before moving to the next cell.
Return the minimum time to reach the destination. If it is impossible to reach the destination, return -1.
'''
from collections import deque
import heapq
from typing import List


class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        queue=[]
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        rows=len(grid)
        cols=len(grid[0])
        if grid[0][1]>(grid[0][0]+1) and grid[1][0]>(grid[0][0]+1):
            return -1
        visited=[[False for _ in range(cols)] for _ in range(rows)]
        queue.append((grid[0][0],0,0))

        while queue:
            time,row,col=heapq.heappop(queue)
            if row==rows-1 and col==cols-1:
                return time
            if visited[row][col]:
                continue
            visited[row][col]=True
            time+=1
            for dir in directions:
                newrow=row+dir[0]
                newcol=col+dir[1]
                if newrow<0 or newrow>=rows or newcol<0 or newcol>=cols:
                    continue
                else:
                    if visited[newrow][newcol]:
                            continue
                    if grid[newrow][newcol]<=time:
                        heapq.heappush(queue,(time,newrow,newcol))
                    else:
                        diff=grid[newrow][newcol]-time
                        if diff%2==0:
                            newtime=grid[newrow][newcol]
                        else:
                            newtime=grid[newrow][newcol]+1
                        heapq.heappush(queue,(newtime,newrow,newcol))

sol=Solution()
grids = [
    [[0,2,4],[3,2,1],[1,0,4]],#-1
    [[0,1,3,2],[5,1,2,5],[4,3,8,6]],#7
    [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,6],[11,17,16,18,7],[10,9,8,7,19]]#14

]
for grid in grids:
    print(sol.minimumTime(grid))

