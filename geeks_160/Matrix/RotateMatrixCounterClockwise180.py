'''
Given a 2D square matrix mat[][] of size n x n, turn it by 180 degrees without using extra space.

Note: You must rotate the matrix in place and modify the input matrix directly.

Examples:

Input: mat[][] = [[1, 2],
                [3, 4]]
Output: [[4, 3], 
        [2, 1]]
Input:  mat[][] = [[1, 2, 3, 4], 
                 [5, 6, 7 ,8], 
                 [9, 10, 11, 12],
                 [13, 14, 15, 16]]
Output: [[16, 15, 14, 13], 
        [12, 11, 10, 9], 
        [8, 7, 6, 5], 
        [4, 3, 2, 1]]
Constraints:
1 ≤ n ≤ 500
0 <= mat[i][j] <= 104
'''

class Solution:
    def rotateMatrix(self, mat):
        # Code here
        for row in mat:
           row.reverse()
        rows=len(mat)
        left=0
        right=rows-1
        while left<right:
            mat[left],mat[right]=mat[right],mat[left]
            left+=1
            right-=1
        return mat
sol=Solution()
mat=[[1, 2, 3, 4], 
                 [5, 6, 7 ,8], 
                 [9, 10, 11, 12],
                 [13, 14, 15, 16]]
print(sol.rotateMatrix(mat))