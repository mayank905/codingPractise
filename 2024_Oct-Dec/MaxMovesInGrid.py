from typing import List


def moves(currentval,currentrow,currentcol,totalrow,totalcol,matrix,grid):
    first,second,third=0,0,0
    if (currentrow>=totalrow or currentrow<0 or currentcol>=totalcol or currentcol<0):
        return 0
    elif matrix[currentrow][currentcol]!=-1:
        return matrix[currentrow][currentcol]
    elif currentcol!=0:
        if grid[currentrow][currentcol]<=currentval:
            return 0
        else:
            first,second,third=1,1,1
        
    first+=moves(grid[currentrow][currentcol],currentrow-1,currentcol+1,totalrow,totalcol,matrix,grid)
    second+=moves(grid[currentrow][currentcol],currentrow,currentcol+1,totalrow,totalcol,matrix,grid)
    third+=moves(grid[currentrow][currentcol],currentrow+1,currentcol+1,totalrow,totalcol,matrix,grid)

    currentmax=max(first,second,third)
    matrix[currentrow][currentcol]=currentmax
    return currentmax

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        maxlength=0
        matrix = [[-1 for x in range(cols)] for y in range(rows)]
        col=0
        for row in range(rows):
            maxlength=max(moves(grid[row][col],row,col,rows,cols,matrix,grid),maxlength)
        return maxlength
    
sol=Solution()
# grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
grid = [[3,2,4],[2,1,9],[1,1,7]]
result=sol.maxMoves(grid)
print(result)