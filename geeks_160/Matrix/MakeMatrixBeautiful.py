'''
A beautiful matrix is a matrix in which the sum of elements in each row and column is equal. Given a square matrix mat[][]. Find the minimum number of operation(s) that are required to make the matrix beautiful. In one operation you can increment the value of any one cell by 1.

Examples:

Input: mat[][] = [[1, 2], [3, 4]]
Output: 4
Explanation: Increment value of cell(0, 0) by 3 and increment value of cell(0, 1) by 1. Hence total 4 operation are required. Such that all rows and columns have sum of 7.
Input: mat[][] = [[1, 2, 3], [4, 2, 3], [3, 2, 1]]
Output: 6
Explanation: Increment value of cell(0, 0) by 1, increment value of cell(0, 1) by 2, increment value of cell(2, 1) by 1, increment value of cell(2, 2) by 2. Such that all rows and columns have sum of 9.
Input: mat[][] = [[0, 2], [3, 4]]
Output: 5
Explanation: Increment value of cell(0, 0) by 4, increment value of cell(0, 1) by 1. Hence total 5 operation are required.
Constraints:
1 <= mat.size(), mat[0].size() <= 500
1 <= mat[i][j] <= 106
'''
class Solution:
    def findMinOperation(self, mat):
        # code here
        rows=len(mat)
        cols=len(mat[0])
        rowsum=[0]*rows
        colsum=[0]*cols
        for i in range(rows):
            for j in range(cols):
                rowsum[i]+=mat[i][j]
                colsum[j]+=mat[i][j]
        max1=max(max(rowsum),max(colsum))
        count=0
        for i in range(rows):
            for j in range(cols):
                min1=min(max1-rowsum[i],max1-colsum[j])
                if min1>0:
                    count+=min1
                    mat[i][j]+=min1
                    rowsum[i]+=min1
                    colsum[j]+=min1
        return count
sol=Solution()
print(sol.findMinOperation([[1, 2], [3, 4]])) # Output: 4
print(sol.findMinOperation([[1, 2, 3], [4, 2, 3], [3, 2, 1]])) # Output: 6
print(sol.findMinOperation([[0, 2], [3, 4]])) # Output: 5