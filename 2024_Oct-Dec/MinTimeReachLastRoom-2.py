from collections import deque
import math
from typing import List


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        N = len(moveTime)
        M = len(moveTime[0])

        dp = [[math.inf] * M for _ in range(N)]
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        queue = deque()
        queue.append(([0,0], 0, 1)) # position, time
        
        while queue:
            cur_pos, cur_time, cur_steps= queue.popleft()
            for dr in directions:
                next_pos = [cur_pos[0]+dr[0], cur_pos[1]+dr[1]]
                if next_pos[0] in range(N) and next_pos[1] in range(M):
                    can_move_time = moveTime[next_pos[0]][next_pos[1]]
                    next_time = 0
                    if cur_time >= can_move_time: # can move
                        next_time = min(dp[next_pos[0]][next_pos[1]], cur_time + cur_steps)
                    else: # need to wait                       
                        next_time = can_move_time + cur_steps
                    if next_time < dp[next_pos[0]][next_pos[1]]:
                        dp[next_pos[0]][next_pos[1]] = next_time
                        if cur_steps==1:
                            step=2
                        else:
                            step=1
                        queue.append((next_pos, next_time, step))

        return dp[N-1][M-1]

sol=Solution()
result=[]
moveTime = [
    # [[0,1],[1,2]],#3
    # [[0,0,0],[0,0,0]],#3
    # [[0,0,0,0],[0,0,0,0]],
    # [[0,4],[4,4]],#6
    # [[94,79,62,27,69,84],[6,32,11,82,42,30]],#72
    [[0,58],[27,69]] #71
            ]
for i in range(len(moveTime)):  
    result.append(sol.minTimeToReach(moveTime[i]))
print(result)