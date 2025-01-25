from collections import deque
import math
from typing import List

# def update(rowIndex,colIndex,ct,rowLength,colLength,matrix,dir):
#     if rowIndex==rowLength-1 and colIndex==colLength-1:
#         return
#     if dir!='up':
#         if rowIndex+1<=rowLength-1:
#             if ct>=matrix[rowIndex+1][colIndex]:
#                 minTime(rowIndex+1,colIndex,ct+1,rowLength,colLength,matrix,'down')
#             else:
#                 minTime(rowIndex+1,colIndex,matrix[rowIndex+1][colIndex]+1,rowLength,colLength,matrix,'down')
#     if dir!='down':
#         if rowIndex-1>=0:
#             if ct>=matrix[rowIndex-1][colIndex]:
#                 minTime(rowIndex-1,colIndex,ct+1,rowLength,colLength,matrix,'up')
#             else:
#                 minTime(rowIndex-1,colIndex,matrix[rowIndex-1][colIndex]+1,rowLength,colLength,matrix,'up')
#     if dir!='left':
#         if colIndex+1<=colLength-1:
#             if ct>=matrix[rowIndex][colIndex+1]:
#                 minTime(rowIndex,colIndex+1,ct+1,rowLength,colLength,matrix,'right')
#             else:
#                 minTime(rowIndex,colIndex+1,matrix[rowIndex][colIndex+1]+1,rowLength,colLength,matrix,'right')
#     if dir!='right':
#         if colIndex-1>=0:
#             if ct>=matrix[rowIndex][colIndex-1]:
#                 minTime(rowIndex,colIndex-1,ct+1,rowLength,colLength,matrix,'left')
#             else:
#                 minTime(rowIndex,colIndex-1,matrix[rowIndex][colIndex-1]+1,rowLength,colLength,matrix,'left')

# def minTime(rowIndex,colIndex,ct,rowLength,colLength,matrix,dir):
#     if visit[rowIndex][colIndex]!=-1:
#         if visit[rowIndex][colIndex]<ct:
#             return
#         else:
#             visit[rowIndex][colIndex]=ct
#             update(rowIndex,colIndex,ct,rowLength,colLength,matrix,dir)
#             return
#     else:
#         visit[rowIndex][colIndex]=ct
#         update(rowIndex,colIndex,ct,rowLength,colLength,matrix,dir)
#         return

# class Solution:
#     def minTimeToReach(self, moveTime: List[List[int]]) -> int:
#         global visit
#         row=len(moveTime)
#         col=len(moveTime[0])
#         visit=[[-1 for i in range(col)]for j in range(row)]
#         i=0
#         j=0
#         ct=0
#         minTime(i,j,ct,row,col,moveTime,'')
#         return visit[row-1][col-1]

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        N = len(moveTime)
        M = len(moveTime[0])

        dp = [[math.inf] * M for _ in range(N)]
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        queue = deque()
        queue.append(([0,0], 0)) # position, time
        
        while queue:
            cur_pos, cur_time = queue.popleft()
            for dr in directions:
                next_pos = [cur_pos[0]+dr[0], cur_pos[1]+dr[1]]
                if next_pos[0] in range(N) and next_pos[1] in range(M):
                    can_move_time = moveTime[next_pos[0]][next_pos[1]]
                    next_time = 0
                    if cur_time >= can_move_time: # can move
                        next_time = min(dp[next_pos[0]][next_pos[1]], cur_time + 1)
                    else: # need to wait                       
                        next_time = can_move_time + 1
                    if next_time < dp[next_pos[0]][next_pos[1]]:
                        dp[next_pos[0]][next_pos[1]] = next_time
                        queue.append((next_pos, next_time))

        return dp[N-1][M-1]

sol=Solution()
result=[]
moveTime = [
    [[0,1],[1,2]],#3
    [[0,0,0],[0,0,0]],#3
    [[0,4],[4,4]],#6
    [[94,79,62,27,69,84],[6,32,11,82,42,30]]#72
            ]
for i in range(len(moveTime)):  
    result.append(sol.minTimeToReach(moveTime[i]))
print(result)

'''
There is a dungeon with n x m rooms arranged as a grid.

You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes exactly one second.

Return the minimum time to reach the room (n - 1, m - 1).

Two rooms are adjacent if they share a common wall, either horizontally or vertically.
'''