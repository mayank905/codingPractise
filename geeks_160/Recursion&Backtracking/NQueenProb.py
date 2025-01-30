'''
The n-queens puzzle is the problem of placing n queens on a (n × n) chessboard such that no two queens can attack each other. Note that two queens attack each other if they are placed on the same row, the same column, or the same diagonal.

Given an integer n, find all distinct solutions to the n-queens puzzle.
You can return your answer in any order but each solution should represent a distinct board configuration of the queen placements, where the solutions are represented as permutations of [1, 2, 3, ..., n]. In this representation, the number in the ith position denotes the row in which the queen is placed in the ith column.
For eg. below figure represents a chessboard [3 1 4 2].



Examples:

Input: n = 1
Output: [1]
Explaination: Only one queen can be placed in the single cell available.
Input: n = 4
Output: [[2 4 1 3 ] [3 1 4 2 ]]
Explaination: There are 2 possible solutions for n = 4.
Input: n = 2
Output: []
Explaination: There are no possible solutions for n = 2.
Constraints:
1 ≤ n ≤ 10
'''
# import copy
# class Solution:
#     def nQueen(self, n):
#         # code here
#         # one visited 2D list pass recursively to track node where queen cant be placed
#         #one global list to store result
#         def newds(ncurlist,nvisited,row,column):
#             ncurlist.append(row+1)
#             nvisited[row][column]=1
#             #fill nvisited row
#             for i in range(column+1,n):
#                 nvisited[row][i]=1
#             #fill nvisited upper diagonal
#             temprow=row-1
#             tempcolumn=column+1
#             while temprow>=0 and tempcolumn<n:
#                 nvisited[temprow][tempcolumn]=1
#                 temprow-=1
#                 tempcolumn+=1
#             #fill nvisited lower diagonal
#             temprow=row+1
#             tempcolumn=column+1
#             while temprow<n and tempcolumn<n:
#                 nvisited[temprow][tempcolumn]=1
#                 temprow+=1
#                 tempcolumn+=1
#             return [ncurlist,nvisited]
            
#         def solveprob(curlist,visited,column):
#             if column==n:
#                 result.append(curlist)
#                 return
#             else:
#                 for row in range(n):
#                     if visited[row][column]:
#                         continue
#                     else:
#                         newcurlist,newvisited=newds(copy.deepcopy(curlist),copy.deepcopy(visited),row,column)
#                         solveprob(newcurlist,newvisited,column+1)
#                 return 
                        
                        
                            
#         result=[]
#         visited=[[0 for _ in range(n)] for _ in range(n)]
#         column=0
#         curlist=[]
#         solveprob(curlist,visited,column)
#         return result
class Solution:
    def nQueen(self, n):
        def solveprob(col, rows, diag1, diag2, curlist):
            if col == n:
                result.append(curlist[:])
                return
            for row in range(n):
                if row in rows or (col - row) in diag1 or (col + row) in diag2:
                    continue
                rows.add(row)
                diag1.add(col - row)
                diag2.add(col + row)
                curlist.append(row+1)
                solveprob(col + 1, rows, diag1, diag2, curlist)
                rows.remove(row)
                diag1.remove(col - row)
                diag2.remove(col + row)
                curlist.pop()

        result = []
        solveprob(0, set(), set(), set(), [])
        return result
sol=Solution()
print(sol.nQueen(4))