'''
Given an incomplete Sudoku configuration in terms of a 9x9  2-D interger square matrix, mat[][], the task is to solve the Sudoku. It is guaranteed that the input Sudoku will have exactly one solution.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Note: Zeros represent blanks to be filled with numbers 1-9, while non-zero cells are fixed and cannot be changed.

Examples:

Input: mat[][] = 

Output:

Explanation: Each row, column and 3 x 3 box of the output matrix contains unique numbers.
Input: mat[][] = 

Output:

Explanation: Each row, column and 3 x 3 box of the output matrix contains unique numbers.
Constraints:
mat.size() = 9
mat[i].size() = 9
0 ≤ mat[i][j] ≤ 9
'''
from collections import defaultdict
class Solution:
    
    #Function to find a solved Sudoku. 
    def solveSudoku(self, mat):
        # Your code here
        def solvepuzzle(row,col):
            if row==9:
                return True
            if col+1==9:
                nextcol=0
                nextrow=row+1
            else:
                nextcol=col+1
                nextrow=row

            if mat[row][col]>0:
                return solvepuzzle(nextrow,nextcol)
            else:
                minmatrow=row//3
                minmatcol=col//3
                for i in range(1,10):
                    if i in rows[row] or i in cols[col] or i in minmat[(minmatrow,minmatcol)]:
                        continue
                    else:
                        mat[row][col]=i
                        rows[row].add(i)
                        cols[col].add(i)
                        minmat[(minmatrow,minmatcol)].add(i)
                        if solvepuzzle(nextrow,nextcol):
                            return True
                        else:
                            mat[row][col]=0
                            rows[row].remove(i)
                            cols[col].remove(i)
                            minmat[(minmatrow,minmatcol)].remove(i)
                return False
                    
        rows=[] #9 set for each row
        cols=[] #9 set for each column
        minmat=defaultdict(set) #9 set for each 3*3 matrix
        
        for i in range(9):
            rows.append(set())
            for j in range(9):
                if len(cols)<j+1:
                    cols.append(set())
                if mat[i][j]==0:
                    continue
                else:
                    rows[i].add(mat[i][j])
                    cols[j].add(mat[i][j])
                    minmatrow=i//3
                    minmatcol=j//3
                    minmat[(minmatrow,minmatcol)].add(mat[i][j])
        solvepuzzle(0,0)
        return mat
sol=Solution()
mat=[
    [3, 0, 6, 5, 7, 8, 4, 0, 0],
     [5, 2, 0, 0, 0, 0, 0, 0, 0],
     [0, 8, 7, 0, 0, 0, 0, 3, 1],
     [0, 0, 3, 0, 1, 0, 0, 8, 0],
     [9, 0, 0, 8, 6, 3, 0, 0, 5],
     [0, 5, 0, 0, 9, 0, 6, 0, 0],
     [1, 3, 0, 0, 0, 0, 2, 5, 0],
     [0, 0, 0, 0, 0, 0, 0, 7, 4],
     [0, 0, 5, 2, 8, 6, 3, 0, 0]
     ]
print(sol.solveSudoku(mat))