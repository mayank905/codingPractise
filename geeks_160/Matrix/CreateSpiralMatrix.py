'''
You are given two positive integers n and m, and an integer array arr[] containing total (n*m) elements. Return a 2D matrix of dimensions n x m by filling it in a clockwise spiral order using the elements from the given array.

Examples:

Input: n = 4, m = 4, arr[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
Output: [[1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7]]
Input: n = 3, m = 4, arr[] =[1, 8, 6, 3, 8, 6, 1, 6, 3, 2, 5, 3]
Output: [[1, 8, 6, 3],
        [2, 5, 3, 8],
        [3, 6, 1, 6]]
Input: n = 2, m = 2, arr[] =[1, 8, 6, 3]
Output: [[1, 8],
        [3, 6]]
Constraints:
1 ≤ n, m ≤ 103
arr.size() = n x m
1 ≤ arr[i] ≤ 103
'''
class Solution:
    def spiralFill(self, n, m, arr):
        # code here
        result=[[-1 for _ in range(m)]for _ in range(n)]
        direction=[(0,1),(1,0),(0,-1),(-1,0)]
        d=0
        x,y=0,0
        for num in arr:
            result[x][y]=num
            upx=x+direction[d][0]
            upy=y+direction[d][1]
            if 0<=upx<n and 0<=upy<m and result[upx][upy]==-1:
                x=upx
                y=upy
            else:
                d=(d+1)%4
                x+=direction[d][0]
                y+=direction[d][1]
        return result
sol=Solution()
n = 4
m = 4
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
print(sol.spiralFill(n,m,arr))