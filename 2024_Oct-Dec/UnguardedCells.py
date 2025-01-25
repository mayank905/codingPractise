from typing import List


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid=[[0]*n for _ in range(m)]
        for x,y in guards:
            grid[x][y]=2
        for wall in walls:
            grid[wall[0]][wall[1]]=2
        dirs=[(-1,0),(0,1),(1,0),(0,-1)]
        for gx,gy in guards:
            for dx,dy in dirs:
                x,y=gx,gy
                while True:
                    x+=dx
                    y+=dy
                    if x<0 or x>=m or y<0 or y>=n or grid[x][y]==2:
                        break
                    grid[x][y]=1
        
        unguardCount=sum(row.count(0) for row in grid)

        return unguardCount
    
sol=Solution()
m,n,guards,walls=5,5,[[0,0],[0,4],[4,0],[4,4]],[[2,2]]
# m,n,guards,walls=3,3,[[1,1]],[[0,1],[1,0],[2,1],[1,2]]
print(sol.countUnguarded(m,n,guards,walls)) #25