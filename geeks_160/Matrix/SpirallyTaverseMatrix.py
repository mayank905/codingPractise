'''
You are given a rectangular matrix mat[][] of size n x m, and your task is to return an array while traversing the matrix in spiral form.

Examples:

Input: mat[][] = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
Output: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
Explanation: 

Input: mat[][] = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]
Output: [1, 2, 3, 4, 5, 6, 12, 18, 17, 16, 15, 14, 13, 7, 8, 9, 10, 11]
Explanation: Applying same technique as shown above.
Input: mat[][] = [[32, 44, 27, 23], [54, 28, 50, 62]]
Output: [32, 44, 27, 23, 62, 50, 28, 54]
Explanation: Applying same technique as shown above, output will be [32, 44, 27, 23, 62, 50, 28, 54].
Constraints:
1 <= n, m <= 1000
0 <= mat[i][j]<= 100
'''

class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, mat):
        # code here
        row=len(mat)
        col=len(mat[0])
        count=row*col
        repmat=[[1 for _ in range(col)]for i in range(row)]
        dir=[(0,1),(1,0),(0,-1),(-1,0)]
        dirlength=4
        d=0
        r,c=0,-1
        result=[]
        while count!=0:
            left=dir[d][0]
            right=dir[d][1]
            if 0<=r+left<row and 0<=c+right<col and repmat[r+left][c+right]:
                r+=left
                c+=right
                count-=1
                repmat[r][c]=0
                result.append(mat[r][c])
            else:
                d=(d+1)%dirlength
        
        return result  